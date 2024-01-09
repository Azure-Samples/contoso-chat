# About Workshop

**This is a hands-on workshop to teach you how to build a RAG-based LLM application _end-to-end_ using Azure AI Studio and Prompt Flow.**

This lab has been designed to work in both instructor-led sessions (at a Microsoft event) and as a self-guided exercise (at home). _The instructions below are meant for self-guided learning_. Instructor-led sessions will have their own adapted version of this manual, using the [Skillable LabOnDemand](https://skillable.com) platform and come with a built-in Azure subscription.

!!! info "PRE-REQUISITES"

    - **GitHub Account** - with GitHub Codespaces. _Free quota is sufficient_.
    - **Your own laptop** - fully-charged. _This is a 75-minute lab_.
    - **Modern browser** - on laptop. _To launch the Lab-on-Demand session_.
    - **Azure subscription** - with Azure OpenAI access. _For model deployments_.

This lab requires a _paid Azure subscription_ to cover usage of some features (e.g., _Semantic Search_ feature in Azure AI Search).

## Learning Objectives

In this lab we'll learn to _build, run, evaluate, and deploy_ a RAG-based application ("Contoso Chat") using Azure AI Studio and Prompt Flow. By the end of this lab, you should be able to:

1. Explain **LLMOps** concepts & benefits.
1. Explain **Prompt Flow** concept & benefits.
1. Explain **Azure AI Studio** features & usage.
1. Use **Prompt Flow** on Visual Studio Code
1. Design **RAG-based LLM Applications**
1. Build, run, evaluate & deploy RAG-based LLM apps **on Azure**.

## Dev Environment

The repository is instrumented with [dev container](https://containers.dev) configuration that provides a consistent pre-built development environment deployed in a Docker container. Launch this in the cloud with [GitHub Codespaces](https://docs.github.com/codespaces), or in your local device with [Docker Desktop](https://www.docker.com/products/docker-desktop/).

In addition, we make use of these tools:

- **[Visual Studio Code](https://code.visualstudio.com/) as the default editor** | Works seamlessly with dev containers. Extensions streamline development with Azure and Prompt Flow. 
- **[Azure Portal](https://portal.azure.com) for Azure subscription management** | Single pane of glass view into all Azure resources, activities, billing and more.
- **[Azure AI Studio (Preview)](https://ai.azure.com)** | Single pane of glass view into all resources and assets for your Azure AI projects. Currently in preview (expect it to evolve rapidly).
- **[Azure ML Studio](https://ml.azure.com)** | Enterprise-grade AI service for managing end-to-end ML lifecycle for operationalizing AI models. Used for some configuration operations in our workshop (expect support to move to Azure AI Studio).
- **[Prompt Flow](https://github.com/microsoft/promptflow)** | Open-source tooling for orchestrating end-to-end development workflow (design, implementation, execution, evaluation, deployment) for modern LLM applications.

## Required Resources

We make use of the following resources in this lab:

!!!info "Azure Samples Used | **Give them a ⭐️ on GitHub**"

    - [Contoso Chat](https://github.com/Azure-Samples/contoso-chat) - as the RAG-based AI app _we will build_.
    - [Contoso Outdoors](https://github.com/Azure-Samples/contoso-web) - as the web-based app _using our AI_.

!!!info "Azure Resources Used | **Check out the Documentation**"

    - [Azure AI Resource](https://learn.microsoft.com/azure/ai-studio/concepts/ai-resources) - Top-level Azure resource for AI Studio, establishes working environment.
    - [Azure AI Project](https://learn.microsoft.com/azure/ai-studio/how-to/create-projects) - saves state and organizes work for AI app development.
    - [Azure AI Search](https://learn.microsoft.com/azure/search/search-what-is-azure-search) - get secure information retrieval at scale over user-owned content 
    - [Azure Open AI](https://learn.microsoft.com/azure/ai-services/openai/overview) - provides REST API access to OpenAI's powerful language models.
    - [Azure Cosmos DB](https://learn.microsoft.com/azure/cosmos-db/) - Fully managed, distributed NoSQL & relational database for modern app development.
    - [Deployment Models](https://learn.microsoft.com/azure/ai-studio/how-to/model-catalog) Deployment from model catalog by various criteria.
