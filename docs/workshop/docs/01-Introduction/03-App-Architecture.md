# 3. The App Architecture

Implementing this design pattern requires these architectural components:

 - an **information retrieval** service (data indexing, similarity search, semantic ranking)
 - a **database** service for storing other data (customer orders)
 - a **model deployments** capability (for chat, embeddings - and AI-assisted evaluation)
 - a **copilot hosting** capability (for real-world access to deployed endpoint)

The corresponding Azure AI application architecture for the Contoso Chat retail copilot is shown below. The copilot is deployed to Azure Container Apps, providing a hosted API endpoint for client integration. The copilot processes incoming requests with the help of:

 - **Azure OpenAI Services**  - provides model deployments for chat and text embeddings
 - **Azure CosmosDB**  - stores the customer order data (JSON) in a noSQL database
 - **Azure AI Search**  - indexes the product catalog with search-retrieval capability. 

![ACA Architecture](./../img/aca-architecture.png)

The copilot _orchestrates_ the steps of the RAG workflow using **Prompty** assets (configured with required Azure OpenAI models) executed in a Prompty runtime (Python). It supports multi-turn conversations and responsible AI practices to meet response quality and safety requirements.