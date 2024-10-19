---
page_type: sample
languages:
- azdeveloper
- python
- bash
- bicep
- prompty
products:
- azure
- azure-openai
- azure-cognitive-search
- azure-cosmos-db
urlFragment: contoso-chat
name: Contoso Chat - Retail RAG Copilot with Azure AI Studio and Prompty (Python Implementation)
description: Build, evaluate, and deploy, a RAG-based retail copilot that responds to customer questions with responses grounded in the retailer's product and customer data.
---
<!-- YAML front-matter schema: https://review.learn.microsoft.com/en-us/help/contribute/samples/process/onboarding?branch=main#supported-metadata-fields-for-readmemd -->

> [!WARNING]  
> **This sample is being actively updated at present and make have breaking changes**. We are refactoring the code to use new Azure AI platform features and moving deployment from Azure AI Studio to Azure Container Apps. We will remove this notice once the migration is complete. Till then, please pause on submitting new issues as codebase is changing.
>
> **Some of the features used in this repository are in preview.** Preview versions are provided without a service level agreement, and they are not recommended for production workloads. Certain features might not be supported or might have constrained capabilities. For more information, see [Supplemental Terms of Use for Microsoft Azure Previews](https://azure.microsoft.com/en-us/support/legal/preview-supplemental-terms/).**


# Contoso Chat: Retail RAG Copilot with Azure AI Studio and Prompty

[![Open in GitHub Codespaces](https://img.shields.io/static/v1?style=for-the-badge&label=GitHub+Codespaces&message=Open&color=brightgreen&logo=github)](https://github.com/codespaces/new?hide_repo_select=true&machine=basicLinux32gb&repo=725257907&ref=main&devcontainer_path=.devcontainer%2Fdevcontainer.json&geo=UsEast)
[![Open in Dev Containers](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/azure-samples/contoso-chat)


## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Pre-Requisites](#pre-requisites)
- [Getting Started](#getting-started)
- [Development](#development)
- [Testing](#testing)
- [Deployment](#deployment)
- [Costs](#costs)
- [Security Guidelines](#security-guidelines)
- [Resources](#resources)
- [Code of Conduct](#code-of-conduct)
- [Responsible AI Guidelines](#responsible-ai-guidelines)

---

## Overview

_Contoso Outdoor_ is an online retailer specializing in hiking and camping equipment for outdoor enthusiasts. The website offers an extensive catalog of products - resulting in customers needing product information and recommendations to assist them in making relevant purchases.

![Contoso Outdoor](./img/app-scenario-ui.png)

This sample implements _Contoso Chat_ - a retail copilot solution for Contoso Outdoor that uses a _retrieval augmented generation_ design pattern to ground chatbot responses in the retailer's product and customer data. Customers can now ask questions from the website in natural language, and get relevant responses along with potential recommendations based on their purchase history - with responsible AI practices to ensure response quality and safety.

![Contoso Chat](./img/app-scenario-ai.png)

The sample illustrates the end-to-end workflow (GenAIOps) for building a RAG-based copilot **code-first** with Azure AI and Prompty. By exploring and deploying this sample, you will learn to:

1. Ideate and iterate rapidly on app prototypes using [Prompty](https://prompty.ai)
1. Deploy and use [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/) models for chat, embeddings and evaluation
1. Use Azure AI Search (indexes) and Azure CosmosDB (databases) for your data
1. Evaluate chat responses for quality using AI-assisted evaluation flows
1. Host the application as a FastAPI endpoint deployed to Azure Container Apps
1. Provision and deploy the solution using the Azure Developer CLI
1. Support Responsible AI practices with content safety & assessments


## Features

The project template provides the following features:

- [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/) for embeddings, chat, and evaluation models
- [Prompty](https://prompty.ai) for creating and managing prompts for rapid ideati
- [Azure AI Search](https://azure.microsoft.com/products/ai-services/ai-search) for performing semantic similarity search
- [Azure CosmosDB](https://learn.microsoft.com/azure/cosmos-db/) for storing customer orders in a noSQL database 
- [Azure Container Apps](https://learn.microsoft.com/azure/container-apps/overview) for hosting the chat AI endpoint on Azure

It also comes with:
- Sample product and customer data for rapid prototyping
- Sample application code for chat and evaluation workflows
- Sample datasets and custom evaluators using prompty assets

### Architecture Diagram 
![Architecture](./img/arch-contoso-retail-aca.png)

### Demo Video

(In Planning) - Get an intuitive sense for how simple it can be to go from template discovery, to codespaces launch, to application deployment with `azd up`. Watch this space for a demo video.

### Versions

The Contoso Chat sample has undergone numerous architecture and tooling changes since its first version back in 2023. The table below links to legacy versions for awareness only. **We recommend all users start with the latest version to leverage the latest tools and practices**.

> | Version | Description |
> |:---|:---|
> | v0 : [#cc2e808](https://github.com/Azure-Samples/contoso-chat/tree/cc2e808eee29768093866cf77a16e8867adbaa9c) | MSAITour 2023-24 (dag-flow, jnja template) - Skillable Lab |
> | v1 : [msbuild-lab322](https://github.com/Azure-Samples/contoso-chat/tree/msbuild-lab322) | MSBuild 2024 (dag-flow, jnja template) - Skillable Lab |
> | v2 : [raghack-24](https://github.com/Azure-Samples/contoso-chat/tree/raghack-24) | RAG Hack 2024 (flex-flow, prompty asset) - AZD Template |
> | v3 : [main](https://github.com/Azure-Samples/contoso-chat/tree/raghack-24)  🆕| MSAITour 2024-25 (prompty asset, ACA)- AZD Template |
> | | |

## Pre-requisites

To deploy and explore the sample, you will need:

1. An active Azure subscription - [Signup for a free account here](https://azure.microsoft.com/free/)
1. An active GitHub account - [Signup for a free account here](https://github.com/signup)
1. Access to Azure OpenAI Services - [Learn about Limited Access here](https://learn.microsoft.com/legal/cognitive-services/openai/limited-access)
1. Access to Azure AI Search - [With Semantic Ranker](https://learn.microsoft.com/en-us/azure/search/semantic-search-overview) (premiun feature)
1. Available Quota for: `text-embedding-ada-002`, `gpt-35-turbo`. and `gpt-4`

We recommend deployments to `swedencentral` or `francecentral` as regions that can support all these models. In addition to the above, you will also need the ability to:
 - provision Azure Monitor (free tier)
 - provision Azure Container Apps (free tier)
 - provision Azure CosmosDB for noSQL (free tier)

From a tooling perspective, familiarity with the following is useful:
 - Visual Studio Code (and extensions)
 - GitHub Codespaces and dev containers
 - Python and Jupyter Notebooks
 - Azure CLI, Azure Developer CLI and commandline usage


## Getting Started

You have three options for setting up your development environment:

1. Use GitHub Codespaces - for a prebuilt dev environment in the cloud
1. Use Docker Desktop - for a prebuilt dev environment on local device
1. Use Manual Setup - for control over all aspects of local env setup

**We recommend going with GitHub Codespaces** for the fastest start and lowest maintenance overheads. Pick one option below - click to expand the section and view the details.

<details>
<summary> 1️⃣ | Quickstart with GitHub Codespaces </summary>

1. Fork this repository to your personal GitHub account
1. Click the green `Code` button in your fork of the repo
1. Select the `Codespaces` tab and click `Create new codespaces ...`
1. You should see: a new browser tab launch with a VS Code IDE
1. Wait till Codespaces is ready - VS Code terminal has active cursor.
1. ✅ | **Congratulations!** - Your Codespaces environment is ready!

</details>

<details>
<summary> 2️⃣ | Get Started with Docker Desktop </summary>

1. Install VS Code (with Dev Containers Extension) to your local device
1. Install Docker Desktop to your local device - and start the daemon
1. Fork this repository to your personal GitHub account
1. Clone the fork to your local device - open with Visual Studio Code
1. If Dev Containers Extension installed - you see: "Reopen in Container" prompt
1. Else [read Dev Containers Documentation](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers) - to launch it manually
1. Wait till the Visual Studio Code environment is ready - cursor is active.
1. ✅ | **Congratulations!** - Your Docker Desktop environment is ready!

</details>

<details>
<summary> 3️⃣ | Get Started with Manual Setup </summary>

1. Verify you have Python 3 installed on your machine
1. Install dependencies with `pip install -r src/api/requirements.txt`
1. Install the [Azure Developer CLI](https://aka.ms/install-azd) for your OS
1. Install the [Azure CLI](https://learn.microsoft.com/en-us/cli/azure/install-azure-cli) for your OS
1. Verify that all required tools are installed and active:
    ```bash
    az version
    azd version
    prompty --version
    python --version
    ```

</details>

<br/>

Once you have set up the development environment, it's time to get started with the _development_ workflow by first provisioning the required Azure infrastructure, then deploying the application from the template.

## Development

Regardless of the setup route you chose, you should at this point have a _Visual Studio Code_ IDE running, with the required tools and package dependencies met in the associated dev environment.

<details>
<summary> 1️⃣ | Authenticate With Azure </summary>

1. Open a VS Code terminal and authenticate with Azure CLI. Use the `--use-device-code` option if authenticating from GitHub Codespaces. Complete the auth workflow as guided.

    ```bash
    az login --use-device-code
    ```
1. Now authenticate with Azure Developer CLI in the same terminal. Complete the auth workflow as guided. You should see: **Logged in on Azure.**

    ```bash
    azd auth login
    ```
</details>

<details>
<summary> 2️⃣ |  Provision-Deploy with AZD </summary>

1. Run `azd up` to provision infrastructure _and_ deploy the application, with one command. (You can also use `azd provision`, `azd deploy` separately if needed)

    ```bash
    azd up
    ```
1. The command will ask for an `environment name`, a `location` for deployment and the `subscription` you wish to use for this purpose.
    - The environment name maps to `rg-ENVNAME` as the resource group created
    - The location should be `swedencentral` or `francecentral` for model quota
    - The subscription should be an active subscription meeting pre-requistes
1. The `azd up` command can take 15-20 minutes to complete. Successful completion sees a **`SUCCESS: ...`** messages posted to the console. We can now validate the outcomes.
</details>

<details>
<summary> 3️⃣ | Validate the Infrastructure </summary>

1. Visit the [Azure Portal](https://portal.azure.con) - look for the `rg-ENVNAME` resource group created above
1. Click the `Deployments` link in the **Essentials** section - wait till all are completed.
1. Return to `Overview` page - you should see: **35** deployments, **15** resources
1. Click on the `Azure CosmosDB resource` in the list
    - Visit the resource detail page - click "Data Explorer"
    - Verify that it has created a `customers` database with data items in it
1. Click on the `Azure AI Search` resource in the list
    - Visit the resource detail page - click "Search Explorer"
    - Verify that it has created a `contoso-products` index with data items in it
1. Click on the `Azure Container Apps` resource in the list
    - Visit the resource detail page - click `Application Url`
    - Verify that you see a hosted endpoint with a `Hello World` message on page
1. Next, visit the [Azure AI Studio](https://ai.azure.com) portal
    - Sign in - you should be auto-logged in with existing Azure credential
    - Click on `All Resources` - you should see an `AIServices` and `Hub` resources
    - Click the hub resource - you should see an `AI Project` resource listed
    - Click the project resource - look at Deployments page to verify models
1. ✅ | **Congratulations!** - Your Azure project infrastructure is ready!
</details>


<details>
<summary> 4️⃣ | Validate the Deployment </summary>

1. The `azd up` process also deploys the application as an Azure Container App
1. Visit the ACA resource page - click on `Application Url` to view endpoint
1. Add a `/docs` suffix to default deployed path - to get a Swagger API test page
1. Click `Try it out` to unlock inputs - you see `question`, `customer_id`, `chat_history`
    - Enter `question` = "Tell me about the waterproof tents"
    - Enter `customer_id` = 2
    - Enter `chat_history` = []
    - Click **Execute** to see results: _You should see a valid response with a list of matching tents from the product catalog with additional details_.
1. ✅ | **Congratulations!** - Your Chat AI Deployment is working! 

</details>

## Testing

We can think about two levels of testing - _manual_ validation and _automated_ evaluation. The first is interactive, using a single test prompt to validate the prototype as we iterate. The second is code-driven, using a test prompt dataset to assess quality and safety of prototype responses for a diverse set of prompt inputs - and score them for criteria like _coherence_, _fluency_, _relevance_ and _groundedness_ based on built-in or custom evaluators.

<details>
<summary> 1️⃣ | Manual Testing (interactive) </summary>
<br/>

The Contoso Chat application is implemented as a _FastAPI_ application that can be deployed to a hosted endpoint in Azure Container Apps. The API implementation is defined in `src/api/main.py` and currently exposes 2 routes:
 - `/` - which shows the default "Hello World" message
 - `/api/create_request` - which is our chat AI endpoint for test prompts

To test locally, we run the FastAPI dev server, then use the Swagger endpoint at the `/docs` route to test the locally-served endpoint in the same way we tested the deployed version/

- Change to the root folder of the repository
- Run `fastapi dev ./src/api/main.py` - it should launch a dev server
- Click `Open in browser` to preview the dev server page in a new tab
    - You should see: "Hello, World" with route at `/`
- Add `/docs` to the end of the path URL in the browser tab
    - You should see: "FASTAPI" page with 2 routes listed
    - Click the `POST` route then click `Try it out` to unlock inputs
- Try a test input
    - Enter `question` = "Tell me about the waterproof tents"
    - Enter `customer_id` = 2
    - Enter `chat_history` = []
    - Click **Execute** to see results: _You should see a valid response with a list of matching tents from the product catalog with additional details_.
1. ✅ | **Congratulations!** - You successfully tested the app locally

</details>

<details>
<summary> 2️⃣ | AI-Assisted Evaluation (code-driven) </summary>
<br/>

Testing a single prompt is good for rapid prototyping and ideation. But once we have our application designed, we want to validate the _quality and safety_ of responses against diverse test prompts. The sample shows you how to do **AI-Assisted Evaluation** using custom evaluators implemented with Prompty.

- Visit the `src/api/evaluators/` folder
- Open the `evaluate-chat-flow.ipynb` notebook - "Select Kernel" to activate
- Clear inputs and then `Run all` - starts evaluaton flow with `data.jsonl` test dataset
- Once evaluation completes (takes 10+ minutes), you should see
    - `results.jsonl` = the chat model's responses to test inputs
    - `evaluated_results.jsonl` = the evaluation model's scoring of the responses
    - tabular results = coherence, fluency, relevance, groundedness scores

Want to get a better understanding of how custom evaluators work? Check out the `src/api/evaluators/custom_evals` folder and explore the relevant Prompty assets and their template instructions.

The Prompty tooling also has support for built-in _tracing_ for observability. Look for a `.runs/` subfolder to be created during the evaluation run, with `.tracy` files containing the trace data. Click one of them to get a _trace-view_ display in Visual Studio Code to help you drill down or debug the interaction flow. _This is a new feature so look for more updates in usage soon_.

</details>

## Deployment

The solution is deployed using the Azure Developer CLI. The `azd up` command effectively calls `azd provision` and then `azd deploy` - allowing you to provision infrastructure and deploy the application with a single command. Subsequent calls to `azd up` (e.g., ,after making changes to the application) should be faster, re-deploying the application and updating infrastructure provisioning only if required. You can then test the deployed endpoint as described earlier.

## Costs

Pricing for services may vary by region and usage and exact costs are hard to determine. You can _estimate_ the cost of this project's architecture with [Azure's pricing calculator](https://azure.microsoft.com/pricing/calculator/) with these services:

- Azure OpenAI - Standard tier, GPT-35-turbo and Ada models. [See Pricing](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/)
- Azure AI Search - Basic tier, Semantic Ranker enabled. [See Pricing](https://azure.microsoft.com/en-us/pricing/details/search/)
- Azure Cosmos DB for NoSQL - Serverless, Free Tier. [See Pricing](https://azure.microsoft.com/en-us/pricing/details/cosmos-db/autoscale-provisioned/#pricing)
- Azure Monitor - Serverless, Free Tier. [See Pricing](https://azure.microsoft.com/en-us/pricing/details/monitor/)
- Azure Container Apps - Severless, Free Tier. [See Pricing](https://azure.microsoft.com/en-us/pricing/details/container-apps/)


## Security Guidelines

This template uses [Managed Identity](https://learn.microsoft.com/entra/identity/managed-identities-azure-resources/overview) for authentication with key Azure services including Azure OpenAI, Azure AI Search, and Azure Cosmos DB. Applications can use managed identities to obtain Microsoft Entra tokens without having to manage any credentials. This also removes the need for developers to manage these credentials themselves and reduces their complexity.

Additionally, we have added a [GitHub Action tool](https://github.com/microsoft/security-devops-action) that scans the infrastructure-as-code files and generates a report containing any detected issues. To ensure best practices we recommend anyone creating solutions based on our templates ensure that the [Github secret scanning](https://docs.github.com/code-security/secret-scanning/about-secret-scanning) setting is enabled in your repo.

## Resources

1. [Prompty Documentation](https://prompty.ai)
1. [Azure AI Studio Documentation](https://aka.ms/aistudio)
1. [Azure AI Templates with Azure Developer CLI](https://aka.ms/ai-studio/azd-templates)


## Code of Conduct

This project has adopted the [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/). Learn more here:

- [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/)
- [Microsoft Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/)
- Contact [opencode@microsoft.com](mailto:opencode@microsoft.com) with questions or concerns

For more information see the [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) or
contact [opencode@microsoft.com](mailto:opencode@microsoft.com) with any additional questions or comments.

## Responsible AI Guidelines

This project follows below responsible AI guidelines and best practices, please review them before using this project:

- [Microsoft Responsible AI Guidelines](https://www.microsoft.com/en-us/ai/responsible-ai)
- [Responsible AI practices for Azure OpenAI models](https://learn.microsoft.com/en-us/legal/cognitive-services/openai/overview)
- [Safety evaluations transparency notes](https://learn.microsoft.com/en-us/azure/ai-studio/concepts/safety-evaluations-transparency-note)

---




