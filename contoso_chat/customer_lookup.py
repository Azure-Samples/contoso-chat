from typing import Dict
from promptflow import tool
from azure.cosmos import CosmosClient
from promptflow.connections import CustomConnection


@tool
def customer_lookup(customerId: str, conn: CustomConnection) -> str:
    client = CosmosClient(url=conn.configs["endpoint"], credential=conn.secrets["key"])
    db = client.get_database_client(conn.configs["databaseId"])
    container = db.get_container_client(conn.configs["containerId"])
    response = container.read_item(item=customerId, partition_key=customerId)
    response["orders"] = response["orders"][:2]
    return response
