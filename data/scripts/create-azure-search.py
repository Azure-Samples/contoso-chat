#!/usr/bin/env python
# coding: utf-8

# # Generating your product search index
# Thereis notebook is designed to automatically create the product search index for you. It uses the [product catalog](products.csv) file to create the index. In order to do so it needs names ane keys for the following services:
# 
# - Azure Search Service
# - Azure OpenAI Service
# 
# You can find the names and keys in the Azure Portal. These need to be entered in a `.env` file in the root of this repository. The `.env` file is not checked in to source control. You can use the [`.env.sample`](../../.env.sample) file as a template.

# In[1]:


import os
import pandas as pd
from azure.identity import DefaultAzureCredential
from azure.identity import DefaultAzureCredential, get_bearer_token_provider
from azure.search.documents import SearchClient
from azure.search.documents.indexes import SearchIndexClient
from azure.search.documents.indexes.models import (
    HnswParameters,
    HnswAlgorithmConfiguration,
    SemanticPrioritizedFields,
    SearchableField,
    SearchField,
    SearchFieldDataType,
    SearchIndex,
    SemanticSearch,
    SemanticConfiguration,
    SemanticField,
    SimpleField,
    VectorSearch,
    VectorSearchAlgorithmKind,
    VectorSearchAlgorithmMetric,
    ExhaustiveKnnAlgorithmConfiguration,
    ExhaustiveKnnParameters,
    VectorSearchProfile,
)
from typing import List, Dict
from openai import AzureOpenAI
from dotenv import load_dotenv

from pathlib import Path

load_dotenv()


# In[2]:


def delete_index(search_index_client: SearchIndexClient, search_index: str):
    print(f"deleting index {search_index}")
    search_index_client.delete_index(search_index)


# In[3]:


def create_index_definition(name: str) -> SearchIndex:
    """
    Returns an Azure Cognitive Search index with the given name.
    """
    # The fields we want to index. The "embedding" field is a vector field that will
    # be used for vector search.
    fields = [
        SimpleField(name="id", type=SearchFieldDataType.String, key=True),
        SearchableField(name="content", type=SearchFieldDataType.String),
        SimpleField(name="filepath", type=SearchFieldDataType.String),
        SearchableField(name="title", type=SearchFieldDataType.String),
        SimpleField(name="url", type=SearchFieldDataType.String),
        SearchField(
            name="contentVector",
            type=SearchFieldDataType.Collection(SearchFieldDataType.Single),
            searchable=True,
            # Size of the vector created by the text-embedding-ada-002 model.
            vector_search_dimensions=1536,
            vector_search_profile_name="myHnswProfile",
        ),
    ]

    # The "content" field should be prioritized for semantic ranking.
    semantic_config = SemanticConfiguration(
        name="default",
        prioritized_fields=SemanticPrioritizedFields(
            title_field=SemanticField(field_name="title"),
            keywords_fields=[],
            content_fields=[SemanticField(field_name="content")],
        ),
    )

    # For vector search, we want to use the HNSW (Hierarchical Navigable Small World)
    # algorithm (a type of approximate nearest neighbor search algorithm) with cosine
    # distance.
    vector_search = VectorSearch(
        algorithms=[
            HnswAlgorithmConfiguration(
                name="myHnsw",
                kind=VectorSearchAlgorithmKind.HNSW,
                parameters=HnswParameters(
                    m=4,
                    ef_construction=400,
                    ef_search=500,
                    metric=VectorSearchAlgorithmMetric.COSINE,
                ),
            ),
            ExhaustiveKnnAlgorithmConfiguration(
                name="myExhaustiveKnn",
                kind=VectorSearchAlgorithmKind.EXHAUSTIVE_KNN,
                parameters=ExhaustiveKnnParameters(
                    metric=VectorSearchAlgorithmMetric.COSINE
                ),
            ),
        ],
        profiles=[
            VectorSearchProfile(
                name="myHnswProfile",
                algorithm_configuration_name="myHnsw",
            ),
            VectorSearchProfile(
                name="myExhaustiveKnnProfile",
                algorithm_configuration_name="myExhaustiveKnn",
            ),
        ],
    )

    # Create the semantic settings with the configuration
    semantic_search = SemanticSearch(configurations=[semantic_config])

    # Create the search index.
    index = SearchIndex(
        name=name,
        fields=fields,
        semantic_search=semantic_search,
        vector_search=vector_search,
    )

    return index


# In[4]:


def gen_contoso_products(
    path: str,
) -> List[Dict[str, any]]:
    openai_service_endoint = os.environ["AZURE_OPENAI_ENDPOINT"]
    openai_deployment = "text-embedding-ada-002"

    token_provider = get_bearer_token_provider(DefaultAzureCredential(), "https://cognitiveservices.azure.com/.default")
    # openai.Embedding.create() -> client.embeddings.create()
    client = AzureOpenAI(
        api_version="2023-07-01-preview",
        azure_endpoint=openai_service_endoint,
        azure_deployment=openai_deployment,
         azure_ad_token_provider=token_provider
    )

    products = pd.read_csv(path)
    items = []
    for product in products.to_dict("records"):
        content = product["description"]
        id = str(product["id"])
        title = product["name"]
        url = f"/products/{title.lower().replace(' ', '-')}"
        emb = client.embeddings.create(input=content, model=openai_deployment)
        rec = {
            "id": id,
            "content": content,
            "filepath": f"{title.lower().replace(' ', '-')}",
            "title": title,
            "url": url,
            "contentVector": emb.data[0].embedding,
        }
        items.append(rec)

    return items


# In[5]:


contoso_search = os.environ["AZURE_SEARCH_ENDPOINT"]
index_name = "contoso-products"

search_index_client = SearchIndexClient(
    contoso_search, DefaultAzureCredential()
)

delete_index(search_index_client, index_name)
index = create_index_definition(index_name)
print(f"creating index {index_name}")
search_index_client.create_or_update_index(index)
print(f"index {index_name} created")


# In[6]:


print(f"indexing documents")
docs = gen_contoso_products("../product_info/products.csv")
# Upload our data to the index.
search_client = SearchClient(
    endpoint=contoso_search,
    index_name=index_name,
    credential=DefaultAzureCredential(),
)
print(f"uploading {len(docs)} documents to index {index_name}")
ds = search_client.upload_documents(docs)

