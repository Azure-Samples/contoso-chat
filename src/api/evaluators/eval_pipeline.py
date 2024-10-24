import json
import os
from datetime import timedelta
from typing import Any, Dict, List
from azure.identity import DefaultAzureCredential
from azure.monitor.query import LogsQueryClient, LogsQueryStatus
from azure.ai.evaluation import RelevanceEvaluator, GroundednessEvaluator, CoherenceEvaluator
from dotenv import load_dotenv
import logging
from opentelemetry._logs import set_logger_provider
from opentelemetry.sdk._logs import LoggerProvider, LoggingHandler
from azure.monitor.opentelemetry.exporter import AzureMonitorLogExporter
from opentelemetry.sdk.resources import SERVICE_NAME, Resource
from opentelemetry.sdk._logs.export import BatchLogRecordProcessor
from opentelemetry.sdk._logs import (
    LoggerProvider,
    LoggingHandler,
)
from opentelemetry._events import Event

# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

credential = DefaultAzureCredential()
logs_client = LogsQueryClient(credential)
workspace_id = os.environ["APPINSIGHTS_WORKSPACE_ID"]


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
        logging.info(
            f"Query executed successfully. Result type: {type(response.tables[0])}")
        return response.tables[0]
    except Exception as e:
        logging.error(f"Error in execute_query: {e}")
        return None


def get_genaispans(timespan_days, interaction_count):
    query = f"""
    AppDependencies
    | where isnotnull(Properties["gen_ai.system"]) and Properties["gen_ai.response.model"] == "gpt-35-turbo"
    | order by TimeGenerated desc
    | take {interaction_count}
    | project OperationId, Id, Properties["gen_ai.response.id"]
    """
    return execute_query(query, timespan_days)


def get_tokenlogs(operation_id, timespan_days):
    query = f"""
    AppTraces
    | where ParentId == "{operation_id}" and Message in ("gen_ai.choice", "gen_ai.user.message", "gen_ai.system.message")
    """
    return execute_query(query, timespan_days)


def process_tokenlogs(traces_table):
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
            logging.warning(
                f"Failed to parse JSON content in trace {trace_idx}: {e}")
            continue

    return result


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
        dependencies_table = get_genaispans(timespan_days, interaction_count)

        if dependencies_table is None:
            logging.error("No data returned from get_interactions")
            return []

        logging.info(f"Type of dependencies_table: {type(dependencies_table)}")

        if not hasattr(dependencies_table, 'columns'):
            logging.error(
                f"dependencies_table has no 'columns' attribute. Content: {dependencies_table}")
            return []

        if not hasattr(dependencies_table, 'rows'):
            logging.error(
                f"dependencies_table has no 'rows' attribute. Content: {dependencies_table}")
            return []

        if not dependencies_table.rows:
            logging.warning("No dependencies found in the initial query.")
            return []

        all_results = []
        dependency_columns = dependencies_table.columns

        # Extract response ID and operation ID
        for idx, dependency_row in enumerate(dependencies_table.rows):
            response_dict = dict(zip(dependency_columns, dependency_row))
            operation_id = response_dict.get("Id", "")
            response_id = response_dict.get(
                'Properties_gen_ai.response.id', "")
            logging.info(f"Response ID extracted: {response_id}")

            # Get traces
            traces_table = get_tokenlogs(operation_id, timespan_days)
            if traces_table is None or not traces_table.rows:
                logging.warning(
                    f"No traces found for operation {operation_id}.")
                return None

            # Process traces
            result = process_tokenlogs(traces_table)
            result["id"] = response_id
            if result:
                all_results.append(result)

        return all_results

    except Exception as e:
        logging.error(f"Error during data extraction: {e}")
        return []


def evaluation_run(timespan_days: int, interaction_count: int, groundedness_eval: bool = True,
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
        app_insights_data = extract_app_insights_data(
            timespan_days, interaction_count)

        logging.info(
            f"Extracted {len(app_insights_data)} interactions from App Insights.")

        model_config = {
            "azure_endpoint": os.environ.get("AZURE_OPENAI_ENDPOINT"),
            "api_key": os.environ.get("AZURE_OPENAI_API_KEY"),
            "azure_deployment": os.environ.get("AZURE_OPENAI_DEPLOYMENT"),
            "api_version": os.environ.get("AZURE_OPENAI_API_VERSION"),
        }

        # Initialzing Relevance Evaluator
        relevance_eval = RelevanceEvaluator(model_config)
        groundedness_eval = GroundednessEvaluator(model_config)
        coherence_eval = CoherenceEvaluator(model_config)

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
                    groundedness_score = groundedness_eval(
                        response=answer,
                        context=context,)
                    result["gen_ai.evaluation.groundedness"] = groundedness_score["gpt_groundedness"]

                if coherence_eval:
                    coherence_score = coherence_eval(
                        response=answer,
                        query=question,)
                    result["gen_ai.evaluation.coherence"] = coherence_score["gpt_coherence"]

                if relevance_eval:
                    relevance_score = relevance_eval(
                        response=answer,
                        context=context,
                        query=question,)
                    result["gen_ai.evaluation.relevance"] = relevance_score["gpt_relevance"]

                results.append(result)

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

    data = json.loads(json_string)

    for score in data:
        response_id = score["gen_ai.response.id"]
        for eval_type in ["groundedness", "coherence", "relevance"]:
            eval_score = score.get(f"gen_ai.evaluation.{eval_type}")
            if eval_score:
                eval = {
                    "gen_ai.response.id": response_id,
                    "gen_ai.evaluation.score": eval_score,
                    "event.name": f"gen_ai.evaluation.{eval_type}",
                }
                logger.info(f"gen_ai.evaluation.{eval_type}", extra=eval)


if __name__ == "__main__":

    # Configure OpenTelemetry logging
    OTEL_SERVICE_NAME = os.getenv("OTEL_SERVICE_NAME", "contoso-eval-pipeline")
    resource = Resource(attributes={SERVICE_NAME: OTEL_SERVICE_NAME
                                    })
    logger_provider = LoggerProvider(resource=resource)
    set_logger_provider(logger_provider)
    exporter = AzureMonitorLogExporter.from_connection_string(
        os.getenv("APPINSIGHTS_CONNECTIONSTRING"))
    logger_provider.add_log_record_processor(
        BatchLogRecordProcessor(exporter, schedule_delay_millis=60000))
    handler = LoggingHandler(level=logging.NOTSET,
                             logger_provider=logger_provider)
    logging.getLogger().addHandler(handler)

    groundedness_eval = True
    coherence_eval = True
    relevance_eval = True
    timespan_days = 2  # number of days you want to select for queries
    interaction_count = 4  # number of interactions you want to evaluate

    # Run evaluation pipeline
    results = evaluation_run(timespan_days, interaction_count,
                             groundedness_eval, coherence_eval, relevance_eval)

    # Upload evaluation results to Azure Application Insights
    upload_evals_to_appinsights(results)
