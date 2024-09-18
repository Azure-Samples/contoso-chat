import json
import os
from datetime import timedelta
from typing import Any, Dict
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


def app_insights_data_extraction(k: int = 0) -> str:
    """
    Extracts data from Azure Application Insights.

    Args:
        k (int): The index of the row to process.

    Returns:
        str: A JSON string containing the extracted id, question, context, and answer.
    """
    query_dependencies = """
    AppDependencies
    | where Properties["task"] == "get_response"
    | project OperationId, Id
    """

    try:
        response = logs_client.query_workspace(workspace_id, query_dependencies, timespan=timedelta(days=1))
        if response.status != LogsQueryStatus.SUCCESS:
            raise HttpResponseError(f"Query failed with status: {response.status}")
        
        dependencies_table = response.tables[0]
        if k >= len(dependencies_table.rows):
            raise IndexError(f"Index {k} out of range for dependencies data.")

        # Convert the specific row to a dictionary
        dependency_row = dependencies_table.rows[k]
        dependency_dict = dict(zip(dependencies_table.columns, dependency_row))
        dependency_id = dependency_dict["Id"]

        logging.info(f"Dependency ID extracted: {dependency_id}")

        query_response_ids = f"""
        AppDependencies
        | where ParentId == "{dependency_id}"
        | project OperationId, Id, Properties["gen_ai.response.id"]
        """

        response2 = logs_client.query_workspace(workspace_id, query_response_ids, timespan=timedelta(days=1))
        if response2.status != LogsQueryStatus.SUCCESS:
            raise HttpResponseError(f"Second query failed with status: {response2.status}")

        response_table = response2.tables[0]
        if not response_table.rows:
            raise ValueError("No data returned for the second query.")

        # Convert the first row to a dictionary
        response_id_row = response_table.rows[0]
        response_id_dict = dict(zip(response_table.columns, response_id_row))
        operation_id = response_id_dict["Id"]
        response_id = response_id_dict.get("Properties_gen_ai.response.id", "")

        logging.info(f"Response ID extracted: {response_id}")

        query_traces = f"""
        AppTraces
        | where ParentId == "{operation_id}"
        """

        response3 = logs_client.query_workspace(workspace_id, query_traces, timespan=timedelta(days=1))
        if response3.status != LogsQueryStatus.SUCCESS:
            raise HttpResponseError(f"Third query failed with status: {response3.status}")

        traces_table = response3.tables[0]
        if not traces_table.rows:
            raise ValueError("No data returned for the third query.")

        result: Dict[str, Any] = {
            "id": response_id,
            "question": "",
            "context": "",
            "answer": ""
        }

        for idx, row in enumerate(traces_table.rows):
            # Convert LogsTableRow to a dictionary
            row_dict = dict(zip(traces_table.columns, row))
            logging.debug(f"Processing row {idx}: {row_dict}")

            event_type = row_dict.get('Message', '')
            properties = row_dict.get('Properties', '')

            try:
                content_json = json.loads(properties)
                gen_ai_content = json.loads(content_json.get('gen_ai.event.content', '{}'))
            except (json.JSONDecodeError, KeyError, TypeError) as e:
                logging.warning(f"Failed to parse JSON content in row {idx}: {e}")
                continue

            if event_type == "gen_ai.system.message":
                result["context"] = gen_ai_content.get('content', '')
            elif event_type == "gen_ai.user.message":
                result["question"] = gen_ai_content.get('content', '')
            elif event_type == "gen_ai.choice":
                result["answer"] = gen_ai_content.get('message', {}).get('content', '')

        json_result = json.dumps(result, indent=2)
        logging.debug(f"Extracted Data: {json_result}")
        return json_result

    except Exception as e:
        logging.error(f"Error during data extraction: {e}")
        raise






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



def evaluation_run(k: int, groundedness_eval: bool = True, coherence_eval: bool = True, relevance_eval: bool = True) -> None:
    """
    Performs an evaluation run by extracting data and running all evaluations mentioned.

    Args:
        k (int): The index of the data row to evaluate.
        groundedness_eval (bool): Whether to perform groundedness evaluation.
        coherence_eval (bool): Whether to perform coherence evaluation.
        relevance_eval (bool): Whether to perform relevance evaluation.
    """
    try:
        app_insights_data = app_insights_data_extraction(k)
        logging.info(f"App Insights Data: {app_insights_data}")

        args = json.loads(app_insights_data)
        question = args.get('question', '')
        context = args.get('context', '')
        answer = args.get('answer', '')
        eval_id = args.get('id', 'N/A')

        # Perform evaluations
        if groundedness_eval:
            groundedness_result = groundedness_evaluation(question, context, answer)
            logging.info("Groundedness Evaluation:")
            logging.info(groundedness_result)

        if coherence_eval:
            coherence_result = coherence_evaluation(question, context, answer)
            logging.info("\nCoherence Evaluation:")
            logging.info(coherence_result)

        if relevance_eval:
            relevance_result = relevance_evaluation(question, context, answer)
            logging.info("\nRelevance Evaluation:")
            logging.info(relevance_result)

        logging.info(f"Results for input ID: {eval_id}")
        logging.info("-" * 50)

    except Exception as e:
        logging.error(f"Error during full evaluation: {e}")
        raise

if __name__ == "__main__":
    groundedness_eval = False
    coherence_eval = True
    relevance_eval = True
    
    evaluation_run(0, groundedness_eval, coherence_eval, relevance_eval)

