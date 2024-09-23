# Build a Retail Copilot Code-First on Azure AI

!!! example "Microsoft AI Tour Attendees:  <br/> To get started with this workshop, [make sure you have everything you need](00-Before-You-Begin/index.md) to start building."   

This website contains the step-by-step instructions for a hands-on workshop that teaches you how to **build, evaluate, and deploy a retail copilot code-first on Azure AI**. 

- Our solution use the [Retrieval Augmented Generation (RAG) pattern](https://learn.microsoft.com/azure/ai-studio/concepts/retrieval-augmented-generation) to ground chat AI responses in the retailer's product catalog and cusomer data.
- Our implementation uses [Prompty](https://prompty.ai) for ideation, [Azure AI Studio](https://ai.azure.com) as the platform for code-first copilotdevelopment, and [Azure Container Apps](https://aka.ms/azcontainerapps) for hosting the deployed copilot.

In this section, we introduce the application scenario (Contoso Chat), review the design pattern used (RAG) and understand how it maps to our application architecture (on Azure AI). We'll wrap the section by understanding the application lifecycle (GenAIOps) and the three stages for end-to-end development that we will follow in this workshop.

---

## 1. The App Scenario

**Contoso Outdoors** is an enterprise retailer that sells a wide variety of hiking and camping equipment to outdoor adventurer through their website. Customers visiting the site often call the customer support line with requests for product information or recommendations, before making their purchases. The retailer decides to build and integrate an AI-based _customer support agent_ (retail copilot) to handle these queries right from their website, for efficiency.

![Contoso Chat UI](./img/chat-ui.png)

**Contoso Chat** is the chat AI implementation (_backend_) for the retail copilot experience. It has a hosted API (_endpoint_) that the chat UI (_frontend_) can interact with to process user requests. Customers can now ask questions in a conversational format, using natural language, and get valid responses grounded in product data and their own purchase history.

![Contoso Chat AI](./img/chat-ai.png)
 
## 2. The RAG Pattern

Foundation large language models are trained on massive quantities of public data, giving them the ability to answer general questions effectively. However, our retail copilot needs responses grounded in _private data_ that exists in the retailer's data stores. _Retrieval Augmented Generation_ (RAG) is a design pattern that provides a popular solution to this challenge with this workflow:

1. The user query arrives at our copilot implementation via the endpoint (API).
1. The copilot sends the text query to a **retrieval** service which vectorizes it for efficiency.
1. It uses this vector to query a search index for matching results (e.g., based on similarity)
1. The retrieval service returns results to the copilot, potentially with semantic ranking applied.
1. The copilot **augments** the user prompt with this knowledge, and invokes the chat model.
1. The chat model now **generates** responses _grounded_ in the provided knowledge.

![RAG](./img/rag-design-pattern.png)
 
## 3. The App Architecture

Implementing this design pattern requires these architectural components:

 - an **information retrieval** service (data indexing, similarity search, semantic ranking)
 - a **database** service for storing other data (customer orders)
 - a **model deployments** capability (for chat, embeddings - and AI-assisted evaluation)
 - a **copilot hosting** capability (for real-world access to deployed endpoint)

The corresponding Azure AI application architecture for the Contoso Chat retail copilot is shown below. The copilot is deployed to Azure Container Apps, providing a hosted API endpoint for client integration. The copilot processes incoming requests with the help of:

 - **Azure OpenAI Services**  - provides model deployments for chat and text embeddings
 - **Azure CosmosDB**  - stores the customer order data (JSON) in a noSQL database
 - **Azure AI Search**  - indexes the product catalog with search-retrieval capability. 

![ACA Architecture](./img/aca-architecture.png)

The copilot _orchestrates_ the steps of the RAG workflow using **Prompty** assets (configured with required Azure OpenAI models) executed in a Prompty runtime (Python). It supports multi-turn conversations and responsible AI practices to meet response quality and safety requirements.

## 4. The App Lifecycle

Building generative AI applications requires an iterative process of refinement from _prompt_ to _production_. The application  lifecycle (GenAIOps) is best illustrated by the three stages shown:

1. **Ideation** - involves building the initial prototype, validating it manually with a test prompt.
2. **Evaluation** - involves assessing it for quality and safety with large, diverse test datasets.
3. **Operationalization** - involves deploying it for real-world usage & monitoring it for insights.

![GenAIOps](./img/gen-ai-ops.png)

In our workshop, you willl see the development workflow organized into sections that mimic this lifecycle - giving you a more intuitive sense for how you can iteratively go from promt to production, code-first, with Azure AI.

## 5. Related Resources

1. **Prompty** | [Documentation](https://prompty.ai) · [Specification](https://github.com/microsoft/prompty/blob/main/Prompty.yaml)  · [Tooling](https://marketplace.visualstudio.com/items?itemName=ms-toolsai.prompty) · [SDK](https://pypi.org/project/prompty/)
1. **Azure AI Studio**  | [Documentation](https://learn.microsoft.com/en-us/azure/ai-studio/)  · [Architecture](https://learn.microsoft.com/azure/ai-studio/concepts/architecture) · [SDKs](https://learn.microsoft.com/azure/ai-studio/how-to/develop/sdk-overview) ·  [Evaluation](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-generative-ai-app)
1. **Azure AI Search** | [Documentation](https://learn.microsoft.com/azure/search/)  · [Semantic Ranking](https://learn.microsoft.com/azure/search/semantic-search-overview) 
1. **Azure Container Apps**  | [Azure Container Apps](https://learn.microsoft.com/azure/container-apps/)  · [Deploy from code](https://learn.microsoft.com/en-us/azure/container-apps/quickstart-repo-to-cloud?tabs=bash%2Ccsharp&pivots=with-dockerfile)
1. **Responsible AI**  | [Overview](https://www.microsoft.com/ai/responsible-ai)  · [With AI Services](https://learn.microsoft.com/en-us/azure/ai-services/responsible-use-of-ai-overview?context=%2Fazure%2Fai-studio%2Fcontext%2Fcontext)  · [Azure AI Content Safety](https://learn.microsoft.com/en-us/azure/ai-services/content-safety/)


---

!!! example "To get started with this workshop, [make sure you have everything you need](00-Before-You-Begin/index.md) to start building."