# 3. The App Architecture

The workshop teaches you to **build, evaluate, and deploy a retail copilot** code-first on Azure AI - using this application architecture for our Contoso Chat implementation.

![ACA Architecture](./../img/aca-architecture.png)

Click on each tab to understand the archtiecture components and processing workflow.

---

=== "1. Architecture Components"

    The architecture contains these core components:

    - _Azure AI Search_ - an **information retrieval** service (product index, semantic ranking)
    - _Azure CosmosDB_ - a **database** for storing customer profiles (order history)
    - _Azure OpenAI_ - with **model deployments** (for embedding, chat, and evaluation)
    - _Azure Container Apps_ - a **application hosting** service (deployed API endpoint)
    - _Azure Managed Identity_ - for **keyless authentication** support (more trustworthy AI)


=== "2. Processing Services"

    The Contoso Chat AI application ("custom copilot") is integrated into a FastAPI application server that is hosted using Azure Container Apps. This exposes an API endpoint to frontend chat UI for user interactions. Incoming user requests are parsed to extract request parameters (_customer ID, chat history, user question_) and to invoke the copilot, which processes the request as follows:

    1. The _customer ID_ is used to retrieve customer order history from _Azure Cosmos DB_
    1. The _user question_ is converted from text to vector using an _Azure OpenAI_ embedding model.
    1. The _vectorized question_ is used to retrieve matching products from _Azure AI Search_
    1. The user question & retrieved documents are combined into an _enhanced model prompt_
    1. The prompt is used to generate the chat response using an _Azure OpenAI_ chat model.
    1. The response is now returned to the frontend chat UI client, for display to the user.
