import json
import os
from datetime import timedelta
from typing import Any, Dict, List
from azure.identity import DefaultAzureCredential, get_bearer_token_provider
from openai import AzureOpenAI
from azure.monitor.query import LogsQueryClient, LogsQueryStatus
from azure.monitor.opentelemetry import configure_azure_monitor
from utils.evaluator import evaluate_metric
from dotenv import load_dotenv
import logging
import sys
# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


# Load environment variables
load_dotenv(override=True)



################################ For app insights #######################################
credential = DefaultAzureCredential()
logs_client = LogsQueryClient(credential)
workspace_id= os.environ["APPINSIGHTS_WORKSPACE_ID"]
os.environ["APPLICATIONINSIGHTS_CONNECTION_STRING"] = os.getenv("APPINSIGHTS_CONNECTIONSTRING") # for logging to app insights


############################### For Azure OpenAI Eval Client ##############################

required_openai_env_vars = ["AZURE_OPENAI_ENDPOINT", "AZURE_OPENAI_API_VERSION", "EVAL_DEPLOY_NAME"]
missing_vars = [var for var in required_openai_env_vars if var not in os.environ]

if missing_vars:
    print(f"Error: The following required environment variables are not set: {', '.join(missing_vars)}")
    print("Please set these variables before running the script.")
    sys.exit(1)

azure_opneai_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")
eval_model_deployment = os.getenv("EVAL_DEPLOY_NAME")
azure_api_version = os.getenv("AZURE_OPENAI_API_VERSION")

# Initialize Azure OpenAI client with Entra ID authentication
token_provider = get_bearer_token_provider(
    DefaultAzureCredential(),
    "https://cognitiveservices.azure.com/.default"
)

eval_client = AzureOpenAI(
    azure_endpoint=azure_opneai_endpoint,
    azure_ad_token_provider=token_provider,
    api_version=azure_api_version,
)




def execute_query(query, timespan_days):
    """
    Executes a query on the Azure Application Insights workspace.

    Args:
        query (str): The query to execute.
        timespan_days (int): The number of days to query for the data.

    Returns:
        Table: The result of the query.
    """
    try:
        response = logs_client.query_workspace(
            workspace_id, query, timespan=timedelta(days=timespan_days)
        )
        if response.status != LogsQueryStatus.SUCCESS:
            error = response.partial_error
            logging.error(f"Query failed: {error}")
            return None
        if not response.tables:
            logging.warning("No tables returned in the query.")
            return None
        logging.info(f"Query executed successfully. Result type: {type(response.tables[0])}")
        return response.tables[0]
    except Exception as e:
        logging.error(f"Error in execute_query: {e}")
        return None

def get_interactions(timespan_days, interaction_count):
    query = f"""
    AppDependencies
    | where Properties["task"] == "get_response"
    | order by TimeGenerated desc
    | take {interaction_count}
    | project OperationId, Id
    """
    return execute_query(query, timespan_days)

def get_responses(dependency_id):
    query = f"""
    AppDependencies
    | where ParentId == "{dependency_id}"
    | project OperationId, Id, Properties["gen_ai.response.id"]
    """
    return execute_query( query, timespan_days)

def get_traces( operation_id, timespan_days):
    query = f"""
    AppTraces
    | where ParentId == "{operation_id}"
    """
    return execute_query( query, timespan_days)


