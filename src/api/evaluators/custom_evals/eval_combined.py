import json
import os
from datetime import timedelta
from typing import Any, Dict, List
from azure.core.exceptions import HttpResponseError
from azure.identity import DefaultAzureCredential
from azure.monitor.query import LogsQueryClient, LogsQueryStatus
from dotenv import load_dotenv
import prompty
import prompty.azure
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


# Load environment variables
load_dotenv()



# Configuration for the Azure OpenAI endpoint
model_config = {
    "azure_endpoint": os.environ["AZURE_OPENAI_ENDPOINT"],
    "api_version": os.environ["AZURE_OPENAI_API_VERSION"],
}


# Authenticate using DefaultAzureCredential
credential = DefaultAzureCredential()
logs_client = LogsQueryClient(credential)
workspace_id= os.environ["APPINSIGHTS_WORKSPACE_ID"]


def extract_app_insights_data( timespan_days: int = 2, take_count: int = 5) -> List[Dict[str, Any]]:
    """
    Extracts data from Azure Application Insights for multiple interactions.

    Args:
        workspace_id (str): The workspace ID to query.
        timespan_days (int, optional): Number of days for the query timespan. Defaults to 2.
        take_count (int, optional): Number of interactions to retrieve. Defaults to 5.

    Returns:
        List[Dict[str, Any]]: A list of dictionaries containing the extracted data.
    """
    try:
        # Authenticate using DefaultAzureCredential
        credential = DefaultAzureCredential()
        client = LogsQueryClient(credential)

        # Define the query to get the last 'take_count' interactions
        query_dependencies = f"""
        AppDependencies
        | where Properties["task"] == "get_response"
        | order by TimeGenerated desc
        | take {take_count}
        | project OperationId, Id
        """

        response = client.query_workspace(workspace_id, query_dependencies, timespan=timedelta(days=timespan_days))
        if response.status != LogsQueryStatus.SUCCESS:
            error = response.partial_error
            logging.error(f"Initial query failed: {error}")
            return []

        dependencies_table = response.tables[0]
        if not dependencies_table.rows:
            logging.warning("No dependencies found in the initial query.")
            return []

        all_results = []

        for idx, dependency_row in enumerate(dependencies_table.rows):
            dependency_id = None  # Initialize dependency_id for error handling
            try:
                # Extract dependency information
                # Corrected line: Use columns directly as they are already strings
                dependency_dict = dict(zip(dependencies_table.columns, dependency_row))
                dependency_id = dependency_dict.get("Id", "")
                logging.info(f"Processing dependency {idx + 1}/{len(dependencies_table.rows)}: {dependency_id}")

                # Query to get the response IDs
                query_response_ids = f"""
                AppDependencies
                | where ParentId == "{dependency_id}"
                | project OperationId, Id, Properties["gen_ai.response.id"]
                """

                response2 = client.query_workspace(workspace_id, query_response_ids, timespan=timedelta(days=timespan_days))
                if response2.status != LogsQueryStatus.SUCCESS:
                    error = response2.partial_error
                    logging.error(f"Query for response IDs failed for dependency {dependency_id}: {error}")
                    continue

                response_table = response2.tables[0]
                if not response_table.rows:
                    logging.warning(f"No response IDs found for dependency {dependency_id}.")
                    continue

                response_id_row = response_table.rows[0]
                # Corrected line
                response_id_dict = dict(zip(response_table.columns, response_id_row))
                operation_id = response_id_dict.get("Id", "")
                response_id = response_id_dict.get("Properties_gen_ai.response.id", "")
                logging.info(f"Response ID extracted: {response_id}")

                # Query to get the traces
                query_traces = f"""
                AppTraces
                | where ParentId == "{operation_id}"
                """

                response3 = client.query_workspace(workspace_id, query_traces, timespan=timedelta(days=timespan_days))
                if response3.status != LogsQueryStatus.SUCCESS:
                    error = response3.partial_error
                    logging.error(f"Query for traces failed for operation {operation_id}: {error}")
                    continue

                traces_table = response3.tables[0]
                if not traces_table.rows:
                    logging.warning(f"No traces found for operation {operation_id}.")
                    continue

                result: Dict[str, Any] = {
                    "id": response_id,
                    "question": "",
                    "context": "",
                    "answer": ""
                }

                column_names = traces_table.columns  # Use columns directly

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
                        logging.warning(f"Failed to parse JSON content in trace {trace_idx} for operation {operation_id}: {e}")
                        continue

                all_results.append(result)

            except Exception as e:
                if dependency_id:
                    logging.error(f"Error processing dependency {dependency_id}: {e}")
                else:
                    logging.error(f"Error processing dependency at index {idx}: {e}")
                continue

        return all_results

    except Exception as e:
        logging.error(f"Error during data extraction: {e}")
        return []






