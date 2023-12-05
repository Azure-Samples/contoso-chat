from typing import List
from promptflow import tool
from azure.search.documents import SearchClient
from azure.search.documents.models import Vector
from azure.core.credentials import AzureKeyCredential
from promptflow.connections import CognitiveSearchConnection


@tool
def retrieve_documentation(
    question: str,
    index_name: str,
    embedding: List[float],
    search: CognitiveSearchConnection,
) -> str:
    search_client = SearchClient(
        endpoint=search.api_base,
        index_name=index_name,
        credential=AzureKeyCredential(search.api_key),
    )

    vector = Vector(value=embedding, k=2, fields="embedding")

    results = search_client.search(
        search_text=question,
        top=2,
        search_fields=["content"],
        vectors=[vector],
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

    return docs
