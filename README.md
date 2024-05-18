---
name: Contoso Chat - RAG-based Retail copilot with Azure Container Apps
description: Build, evaluate, and deploy, a RAG-based retail copilot using Azure AI with Promptflow.
languages:
- python
- bicep
- azdeveloper
- prompty
products:
- azure-openai
- azure-cognitive-search
- azure
- azure-cosmos-db
page_type: sample
urlFragment: contoso-chat
---
 
# Contoso Chat: RAG-based Retail copilot with Azure Container Apps

Contoso Chat is the signature Python sample demonstrating how to build, evaluate, and deploy, a retail copilot application end-to-end with Azure Container Apps using Promptflow (flex-flow) with Prompty assets.

[![Open in GitHub Codespaces](https://img.shields.io/static/v1?style=for-the-badge&label=GitHub+Codespaces&message=Open&color=brightgreen&logo=github)](https://github.com/codespaces/new?hide_repo_select=true&machine=basicLinux32gb&repo=725257907&ref=main&devcontainer_path=.devcontainer%2Fdevcontainer.json&geo=UsEast)
[![Open in Dev Containers](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/azure-samples/contoso-chat)

---

# Table of Contents

- [What is this sample?](#what-is-this-sample)
    - [Version History](#version-history)
    - [Key Features](#key-features)
    - [Architecture Diagram](#architecture-diagram)
- [Getting Started](#getting-started)
  - [1. Prerequisites](#1-prerequisites)
  - [2. Setup Environment](#2-setup-environment)
  - [3. Azure Deployment](#azure-deployment)
  - [4. Local Development](#local-development)
  - [5. Troubleshooting](#troubleshooting)
- [Guidance: Costs](#guidance-costs)
- [Guidance: Security](#guidance-security)
- [Resources](#resources)

# What is this sample?

In this sample we build, evaluate and deploy a support chat agent for Contoso Outdoors, a fictitious retailer who sells hiking and camping equipment. The implementation uses a Retrieval Augmented Generation approach to answer customer queries with responses grounded in the company's product catalog and customer purchase history.

The sample uses the following Azure technologies:
- [Azure AI Search](https://learn.microsoft.com/azure/search/) to create and manage search indexes for product catalog data
- [Azure Cosmos DB](https://learn.microsoft.com/azure/cosmos-db/) to store and manage customer purchase history data
- [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/) to deploy and manage key models for our copilot workflow
    - `text-embeddings-ada-002` for vectorizing user queries
    - `gpt-4` for AI-assisted evaluation
    - `gpt-35-turbo` for generating chat responses

By exploring and deploying this sample, you will learn to:
- Build a retail copilot application using the _RAG pattern_.
- Define and engineer prompts using the _Prompty_ asset.
- Design, run & evaluate a copilot using the _Promptflow_ framework.
- Provision and deploy the solution to Azure using the _Azure Developer CLI_.
- Explore and understand Responsible AI practices for _evaluation and content safety._

## Version History

This is the signature sample for showcasing end-to-end development of a copilot application **code-first** on the Azure AI platform and has been actively used for training developer audiences and partners at signature events including [Microsoft AI Tour](https://aka.ms/msaitour) and [Microsoft Build](https://aka.ms/msbuild). This section maintains links to prior versions associated with the relevant events and workshops for reference.

> | Version | Description |
> |:---|:---|
> | v0 : [#cc2e808](https://github.com/Azure-Samples/contoso-chat/tree/cc2e808eee29768093866cf77a16e8867adbaa9c) | Microsoft AI Tour 2023-24 (dag-flow, jnja template) - Skillable Lab |
> | v1 : [msbuild-lab322](https://github.com/Azure-Samples/contoso-chat/tree/msbuild-lab322) | Microsoft Build 2024 (dag-flow, jnja template) - Skillable Lab |
> | v2 : [main](https://github.com/Azure-Samples/contoso-chat) | Latest version (flex-flow, prompty asset)- Azure AI Template |
> | | |

This sample builds the _chat AI_ (copilot backend) that can be deployed to Azure Container Apps as a hosted API (endpoint) for integrations with front-end applications. For **demonstration purposes only**, the _chat UI_ (retail front-end website) was prototyped in a second sample: [contoso-web](https://github.com/Azure-Samples/contoso-web) that provides the user experience shown below. Revisit this section for future updates on chat-UI samples that are Azure AI template ready for convenience.

![Image shows a retailer website with backpacks - and a chat session with a customer](./docs/img/00-app-scenario-ai.png)

## Key Features

The project comes with:
* **Sample model configurations, chat and evaluation prompts** for a RAG-based copilot app.
* **Prompty assets** to simplify prompt creation & iteration for this copilot scenario.
* Sample **product and customer data** for the retail copilot scenario.
* Sample **application code** for copilot chat and evaluation workflows.
* Sample **azd-template configuration** for managing the application on Azure.
* **Managed Identity** configuration as a best practice for managing sensitive credentials.

This is also a **signature sample** for demonstrating the end-to-end capabilities of the Azure AI platform. Expect regular updates to showcase cutting-edge features and best practices for generative AI development. 

 
## Architecture Diagram

The Contoso Chat application implements a _retrieval augmented generation_ pattern to ground the model responses in your data. The architecture diagram below illustrates the key components and services used for implementation and highlights the use of [Azure Managed Identity](https://learn.microsoft.com/entra/identity/managed-identities-azure-resources/) to reduce developer complexity in managing sensitive credentials.

![Architecture Diagram](./docs/img/aca.png)

 
# Getting Started

## 1. Pre-Requisites

- **Azure Subscription** - [Signup for a free account here.](https://azure.microsoft.com/free/)
- **Visual Studio Code** - [Download it for free here.](https://code.visualstudio.com/download)
- **GitHub Account** - [Signup for a free account here.](https://github.com/signup)
- **Access to Azure Open AI Services** - [Apply for access here.](https://learn.microsoft.com/legal/cognitive-services/openai/limited-access)

You will also need to validate the following requirements:
 - Access to [semantic ranker feature](https://azure.microsoft.com/explore/global-infrastructure/products-by-region/?products=search) for your search service tier and deployment region.
 - Access to [sufficient Azure OpenAI quota](https://learn.microsoft.com/azure/ai-services/openai/quotas-limits) for your selected models and deployment region.

 > ![!Note]
 > In this template, we have _pre-configured_ Azure AI Search for deployment in `eastus`, while all other resources get deployed to the default `location` specified during the _azd-driven_ deployment. This is primarily due to the limited regional availability of the _semantic ranker_ feature at present. By using a default location for the search resource, we can now be more flexible in selecting the location for deploying other resources (e.g., to suit your model quota availability).
 
## 2. Setup Environment

You have three options for getting started with this template:
 - **GitHub Codespaces** - Cloud-hosted dev container (pre-built environment)
 - **VS Code Dev Containers** - Locally-hosted dev container (pre-built environment)
 - **Manual Setup** - Local environment setup (for advanced users)

We recommend the first option for the quickest start with minimal effort required. The last option requires the most user effort offers maximum control over your setup. All three options are documented below - **pick one**. 

Once you complete setup, use these commands to validate the install:


### 2.1 Using GitHub Codespaces

 1. Click the button to launch this repository in GitHub Codespaces.
  
    [![Open in GitHub Codespaces](https://img.shields.io/static/v1?style=for-the-badge&label=GitHub+Codespaces&message=Open&color=brightgreen&logo=github)](https://github.com/codespaces/new?hide_repo_select=true&machine=basicLinux32gb&repo=725257907&ref=main&devcontainer_path=.devcontainer%2Fdevcontainer.json&geo=UsEast)

 1. This should launch a new browser tab for GitHub Codespaces setup. The process may take a few minutes to complete.
 1. Once ready, the tab will refresh to show a Visual Studio Code editor in the browser.
 1. Open the terminal in VS Code and validate install with these commands:
    - `azd version` - Azure Developer CLI is installed (v1.8.2+)
    - `pf version` - Promptflow is installed (v1.10.0+)
    - `az version` - Azure CLI is installed (v2.60+)
    - `python3 --version` - Python3 is installed (v3.11+)
 1. Sign into your Azure account from the VS Code terminal
    ```bash
    azd auth login --use-device-code
    ```
 1. **Congratulations!** You are ready to move to the _Azure Deployment_ step.

### 2.2 Using VS Code Dev Containers

A related option is VS Code Dev Containers, which will open the project in your local VS Code using the [Dev Containers extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers):

1. Start Docker Desktop (install it if not already installed)
1. Open the project by clickjing the button below:

    [![Open in Dev Containers](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/azure-samples/contoso-chat)

 1. Once ready, the tab will refresh to show a Visual Studio Code editor in the browser.
 1. Open the terminal in VS Code and validate install with these commands:
    - `azd version` - Azure Developer CLI is installed (v1.8.2+)
    - `pf version` - Promptflow is installed (v1.10.0+)
    - `az version` - Azure CLI is installed (v2.60+)
    - `python3 --version` - Python3 is installed (v3.11+)
 1. Sign into your Azure account from the VS Code terminal
    ```bash
    azd auth login
    ```
 1. **Congratulations!** You are ready to move to the _Azure Deployment_ step.

### 2.3 Manual Setup (Local Environment)

* Verify you have Python3 installed on your machine.
  * Install dependencies with `pip install -r requirements.txt`
* Install [Azure CLI](https://docs.microsoft.com/cli/azure/install-azure-cli) 
* Install [Azure Developer CLI](https://aka.ms/install-azd)
  * Windows: `winget install microsoft.azd`
  * Linux: `curl -fsSL https://aka.ms/install-azd.sh | bash`
  * MacOS: `brew tap azure/azd && brew install azd`
* Validate install with these commands:
    - `azd version` - Azure Developer CLI is installed (v1.8.2+)
    - `pf version` - Promptflow is installed (v1.10.0+)
    - `az version` - Azure CLI is installed (v2.60+)
    - `python3 --version` - Python3 is installed (v3.11+)

### 3. Azure Deployment

Complete these steps in the same terminal that you used previously, to authenticate with Azure.
 1. Provision Azure resources _and_ deploy your application with one command. The process should ask you for an _environment name_ (maps to resource group) and a _location_ (Azure region) and _subscription_ for deployment.
    ```bash
    azd up
    ```
 1. Verify that your application was provisioned correctly.
    - Visit the [Azure Portal](https://portal.azure.com) and verify the resource group (above) was created.
    - Visit the [Azure Container Apps](https://ai.azure.com/build) site and verify the AI project was created.
  1. **Congratulations!** Your setup step is complete. 
 
### Local Development

The core functionality of the copilot application is developed using the Promptflow framework with Python. In this project, we use the Promptflow extension in Visual Studio Code, with its `pf` commandline tool, for all our local development needs. 

Run this command to get a result locally

```
 pf flow test --flow ./src/contoso_chat --inputs question="tell me about your jackets" customerId="3" chat_history=[]
```

 
## Costs
You can estimate the cost of this project's architecture with [Azure's pricing calculator](https://azure.microsoft.com/pricing/calculator/)

- Azure OpenAI - Standard tier, GPT-4, GPT-35-turbo and Ada models.  [See Pricing](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/)
- Azure AI Search - Basic tier, Semantic Ranker enabled [See Pricing](https://azure.microsoft.com/en-us/pricing/details/search/)
- Azure Cosmos DB for NoSQL - Serverless, Free Tier [See Pricing](https://azure.microsoft.com/en-us/pricing/details/cosmos-db/autoscale-provisioned/#pricing)

## Security Guidelines

We recommend using keyless authentication for this project. Read more about why you should use managed identities on [our blog](https://techcommunity.microsoft.com/t5/microsoft-developer-community/using-keyless-authentication-with-azure-openai/ba-p/4111521).

## Resources
 
- [Azure Container Apps Documentation](https://learn.microsoft.com/azure/ai-studio/)
- [Promptflow Documentation](https://github.com/microsoft/promptflow)
- [Prompty Assets](https://microsoft.github.io/promptflow/how-to-guides/develop-a-prompty/index.html)
- [Flex Flow](https://microsoft.github.io/promptflow/tutorials/flex-flow-quickstart.html)
- [Link to similar sample] 🚧
 
<br/>

## Troubleshooting

Have questions or issues to report? Please [open a new issue](https://github.com/Azure-Samples/contoso-chat/issues) after first verifying that the same question or issue has not already been reported. In the latter case, please add any additional comments you may have, to the existing issue.


## Contributing

This project welcomes contributions and suggestions.  Most contributions require you to agree to a
Contributor License Agreement (CLA) declaring that you have the right to, and actually do, grant us
the rights to use your contribution. For details, visit https://cla.opensource.microsoft.com.

When you submit a pull request, a CLA bot will automatically determine whether you need to provide
a CLA and decorate the PR appropriately (e.g., status check, comment). Simply follow the instructions
provided by the bot. You will only need to do this once across all repos using our CLA.

This project has adopted the [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/).
For more information see the [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) or
contact [opencode@microsoft.com](mailto:opencode@microsoft.com) with any additional questions or comments.

## Trademarks

This project may contain trademarks or logos for projects, products, or services. Authorized use of Microsoft 
trademarks or logos is subject to and must follow 
[Microsoft's Trademark & Brand Guidelines](https://www.microsoft.com/en-us/legal/intellectualproperty/trademarks/usage/general).
Use of Microsoft trademarks or logos in modified versions of this project must not cause confusion or imply Microsoft sponsorship.
Any use of third-party trademarks or logos are subject to those third-party's policies.
