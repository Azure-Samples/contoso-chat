# 3. The App Architecture

The workshop teaches you to **build, evaluate, and deploy a retail copilot** code-first on Azure AI - using this application architecture for our Contoso Chat implementation.

![ACA Architecture](./../img/aca-architecture.png)

Click on each tab to understand the archtiecture components and processing workflow.

---

=== "1. Architecture Components"

    The architecture has these core components:

    - _Azure AI Search_ → the **information retrieval** service (product index)
    - _Azure CosmosDB_ → the **database** (customer profile, order history)
    - _Azure OpenAI_ → the **model deployments** (embedding, chat, eval)
    - _Azure Container Apps_ → the **app hosting** service (API endpoint)
    - _Azure Managed Identity_ → for **keyless authentication** (trustworthy AI)


=== "2. Processing Services"

    The Architecture "processes" incoming user requests received on the hosted API endpoint by taking the following steps:

    1. Extracts _{question, customer id, chat history}_ parameters from request.
    1. The parsed parameters are used to trigger chat AI (_get-request_)
    1. The _customer id_ is used to retrieve customer profile from Azure Cosmos DB
    1. 

    1. The _customer ID_ is used to retrieve customer order history from _Azure Cosmos DB_
    1. The _user question_ is converted from text to vector using an _Azure OpenAI_ embedding model.
    1. The _vectorized question_ is used to retrieve matching products from _Azure AI Search_
    1. The user question & retrieved documents are combined into an _enhanced model prompt_
    1. The prompt is used to generate the chat response using an _Azure OpenAI_ chat model.
    1. The response is now returned to the frontend chat UI client, for display to the user.
