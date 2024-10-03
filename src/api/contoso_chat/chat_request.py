import logging
from azure.identity import DefaultAzureCredential
import json
from opentelemetry import trace
from contoso_chat.models import FeedbackItem
from .product import product
import os
from azure.cosmos import CosmosClient
from dotenv import load_dotenv
from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import SystemMessage, UserMessage, AssistantMessage
from azure.core.credentials import AzureKeyCredential
from jinja2 import Template
from opentelemetry.sdk._logs import LoggerProvider, Logger, LogRecord
from opentelemetry._logs import set_logger_provider
from opentelemetry._events import set_event_logger_provider, EventLoggerProvider
from opentelemetry._events import Attributes, EventLoggerProvider, EventLogger, Event, get_event_logger_provider
from opentelemetry.sdk._logs.export import SimpleLogRecordProcessor, ConsoleLogExporter


load_dotenv()

tracer = trace.get_tracer(__name__)
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


def get_customer(customerId: str) -> str:
    try:
        url = os.environ["COSMOS_ENDPOINT"]
        client = CosmosClient(url=url, credential=DefaultAzureCredential())
        db = client.get_database_client("contoso-outdoor")
        container = db.get_container_client("customers")
        response = container.read_item(
            item=str(customerId), partition_key=str(customerId))
        response["orders"] = response["orders"][:2]
        return response
    except Exception as e:
        print(f"Error retrieving customer: {e}")
        return None


def get_response(customerId: str, question: str, chat_history: str) -> dict:

    endpoint = "{}openai/deployments/{}".format(
        os.environ['AZURE_OPENAI_ENDPOINT'], os.environ['AZURE_OPENAI_CHAT_DEPLOYMENT'])

    client = ChatCompletionsClient(
        endpoint=endpoint,
        credential=DefaultAzureCredential(
            exclude_interactive_browser_credential=False),
        credential_scopes=["https://cognitiveservices.azure.com/.default"],
        api_version="2023-03-15-preview",
        logging_enable=True,
    )

    customer = get_customer(customerId)
    context = product.find_products(question)

    # Get the base directory (the directory of the current file)
    base_dir = os.path.dirname(os.path.abspath(__file__))

    # Construct the full path to the file
    file_path = os.path.join(base_dir, 'chat.txt')

    # Open the file using the constructed path
    with open(file_path, 'r') as file:
        template_string = file.read()

    template = Template(template_string)
    template_input = {
        "question": question,
        "customer": customer,
        "documentation": context}

    rendered_template = template.render(template_input)

    try:
        with tracer.start_as_current_span("llm", attributes={"task": "get_response"}):
            messages = [SystemMessage(content=rendered_template)]
            for m in chat_history:
                try:
                    content = m['content']
                    role = m['role']
                    if role == 'user':
                        messages.append(UserMessage(content=content))
                    elif role == 'assistant':
                        messages.append(AssistantMessage(content=content))
                    else:
                        logger.warning(f"Unknown role for message: {role}")
                except Exception:
                    logger.warning("Unable to parse chat history messages")

            messages.append(UserMessage(content=question))

            response = client.complete(messages=messages)

        response_content = response.choices[0].message.content

        response_back = {"question": question,
                         "answer": response_content, "context": context}
        metadata = {"responseId": response.id,
                    "model": response.model, "usage": response.usage}

    except Exception as e:
        logger.error(f"Error getting response: {e}")
        raise e

    return response_back, metadata


def provide_feedback(feedback_item: FeedbackItem) -> dict:
    extra_info = validate_extra_feedback(feedback_item.extra)

    feedback_context = {"gen_ai.response.id": feedback_item.responseId,
                        "gen_ai.evaluation.score": feedback_item.feedback, "event.name": "gen_ai.evaluation.user_feedback", "extra": extra_info}
    logger.info("gen_ai.evaluation.user_feedback", extra=feedback_context)

    return {"result": "success"}


def validate_extra_feedback(extra: dict) -> str:
    if extra is None:
        return {}
    return json.dumps(extra)


if __name__ == "__main__":
    get_response(4, "What hiking jackets would you recommend?", [])
    # get_response(argv[1], argv[2], argv[3])