def evaluate(prompt_name: str, inputs: Dict[str, Any]) -> str:
    """
    Executes a prompty evaluation.

    Args:
        prompt_name (str): The name of the prompt to execute.
        inputs (Dict[str, Any]): The input parameters for the prompt.

    Returns:
        str: The result of the prompty execution.
    """
    try:
        result = prompty.execute(
            prompt_name,
            inputs=inputs,
            configuration=model_config
        )
        return result
    except Exception as e:
        logging.error(f"Error during {prompt_name} evaluation: {e}")
        return ""

def groundedness_evaluation(question: str, context: str, answer: str) -> str:
    """
    Evaluates the groundedness of the answer.

    Args:
        question (str): The user's question.
        context (str): The context provided.
        answer (str): The generated answer.

    Returns:
        str: The groundedness evaluation result.
    """
    return evaluate("groundedness.prompty", {
        "question": question,
        "context": context,
        "answer": answer
    })

def coherence_evaluation(question: str, context: str, answer: str) -> str:
    """
    Evaluates the coherence of the answer.

    Args:
        question (str): The user's question.
        context (str): The context provided.
        answer (str): The generated answer.

    Returns:
        str: The coherence evaluation result.
    """
    return evaluate("coherence.prompty", {
        "question": question,
        "context": context,
        "answer": answer
    })

def relevance_evaluation(question: str, context: str, answer: str) -> str:
    """
    Evaluates the relevance of the answer.

    Args:
        question (str): The user's question.
        context (str): The context provided.
        answer (str): The generated answer.

    Returns:
        str: The relevance evaluation result.
    """
    return evaluate("relevance.prompty", {
        "question": question,
        "context": context,
        "answer": answer
    })



def evaluation_run(timespan_days: int, take_count:int, groundedness_eval: bool = True, 
     coherence_eval: bool = True, relevance_eval: bool = True) -> str:
    
    """
    Extracts data from Azure Application Insights for multiple interactions.

    Args:
        timespan_days (int, optional): Number of days for the query timespan. Defaults to 2.
        take_count (int, optional): Number of interactions to retrieve. Defaults to 5.

    Returns:
        str: A JSON string containing a list of dictionaries with the evaluation results.
    """

    results = []  # Initialize a list to store results for all IDs

    try:
        app_insights_data = extract_app_insights_data(timespan_days, take_count)
        
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
                    groundedness_result = groundedness_evaluation(question, context, answer)
                    result["groundedness_result"] = groundedness_result
                    logging.info("Groundedness Evaluation:")
                    logging.info(groundedness_result)

                if coherence_eval:
                    coherence_result = coherence_evaluation(question, context, answer)
                    result["coherence_result"] = coherence_result
                    logging.info("Coherence Evaluation:")
                    logging.info(coherence_result)

                if relevance_eval:
                    relevance_result = relevance_evaluation(question, context, answer)
                    result["relevance_result"] = relevance_result
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


if __name__ == "__main__":

    groundedness_eval = True
    coherence_eval = True
    relevance_eval = True

    timespan_days =2 # number of days you want to select for queries
    take_count =5 # number of interactions you want to evaluate
    
    results = evaluation_run(timespan_days,take_count, 
    groundedness_eval, coherence_eval, relevance_eval)

    print(results)