def process_traces(traces_table):
    """
    Processes the traces table and extracts the relevant data.

    Args:
        traces_table (Table): The table containing the traces data.

    Returns:
        dict: A dictionary containing the processed data.   
    """
    result = {
        "id": "",
        "question": "",
        "context": "",
        "answer": ""
    }

    column_names = traces_table.columns

    for trace_idx, trace_row in enumerate(traces_table.rows):
        row_dict = dict(zip(column_names, trace_row))

        event_type = row_dict.get('Message', '')
        content_str = row_dict.get('Properties', '')

        try:
            content_json = json.loads(content_str)
            gen_ai_content_str = content_json.get('gen_ai.event.content', '{}')
            gen_ai_content = json.loads(gen_ai_content_str)

            if event_type == "gen_ai.system.message" and 'content' in gen_ai_content:
                result["context"] = gen_ai_content['content']
            elif event_type == "gen_ai.user.message" and 'content' in gen_ai_content:
                result["question"] = gen_ai_content['content']
            elif event_type == "gen_ai.choice" and 'message' in gen_ai_content:
                result["answer"] = gen_ai_content['message']['content']

        except (json.JSONDecodeError, KeyError, TypeError) as e:
            logging.warning(f"Failed to parse JSON content in trace {trace_idx}: {e}")
            continue

    return result

def process_dependency(dependency_row, dependency_columns, timespan_days):
    """
    Processes a single dependency row from the App Insights data.

    Args:
        dependency_row (list): A list of values representing the dependency row.
        dependency_columns (list): A list of column names for the dependency data.
        timespan_days (int): The number of days to query for the data.

    Returns:
        dict: A dictionary containing the processed data.
    """
    dependency_id = ""
    try:
        dependency_dict = dict(zip(dependency_columns, dependency_row))
        dependency_id = dependency_dict.get("Id", "")
        logging.info(f"Processing dependency: {dependency_id}")

        # Get responses
        response_table = get_responses(dependency_id)
        if response_table is None or not response_table.rows:
            logging.warning(f"No response IDs found for dependency {dependency_id}.")
            return None

        # Extract response ID and operation ID
        response_row = response_table.rows[0]
        response_columns = response_table.columns
        response_dict = dict(zip(response_columns, response_row))
        operation_id = response_dict.get("Id", "")
        response_id = response_dict.get('Properties_gen_ai.response.id', "")
        logging.info(f"Response ID extracted: {response_id}")

        # Get traces
        traces_table = get_traces(operation_id, timespan_days)
        if traces_table is None or not traces_table.rows:
            logging.warning(f"No traces found for operation {operation_id}.")
            return None

        # Process traces
        result = process_traces(traces_table)
        result["id"] = response_id

        return result

    except Exception as e:
        if dependency_id:
            logging.error(f"Error processing dependency {dependency_id}: {e}")
        else:
            logging.error(f"Error processing dependency: {e}")
        return None



def extract_app_insights_data(timespan_days: int = 2, interaction_count: int = 5) -> List[Dict[str, Any]]:

    """
    Extracts data from Azure Application Insights for multiple interactions.

    Args:
        timespan_days (int, optional): Number of days for the query timespan. Defaults to 2.
        interaction_count (int, optional): Number of interactions to retrieve. Defaults to 5.

    Returns:
        List[Dict[str, Any]]: A list of dictionaries containing the extracted data.
    """
    try:
        dependencies_table = get_interactions(timespan_days, interaction_count)
        
        if dependencies_table is None:
            logging.error("No data returned from get_interactions")
            return []
        
        logging.info(f"Type of dependencies_table: {type(dependencies_table)}")
        
        if not hasattr(dependencies_table, 'columns'):
            logging.error(f"dependencies_table has no 'columns' attribute. Content: {dependencies_table}")
            return []

        if not hasattr(dependencies_table, 'rows'):
            logging.error(f"dependencies_table has no 'rows' attribute. Content: {dependencies_table}")
            return []

        if not dependencies_table.rows:
            logging.warning("No dependencies found in the initial query.")
            return []

        all_results = []
        dependency_columns = dependencies_table.columns  

        for idx, dependency_row in enumerate(dependencies_table.rows):
            result = process_dependency(dependency_row, dependency_columns, timespan_days)
            if result:
                all_results.append(result)

        return all_results
    
    except Exception as e:
        logging.error(f"Error during data extraction: {e}")
        return []


