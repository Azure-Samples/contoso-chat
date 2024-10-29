import os
import json
from typing import Dict, List
from azure.identity import DefaultAzureCredential
from dotenv import load_dotenv
from pathlib import Path
from azure.search.documents import SearchClient
from azure.search.documents.models import (
    VectorizedQuery,
    QueryType,
    QueryCaptionType,
    QueryAnswerType,
)
from azure.ai.inference import ChatCompletionsClient, EmbeddingsClient
from azure.ai.inference.models import SystemMessage, UserMessage
from jinja2 import Template
from opentelemetry import trace

load_dotenv()

tracer = trace.get_tracer(__name__)


def generate_embeddings(queries: List[str]) -> str:
    endpoint = "{}openai/deployments/{}".format(
        os.environ['AZURE_OPENAI_ENDPOINT'], os.environ['AZURE_EMBEDDING_NAME'])

    client = EmbeddingsClient(
        endpoint=endpoint,
        credential=DefaultAzureCredential(
            exclude_interactive_browser_credential=False),
        credential_scopes=["https://cognitiveservices.azure.com/.default"],
        api_version="2023-05-15",
        logging_enable=True,
    )
    response = client.embed(input=queries)
    embs = [emb.embedding for emb in response.data]
    items = [{"item": queries[i], "embedding": embs[i]}
             for i in range(len(queries))]

    return items


def retrieve_products(items: List[Dict[str, any]], index_name: str) -> str:
    search_client = SearchClient(
        endpoint=os.environ["AZURE_SEARCH_ENDPOINT"],
        index_name=index_name,
        credential=DefaultAzureCredential(),
    )

    products = []
    for item in items:
        vector_query = VectorizedQuery(
            vector=item["embedding"], k_nearest_neighbors=3, fields="contentVector"
        )
        results = search_client.search(
            search_text=item["item"],
            vector_queries=[vector_query],
            query_type=QueryType.SEMANTIC,
            semantic_configuration_name="default",
            query_caption=QueryCaptionType.EXTRACTIVE,
            query_answer=QueryAnswerType.EXTRACTIVE,
            top=2,
        )

        docs = [
            {
                "id": doc["id"],
                "title": doc["title"],
                "content": doc["content"],
                "url": doc["url"],
            }
            for doc in results
        ]

        # Remove duplicates
        products.extend([i for i in docs if i["id"] not in [
                        x["id"] for x in products]])

    return products


def find_products(context: str) -> Dict[str, any]:
    # Get product queries
    print("context:", context)

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

    # Get the base directory (the directory of the current file)
    base_dir = os.path.dirname(os.path.abspath(__file__))

    # Construct the full path to the file
    file_path = os.path.join(base_dir, 'product.txt')

    # Open the file using the constructed path
    with open(file_path, 'r') as file:
        template_string = file.read()

    # Step 3: Create a Jinja template object
    template = Template(template_string)
    template_input = {
        "context": context
    }

    rendered_template = template.render(template_input)

    try:
        with tracer.start_as_current_span("llm", attributes={"task": "find_products"}):
            response = client.complete(
                messages=[
                    SystemMessage(content=rendered_template),
                    UserMessage(content=context),
                ]
            )

            queries = response.choices[0].message.content

    except Exception as e:
        print(f"Error getting response: {e}")

    print("queries:", queries)
    qs = json.loads(queries)
    # Generate embeddings
    items = generate_embeddings(qs)
    # Retrieve products
    products = retrieve_products(items, "contoso-products")
    return products


if __name__ == "__main__":
    context = "Can you use a selection of tents and backpacks as context?"
    answer = find_products(context)
    print(json.dumps(answer, indent=2))
