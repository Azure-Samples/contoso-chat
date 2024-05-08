from dotenv import load_dotenv
load_dotenv()

from azure.cosmos import CosmosClient
from sys import argv
import os
import pathlib
from ai_search import retrieve_documentation
from promptflow.tools.common import init_azure_openai_client
from promptflow.connections import AzureOpenAIConnection
from promptflow.core import (AzureOpenAIModelConfiguration, Prompty, tool)

def get_customer(customerId: str) -> str:
    url = os.environ["COSMOS_ENDPOINT"]
    credential = os.environ["COSMOS_KEY"]
    client = CosmosClient(url=url, credential=credential)
    db = client.get_database_client("contoso-outdoor")
    container = db.get_container_client("customers")
    response = container.read_item(item=str(customerId), partition_key=str(customerId))
    response["orders"] = response["orders"][:2]
    return response


def get_context(question, embedding):
    return retrieve_documentation(question=question, index_name="contoso-products", embedding=embedding)


def get_embedding(question: str):
    connection = AzureOpenAIConnection(        
                    azure_deployment=os.environ["AZURE_EMBEDDING_NAME"],
                    api_key=os.environ["AZURE_OPENAI_API_KEY"],
                    api_version=os.environ["AZURE_OPENAI_API_VERSION"],
                    api_base=os.environ["AZURE_OPENAI_ENDPOINT"]
                    )
                
    client = init_azure_openai_client(connection)

    return client.embeddings.create(
            input=question,
            model=os.environ["AZURE_EMBEDDING_NAME"]
        ).data[0].embedding
@tool
def get_response(customerId, question, chat_history):
    print("inputs:", customerId, question)
    customer = get_customer(customerId)
    embedding = get_embedding(question)
    context = get_context(question, embedding)
    print("context:", context)
    print("getting result...")

    configuration = AzureOpenAIModelConfiguration(
        azure_deployment=os.environ["AZURE_DEPLOYMENT_NAME"],
        api_key=os.environ["AZURE_OPENAI_API_KEY"],
        api_version=os.environ["AZURE_OPENAI_API_VERSION"],
        azure_endpoint=os.environ["AZURE_OPENAI_ENDPOINT"]
    )
    override_model = {
        "configuration": configuration,
        "parameters": {"max_tokens": 512}
    }
    # get cwd
    data_path = os.path.join(pathlib.Path(__file__).parent.resolve(), "./chat.prompty")
    prompty_obj = Prompty.load(data_path, model=override_model)

    result = prompty_obj(question = question, customer = customer, documentation = context)

    print("result: ", result)

    return {"answer": result, "context": context}

# if __name__ == "__main__":
#     get_response(4, "What hiking jackets would you recommend?", [])
#     #get_response(argv[1], argv[2], argv[3])