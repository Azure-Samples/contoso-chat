from dotenv import load_dotenv
load_dotenv()

from azure.cosmos import CosmosClient
from sys import argv
import os
import pathlib
from ai_search import retrieve_documentation
from azure.identity import DefaultAzureCredential
from promptflow.tools.common import init_azure_openai_client
from promptflow.connections import AzureOpenAIConnection
from promptflow.core import (AzureOpenAIModelConfiguration, Prompty, tool)

def get_customer(customerId: str) -> str:
    try:
        url = os.environ["COSMOS_ENDPOINT"]
        client = CosmosClient(url=url, credential=DefaultAzureCredential())
        db = client.get_database_client("contoso-outdoor")
        container = db.get_container_client("customers")
        response = container.read_item(item=str(customerId), partition_key=str(customerId))
        response["orders"] = response["orders"][:2]
        return response
    except Exception as e:
        print(f"Error retrieving customer: {e}")
        return None

def get_product(productId: str) -> str:
    try:
        url = os.environ["COSMOS_ENDPOINT"]
        client = CosmosClient(url=url, credential=DefaultAzureCredential())
        db = client.get_database_client("contoso-outdoor")
        container = db.get_container_client("products")
        response = container.read_item(item=str(productId), partition_key=str(productId))
        return response
    except Exception as e:
        print(f"Error retrieving product: {e}")
        return None

def get_context(question, embedding):
    return retrieve_documentation(question=question, index_name="contoso-products", embedding=embedding)


def get_embedding(question: str):
    connection = AzureOpenAIConnection(        
                    #azure_deployment=os.environ["AZURE_EMBEDDING_NAME"],
                    azure_deployment="text-embedding-ada-002",
                    api_version=os.environ["AZURE_OPENAI_API_VERSION"],
                    api_base=os.environ["AZURE_OPENAI_ENDPOINT"]
                    )
                
    client = init_azure_openai_client(connection)

    return client.embeddings.create(
            input=question,
            #model=os.environ["AZURE_EMBEDDING_NAME"]
            model="text-embedding-ada-002",
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
        #azure_deployment=os.environ["AZURE_DEPLOYMENT_NAME"],
        azure_deployment="gpt-35-turbo",
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