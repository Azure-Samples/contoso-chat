from dotenv import load_dotenv
from azure.cosmos import CosmosClient
from sys import argv
import os
from ai_search import retrieve_documentation
from evaluations import coherence, relevance, groundedness, fluency
from promptflow.core import (AzureOpenAIModelConfiguration,
                             OpenAIModelConfiguration, Prompty)
load_dotenv()


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

    embedding = Prompty(model={"azure_deployment": "text-embedding-ada-002", "type": "azure"},
                        api="embedding",
                        content=question)
    return embedding


def get_response(customerId, question, chat_history):
    print("inputs:", customerId, question)
    customer = get_customer(customerId)
    embedding = get_embedding(question)
    context = get_context(question, embedding)
    prompt = "chat.prompty"
    print("getting result...")
    #prompt.inputs["question"] = "what is the price of the RainGuard Hiking Jacket?"
    result = prompty.execute(
        prompt,
        #model={"azure_endpoint": endpoint, "api_key": key},
        inputs={"question": question, "customer": customer, "documentation": context},
    )
    score = {}
    score["groundedness"] = groundedness.evaluate(question, context, result)
    score["coherence"] = coherence.evaluate(question, context, result)
    score["relevance"] = relevance.evaluate(question, context, result)
    score["fluency"] = fluency.evaluate(question, context, result)

    print("result: ", result)
    print("score: ", score)
    return {"question": question, "answer": result, "context": context}


if __name__ == "__main__":
    get_response(4, "What hiking jackets would you recommend?", [])
    #get_response(argv[1], argv[2], argv[3])