from typing import List
from promptflow import tool
from azure.search.documents import SearchClient
from azure.search.documents.models import VectorizedQuery, QueryType, QueryCaptionType, QueryAnswerType
from azure.core.credentials import AzureKeyCredential
from promptflow.connections import CognitiveSearchConnection

@tool
def retrieve_documentation(question: str, index_name: str, embedding: List[float], search: CognitiveSearchConnection) -> str:

  # Semantic Hybrid Search
  query = question

  search_client = SearchClient(endpoint=search.api_base, 
                              index_name=index_name, 
                              credential=AzureKeyCredential(search.api_key))

  vector_query = VectorizedQuery(vector=embedding, 
                                 k_nearest_neighbors=3, 
                                 fields="contentVector")

  results = search_client.search(  
      search_text=query,  
      vector_queries=[vector_query],
      query_type=QueryType.SEMANTIC, 
      semantic_configuration_name='azureml-default', 
      query_caption=QueryCaptionType.EXTRACTIVE, 
      query_answer=QueryAnswerType.EXTRACTIVE,
      top=6
  )

  docs = [{"id": doc["id"],  "content": doc["content"]}
          for doc in results]
  
  return docs