---
name: Contoso Chat - RAG-based Retail copilot with Azure AI Studio
description: Use Azure AI Studio to build, evaluate and deploy, a retail copilot using the Retrieval Augmented Generation (RAG) pattern with Prompflow flex-flow and Prompty assets.
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
 
# Contoso Chat: RAG-based Retail copilot with Azure AI Studio

Contoso Chat is the signature Python sample demonstrating how to build, evaluate, and deploy, a retail copilot application end-to-end with Azure AI Studio using Promptflow with Prompty assets.

[![Open in GitHub Codespaces](https://img.shields.io/static/v1?style=for-the-badge&label=GitHub+Codespaces&message=Open&color=brightgreen&logo=github)](https://github.com/codespaces/new?hide_repo_select=true&machine=basicLinux32gb&repo=725257907&ref=main&devcontainer_path=.devcontainer%2Fdevcontainer.json&geo=UsEast)
[![Open in Dev Containers](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/azure-samples/contoso-chat)

---

# Table of Contents

- [What is this sample?](#what-is-this-sample)
- [Version History](#version-history)
- [Features](#features)
- [Architecture Diagram](#architecture-diagram)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Quickstart](#quickstart)
- [Security Guidelines](#security-guidelines)
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

# Version History

This is the signature sample for showcasing end-to-end development of a copilot application **code-first** on the Azure AI platform and has been actively used for training developer audiences and partners at signature events including [Microsoft AI Tour](https://aka.ms/msaitour) and [Microsoft Build](https://aka.ms/msbuild). This section maintains links to prior versions associated with the relevant events and workshops for reference.

> | Version | Description |
> |:---|:---|
> | v0 : [#cc2e808](https://github.com/Azure-Samples/contoso-chat/tree/cc2e808eee29768093866cf77a16e8867adbaa9c) | Microsoft AI Tour 2023-24 (dag-flow, jnja template) - Skillable Lab |
> | v1 : [msbuild-lab322](https://github.com/Azure-Samples/contoso-chat/tree/msbuild-lab322) | Microsoft Build 2024 (dag-flow, jnja template) - Skillable Lab |
> | v2 : [main](https://github.com/Azure-Samples/contoso-chat) | Latest version (flex-flow, prompty asset)- Azure AI Template |
> | | |

This sample builds the _chat AI_ (copilot backend) that can be deployed to Azure AI Studio as a hosted API (endpoint) for integrations with front-end applications. For **demonstration purposes only**, the _chat UI_ (retail front-end website) was prototyped in a second sample: [contoso-web](https://github.com/Azure-Samples/contoso-web) that provides the user experience shown below. Revisit this section for future updates on chat-UI samples that are Azure AI template ready for convenience.

![Image shows a retailer website with backpacks - and a chat session with a customer](./docs/img/00-app-scenario-ai.png)

## Features

The project comes with:
* Sample _promptflow assets_ for a RAG-based copilot application
* Sample _model configurations_ for a RAG-based copilot application
* Sample _evaluation prompts_ for a RAG-based copilot application
* Sample _product and customer data_ for retail application scenario
* Sample _application code_ for copilot chat and evaluation functions
* Sample _azd-template configuration_ for managing application on Azure

The sample is also a  _signature application_ for demonstrating new the capabilities of the Azure AI platform. Expect regular updates to showcase cutting-edge features and best practices for generative AI development. Planned updates include support for:
* New _flexflow_ implementation (instead of existing `flow.dag.yaml`)
* New _prompty_ assets (to simplify prompt creation & iteration)
* New `azd` _ai.endpoint_ host type (to configure AI deployments in Azure)

 
### Architecture Diagram

![Architecture Digram](docs/img/architecture-diagram-contoso-retail-aistudio.png)

 
## Getting Started

### Pre-Requisites

- **Azure Subscription** - [Signup for a free account.](https://azure.microsoft.com/free/)
- **Visual Studio Code** - [Download it for free.](https://code.visualstudio.com/download)
- **GitHub Account** - [Signup for a free account.](https://github.com/signup)
- **Access to Azure Open AI Services** - [Learn about getting access.](https://learn.microsoft.com/legal/cognitive-services/openai/limited-access)
- **Ability to provision Azure AI Search (Paid)** - Required for Semantic Ranker
- **Ability to deploy these models** - `gpt-35-turbo`, `gpt-4`, `text-embeddings-ada-002`

Note that the Azure AI Search and Azure Open AI services are paid services that may also have regional availability and quota constraints. Check the Azure documentation for more details.
 
### Installation
 
The repository is configured with a `devcontainer.json` that has the required dependencies pre-installed. Use the following commands to verify the install:
 
- `azd version` - Verify Azure Developer CLI is v1.8.2+
- `pf version` - Verify Promptflow is v1.9.0+
- `az version` - Verify Azure CLI is v2.60+.
- `python3 --version` - Verify Python is v3.11+ 

Local development is done using a Python environment (runtime) with the Promptflow extension on VS Code (IDE). No other installs are needed in the pre-built environment. _For other options, check the [documentation](docs/README.md)_.
 
### Quickstart

The quickest way to get started is to use the pre-built dev environment by following these steps:

1. Fork this repo, then launch it in GitHub Codespaces
1. Run `azd auth login` in the VS Code terminal to authenticate with Azure.
1. Run `azd up` to deploy the application to Azure and wait for completion.
1. Launch browser and navigate to `https://ai.azure.com/build`.
1. Look for the recently-created project and explore it!

This process illustrates the ease of provisioning and deploying the completed application to Azure with a single commandline tool. To understand how to _build_ the application from scratch, follow the steps described in the [documentation](docs/README.md) section of this repo.

 
### Local Development

The core functionality of the copilot application is developed using the Promptflow framework with Python. In this project, we use the Promptflow extension in Visual Studio Code, with its `pf` commandline tool, for all our local development needs. More details can be found in the [documentation](docs/README.md) section of this repo.
 
## Costs
You can estimate the cost of this project's architecture with [Azure's pricing calculator](https://azure.microsoft.com/pricing/calculator/)

- Azure OpenAI - Standard tier, GPT-4, GPT-35-turbo and Ada models.  [See Pricing](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/)
- Azure AI Search - Basic tier, Semantic Ranker enabled [See Pricing](https://azure.microsoft.com/en-us/pricing/details/search/)
- Azure Cosmos DB for NoSQL - Serverless, Free Tier [See Pricing](https://azure.microsoft.com/en-us/pricing/details/cosmos-db/autoscale-provisioned/#pricing)

## Security Guidelines

We recommend using keyless authentication for this project. Read more about why you should use managed identities on [our blog](https://techcommunity.microsoft.com/t5/microsoft-developer-community/using-keyless-authentication-with-azure-openai/ba-p/4111521).

## Resources
 
- [Azure AI Studio Documentation](https://learn.microsoft.com/azure/ai-studio/)
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
