#!/usr/bin/env python
# coding: utf-8

# In[1]:


from azure.cosmos import CosmosClient, exceptions, PartitionKey
from azure.identity import DefaultAzureCredential
import os
from dotenv import load_dotenv

load_dotenv()


# In[2]:


# from azure.identity import DefaultAzureCredential, InteractiveBrowserCredential

# try:
#     credential = DefaultAzureCredential()
#     # Check if given credential can get token successfully.
#     credential.get_token("https://management.azure.com/.default")
# except Exception as ex:
#     # Fall back to InteractiveBrowserCredential in case DefaultAzureCredential not work
#     # This will open a browser page for
#     credential = InteractiveBrowserCredential()


# In[3]:


# Set the Cosmos DB endpoint, key and database name in the .env file. The key and endpoint can be found in the resource created in the portal.
COSMOS_ENDPOINT = os.environ["COSMOS_ENDPOINT"]
client = CosmosClient(COSMOS_ENDPOINT, credential=DefaultAzureCredential())
DATABASE_NAME = 'contoso-outdoor'
CONTAINER_NAME = 'customers'


# In[4]:


# Get the database and container created by Bicep
database = client.get_database_client(DATABASE_NAME)
container = database.get_container_client(CONTAINER_NAME)

print(database)


# In[5]:


# Loop through each json file in data/customer_info and insert into container
import os
import json
import glob
path = './../customer_info'
for filename in glob.glob(os.path.join(path, '*.json')):
    with open(filename) as file:
        customer = json.load(file)
        container.upsert_item(customer)
        print('Upserted item with id {0}'.format(customer['id']))


# In[6]:


# Get items from container to validate they were inserted
print('Get all items in container')
items = list(container.read_all_items(max_item_count=10))
print(items)

