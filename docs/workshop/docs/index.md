# Build a Retail Copilot Code-First on Azure AI

This website contains the step-by-step instructions for a hands-on workshop that teaches you how to **build, evaluate, and deploy a retail copilot code-first on Azure AI**. 

- The solution uses the [Retrieval Augmented Generation (RAG) pattern](https://learn.microsoft.com/azure/ai-studio/concepts/retrieval-augmented-generation) to ground chat AI responses in the retailer's product catalog and cusomer data.
- The implementation uses [Prompty](https://prompty.ai) for ideation, [Azure AI Studio](https://ai.azure.com) as the underlying platform for GenAIOps, and [Azure Container Apps](https://aka.ms/azcontainerapps) for hosting the deployed copilot.

This section introduces you to the application scenario (retail copilot), briefly reviews the Retrieval Augmented Generation (RAG) design pattern implemented, and illustrates the Azure AI application architecture used for solution deployment - with a link to resources for the key developer tools and services used.

---

## 1. The App Scenario

**Contoso Outdoors** is an enterprise retailer that sells a wide variety of hiking and camping equipment to outdoor adventurers. The retailer's website has an extensive catalog of products with customers constantly asking questions and looking for information and recommendations, to make relevant purchases. The retailer decides to build a _customer support agent_ to handle these queries right within the website.

![Contoso Chat UI](./img/chat-ui.png)

**Contoso Chat** is the implementation of that vision, with a retail copilot backend that can be interacted with directly from the website. Customers can now ask the chatbot questions _in natural language_ - and get back valid responses that are grounded in the product catalog and their own purchase history.

![Contoso Chat AI](./img/chat-ai.png)
 
## 2. The RAG Pattern

Many foundation models are trained on massive quantities of public data, giving them the ability to answer general-purpose queries effectively. However, in our app scenario we want responses based on private data from the retailer databases. The _Retrieval Augmented Generation_ (RAG) pattern is currently the recommended approach to solving this problem.

1. The user query arrives at our copilot implementation via the endpoint (API).
1. It sends the text query to a **retrieval** service which vectorizes it for efficiency.
1. It uses this vector to query a search index for matching results (e.g., based on similarity)
1. It then returns results to the copilot, potentially with semantic ranking applied.
1. The copilot **augments** the prompt with the results, then calls the chat model.
1. The chat model now **generates** responses _grounded_ in the knowledge provided.

![RAG](./img/rag-design-pattern.png)
 
## 3. The App Architecture

Implementing this design pattern requires:

 - an **information retrieval** service (data indexing, similarity search, semantic ranking)
 - a **database** service for storing other data (customer orders)
 - a **model deployments** capability (for chat, embeddings - and AI-assisted evaluation)
 - a **copilot hosting** capability (for real-world access to deployed endpoint)

The figure below shows the Azure application architecture for the Contoso Chat Retail Copilot, showcasing these elements. The copilot is deployed to Azure Container Apps, providing a hosted API endpoint for client integration. Requests to that endpoint are processed with:

 - **Azure OpenAI Services**  - provides model deployments for chat and text embeddings
 - **Azure CosmosDB**  - stores the customer order data (JSON) in a noSQL database
 - **Azure AI Search**  - indexes the product catalog with search-retrieval capability. 

![ACA Architecture](./img/aca-architecture.png)

The _orchestration_ of RAG workflow steps is achieved using **Prompty** assets configured with relevant Azure OpenAI models and executed in a Prompty runtime (Python). This solution can support _multi-turn conversations_ and illustrates usage of _responsible AI_ practices (i.e., evaluation, content safety) to deliver responses that meet desired quality and safety standards.

## 4. Related Resources

1. **Prompty** | [Documentation](https://prompty.ai) · [Specification](https://github.com/microsoft/prompty/blob/main/Prompty.yaml)  · [Tooling](https://marketplace.visualstudio.com/items?itemName=ms-toolsai.prompty) · [SDK](https://pypi.org/project/prompty/)
1. **Azure AI Studio**  | [Documentation](https://learn.microsoft.com/en-us/azure/ai-studio/)  · [Architecture](https://learn.microsoft.com/azure/ai-studio/concepts/architecture) · [SDKs](https://learn.microsoft.com/azure/ai-studio/how-to/develop/sdk-overview) ·  [Evaluation](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-generative-ai-app)
1. **Azure AI Search** | [Documentation](https://learn.microsoft.com/azure/search/)  · [Semantic Ranking](https://learn.microsoft.com/azure/search/semantic-search-overview) 
1. **Azure Container Apps**  | [Azure Container Apps](https://learn.microsoft.com/azure/container-apps/)  · [Deploy from code](https://learn.microsoft.com/en-us/azure/container-apps/quickstart-repo-to-cloud?tabs=bash%2Ccsharp&pivots=with-dockerfile)
1. **Responsible AI**  | [Overview](https://www.microsoft.com/ai/responsible-ai)  · [With AI Services](https://learn.microsoft.com/en-us/azure/ai-services/responsible-use-of-ai-overview?context=%2Fazure%2Fai-studio%2Fcontext%2Fcontext)  · [Azure AI Content Safety](https://learn.microsoft.com/en-us/azure/ai-services/content-safety/)


---

To get started with this workshop, [make sure you have everything you need](00-Before-You-Begin/index.md) to start building.