def load_prompt(prompt_name: str) -> str:
    """
    Loads the prompt text from a file.

    Args:
        prompt_name (str): The name of the prompt file (without extension).

    Returns:
        str: The prompt text.
    """
    prompt_path = os.path.join("prompts", f"{prompt_name}.txt")
    try:
        with open(prompt_path, 'r', encoding='utf-8') as file:
            prompt_text = file.read()
        return prompt_text
    except FileNotFoundError:
        print(f"Prompt file {prompt_path} not found.")
        return ""
    

def evaluation_run(timespan_days: int, interaction_count:int, groundedness_eval: bool = True, 
     coherence_eval: bool = True, relevance_eval: bool = True) -> str:
    
    """
    Extracts data from Azure Application Insights for multiple interactions.

    Args:
        timespan_days (int, optional): Number of days for the query timespan. Defaults to 2.
        interaction_count (int, optional): Number of interactions to retrieve. Defaults to 5.

    Returns:
        str: A JSON string containing a list of dictionaries with the evaluation results.
    """

    results = []  # Initialize a list to store results for all IDs

    try:
        app_insights_data = extract_app_insights_data(timespan_days, interaction_count)
        
        logging.info(f"Extracted {len(app_insights_data)} interactions from App Insights.")

        for idx, entry in enumerate(app_insights_data):
            logging.info(f"Processing entry {idx}")
            
            try:
                question = entry.get('question', '')
                context = entry.get('context', '')
                answer = entry.get('answer', '')
                eval_id = entry.get('id', 'N/A')
                result = {"gen_ai.response.id": eval_id}

                logging.info(f"Processing data for ID: {eval_id}")

                # Perform evaluations
                if groundedness_eval:
                    prompt = load_prompt("groundedness")
                    groundedness_result = evaluate_metric(question=question,
                                                        context=context,  
                                                        answer=answer,
                                                        client=eval_client,
                                                        model_deployment=eval_model_deployment,
                                                        prompt=prompt)
                    result["groundedness"] = groundedness_result
                    logging.info("Groundedness Evaluation:")
                    logging.info(groundedness_result)

                if coherence_eval:
                    prompt = load_prompt("coherence")
                    coherence_result = evaluate_metric( question=question,
                                                        context="", # no context provided for coherence eval
                                                        answer=answer,
                                                        client=eval_client,
                                                        model_deployment=eval_model_deployment,
                                                        prompt=prompt)
                    result["coherence"] = coherence_result      
                    logging.info("Coherence Evaluation:")
                    logging.info(coherence_result)

                if relevance_eval:
                    prompt = load_prompt("relevance")
                    relevance_result = evaluate_metric( question=question,
                                                        context=context,  
                                                        answer=answer,
                                                        client=eval_client,
                                                        model_deployment=eval_model_deployment,
                                                        prompt=prompt)
                    result["relevance"] = relevance_result
                    logging.info("Relevance Evaluation:")
                    logging.info(relevance_result)

                results.append(result)  # Add the result for this ID to the list
                logging.info(f"Completed processing for input ID: {eval_id}")
                logging.info("-" * 50)
            
            except Exception as e:
                logging.error(f"Error processing entry {idx}: {str(e)}")

    except Exception as e:
        logging.error(f"Error during full evaluation: {e}")
        raise

    return json.dumps(results)  # Return JSON string of all results


def upload_evals_to_appinsights(json_string: str):
    """
    Uploads the evaluation results to Azure Application Insights.

    Args:
        results (str): A JSON string containing a list of dictionaries with the evaluation results.
    """

    configure_azure_monitor()

    data = json.loads(json_string)
  
    for item in data:        
        extra = {'extra': item}
        logger.info("eval", **extra)
       
    

if __name__ == "__main__":

    groundedness_eval = True
    coherence_eval = True
    relevance_eval = True

    timespan_days =2 # number of days you want to select for queries
    interaction_count = 4# number of interactions you want to evaluate
    
    results = evaluation_run(timespan_days,interaction_count, 
    groundedness_eval, coherence_eval, relevance_eval)
    upload_evals_to_appinsights(results)

    

