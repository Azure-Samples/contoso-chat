# 1.1 | What You'll Learn

This is a 60-75 minute workshop that consists of a series of lab exercises that teach you how to build a production RAG (Retrieval Augmented Generation) based LLM application using Promptflow and Azure AI Studio.

You'll gain hands-on experience with the various steps involved in the _end-to-end application development lifecycle_ from prompt engineering to LLM Ops.

---

## Learning Objectives

!!!info "By the end of this lab, you should be able to:"

1. Explain **LLMOps** - concepts & differentiation from MLOps.
1. Explain **Prompt Flow** - concepts & tools for building LLM Apps.
1. Explain **Azure AI Studio** - features & functionality for streamlining E2E app development.
1. **Design, run & evaluate** RAG apps - using the Promptflow Extension on VS Code
1. **Deploy, test & use** RAG apps - from Azure AI Studio UI (no code experience)

---

## Pre-Requisites

!!!info "We assume you have familiarity with the following:"

1. Machine Learning & Generative AI _concepts_
1. Python & Jupyter Notebook _programming_
1. Azure, GitHub & Visual Studio Code _tooling_

!!!info "You will need the following to complete the lab:"

1. Your own laptop (charged) with a modern browser
1. A GitHub account with GitHub Codespaces quota.
1. An Azure subscription with Azure OpenAI access.
1. An Azure AI Search resource with Semantic Ranker enabled.

---

## Dev Environment

You'll make use of the following resources in this workshop:

!!!info "Code Samples (GitHub Repositories)"

 - [Contoso Chat](https://github.com/Azure-Samples/contoso-chat) - source code for the RAG-based LLM app.
 - [Contoso Web](https://github.com/Azure-Samples/contoso-web) - source code for the Next.js-based Web app.


!!!info "Developer Tools (local and cloud)"

 - [Visual Studio Code](https://code.visualstudio.com/) - as the default editor
 - [Github Codespaces](https://github.com/codespaces) - as the dev container
 - [Azure AI Studio (Preview)](https://ai.azure.com) - for AI projects
 - [Azure ML Studio](https://ml.azure.com) - for minor configuration
 - [Azure Portal](https://portal.azure.com) - for managing Azure resources
 - [Prompt Flow](https://github.com/microsoft/promptflow) - for streamlining end-to-end LLM app dev

!!!info "Azure Resources (Provisioned in Subscription)"

 - [Azure AI Resource](https://learn.microsoft.com/azure/ai-studio/concepts/ai-resources) - top-level AI resource, provides hosting environment for apps
 - [Azure AI Project](https://learn.microsoft.com/azure/ai-studio/how-to/create-projects) - organize work & save state for AI apps.
 - [Azure AI Search](https://learn.microsoft.com/azure/search/search-create-service-portal) - full-text search, indexing & information retrieval. (product data)
 - [Azure OpenAI Service](https://learn.microsoft.com/azure/ai-services/openai/overview) - chat completion & text embedding models. (chat UI, RAG)
 - [Azure Cosmos DB](https://learn.microsoft.com/azure/cosmos-db/nosql/quickstart-portal) - globally-distributed multi-model database. (customer data)
 - [Azure Static Web Apps](https://learn.microsoft.com/azure/static-web-apps/overview) - optional, deploy Contoso Web application. (chat integration)

===