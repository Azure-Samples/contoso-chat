import logging
from azure.identity import DefaultAzureCredential
import os
from sys import argv
from azure.cosmos import CosmosClient
from dotenv import load_dotenv
from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import SystemMessage, UserMessage
from azure.core.credentials import AzureKeyCredential
from jinja2 import Template
from opentelemetry import trace

from .product import product


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

    endpoint = os.environ["AZUREAI_ENDPOINT_URL"]
    key = os.environ["AZUREAI_ENDPOINT_KEY"]

    client = ChatCompletionsClient(
        endpoint=endpoint,
        credential=AzureKeyCredential(""),  # Pass in an empty value.
        headers={"api-key": key},
        api_version="2023-03-15-preview",
        logging_enable=True,
    )
    
    logger.info("getting customer...")
    customer = get_customer(customerId)
    logger.info("customer complete")
    context = product.find_products(question)
    logger.info(context)
    logger.info("products complete")
    logger.info("getting result...")

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
            response = client.complete(
                messages=[
                    SystemMessage(content=rendered_template),
                    UserMessage(content=question),
                ]
            )

        response_content = response.choices[0].message.content

        response_back = {"question": question, "answer": response_content, "context": context}
        metadata = {"responseId": response.id, "model": response.model, "usage": response.usage}

    except Exception as e:
        logger.error(f"Error getting response: {e}")

    return response_back, metadata

def provide_feedback(responseId: str, feedback: int, extra: any) -> dict:
    feedback = {"responseId": responseId, "feedback": feedback, "extra": extra}
    logger.info("Feedback Provided", extra=feedback)
    return feedback

if __name__ == "__main__":
    get_response(4, "What hiking jackets would you recommend?", [])
    # get_response(argv[1], argv[2], argv[3])
