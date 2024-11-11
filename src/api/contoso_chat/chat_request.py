import logging
from azure.identity import DefaultAzureCredential
import json
from opentelemetry import trace
from contoso_chat.models import FeedbackItem
from contoso_chat.product import product
import os
from azure.cosmos import CosmosClient

from sys import argv
import prompty
import prompty.azure
from prompty.tracer import trace, Tracer, console_tracer, PromptyTracer
from dotenv import load_dotenv
load_dotenv()

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


@trace
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

@trace
def get_response(customerId: str, question: str, chat_history: list) -> dict:

    print("getting customer...")
    customer = get_customer(customerId)
    print("customer complete")
    context = product.find_products(question)
    print("products complete")
    print("getting result...")

    model_config = {
        "azure_endpoint": os.environ["AZURE_OPENAI_ENDPOINT"],
        "api_version": os.environ["AZURE_OPENAI_API_VERSION"],
    }

    try:
        response = prompty.execute(
            "chat.prompty",
            inputs={"question": question, "customer": customer, "documentation": context, "history": chat_history},
            configuration=model_config,
            raw=True,
        )

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
    #get_response(argv[1], argv[2], argv[3])
