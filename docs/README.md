# Deconstructing Contoso Chat: Self-Guided Workshop 

[Contoso Chat](https://github.com/Azure-Samples/contoso-chat) is an open-source application sample that teaches you how to build a modern generative AI application using the Azure AI platform (development) and the Azure Developer CLI (deployment) to streamline your end-to-end developer experience.

This document walks you through the steps needed to understand the application scenario, architecture, codebase (v1 vs. v2), and developer workflow (setup-develop-evaluate-deploy-iterate) required for building a retail copilot application end-to-end on the Azure AI platform.

## 1. Application Scenario

This sample teaches you how to design, develop, evaluate, and deploy, a _retail copilot application_ using the Azure AI Studio with promptflow. The application scenario focuses on a fictional retailer (Contoso Outdoor Company) that has a website where outdoor enthusiasts can purchase hiking and camping equipment as shown below. The company has two data sources:
- A site product catalog (with indexes stored in Azure AI Search)
- A customer orders database (with data stored in Azure Cosmos DB)

![Contoso Outdoors](./img/00-app-scenario-ui.png)

The _Contoso Chat_ application implements the copilot AI backend that integrates with this front-end, allowing customers to "chat with the copilot" to get answers about the products and recommendations based on their order history - _simply by clicking the chat icon seen at the bottom right corner of the website_. This chat experience is powered by the Contoso Chat API endpoint that you will be deploying by the end of this workshop, allowing customer requests to be responded to in real-time using a custom model that is grounded in the product catalog and customer history data.

![Contoso Chat](./img/00-app-scenario-ai.png)

## 2. Copilot Implementation

The _basic copilot_ implementation is shown at a high level in the diagram below. the Contoso Chat API (copilot API) exposes a _managed online endpoint_ that receives requests from remote clients like the website. 
- The requests are handled by your _chat application_ which implements the "chat function" block seen below.
- This uses a Retrieval Augmented Generation pattern on input prompt (_user question_) to enhance the request (_model prompt_).
- The model prompt is sent to a chat model (_Azure OpenAI service_) which returns a response (_answer_).
- The answer is then presented to the user on the chat UI (_website_) to complete the interaction.

The Contoso Chat scenario extends this basic copilot implementation with **an additional "customer lookup" step** that retrieves relevant customer orders related to the user question. This information is added into the previously created model prompt, to generate a new _model prompt_ that is send to the chat model. The final response will now reflect both the product catalog and customer history data.

![Copilot Architecture](./img/00-app-architecture-copilot.png)

## 3. End-to-End Workflow

The Contoso Chat application sample reflects the end-to-end developer workflow for building a generative AI application on the Azure AI platform. You'll go from from _prompt engineering_ (ideation using the RAG pattern with promptflow) to _LLM Ops_ (iterative evaluation for response quality, and deployment for operationalization) as shown below.

![LLM Ops](./img/00-llmops-lifecycle.png)

## 4. Developer Experience

The end-to-end developer experience is streamlined by the use of four core components in our developer platform:
- **Azure AI Studio**: A unified platform for exploring AI models, managing AI application resources, and building AI projects. It supports both code-first (SDK) and low-code (UI) approaches for building generative AI applications end-to-end.
- **Promptflow**: An open-source framework that simplifies the ideation and evaluation phases of this workflow with support for
  - _prompty assets_ for simplifying your prompt engineering process
  - _dag-flow_ option for building applications as a directed acyclic graph
  - _flex-flow_ option (new) that supports more flexibility in tool integrations
  - _pf tools_ with CLI and IDE based options for simplifed developer experience
- **Azure Developer CLI**: A command-line tool that supports _infrastructure-as-code_ configuration for consistent and repeatable deployments of AI applications on Azure - that can also be version controlled and shared across teams. It provides three key features:
  - _azd-template_ configuration for managing application resources
  - _azd_ CLI for managing resource provisioning & deployments from command-line
  - _azd extension_ for Visual Studio Code, achieving the same goals from the IDE
- **Dev Containers**: These enforce a _configuration-as-code_ approach by defining the required development dependencies in a "development container" that can be launched in the cloud (with GitHub Codespaces) or in your local device (with Docker Desktop). It has 3 key features:
  - Python runtime with all required tools (`azd`, `pf`, `az`) and packages (`pip` dependencies) pre-installed.
  - Visual Studio Code IDE with required extensions - for local development
  - GitHub Codespaces support - for local development in a cloud-hosted VM

To get started, the easiest way is to fork the Contoso Chat repository, and launch a development container to get a pre-built development environment. Then follow these instructions for next steps.
 - [README-v1](README-v1.md) for v1 using DAG flow
 - [README-v2](README-v2.md) for v2 using Flex flow

---