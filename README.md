---
name: Contoso Retail copilot with Azure AI 
description: Build, evaluate and deploy a RAG-based retail copilot with promptflow on Azure AI
languages:
- python
- bicep
- azdeveloper
products:
- azure-openai
- azure-cognitive-search
- azure
- azure-cosmos-db
page_type: sample
urlFragment: contoso-chat
---
 
# Contoso Retail copilot with Azure AI

In this sample we build, evaluate and deploy a support chat agent for Contoso Outdoors, a fictitious retailer who sells hiking and camping equipment. The implementation uses a Retrieval Augmented Generation approach to answer customer queries with responses grounded in the company's product catalog and customer purchase history.

# Contoso Retail copilot with Azure AI

This sample uses the [**Azure AI Search**](https://learn.microsoft.com/azure/search/) service to store product indexes, and the [**Azure Cosmos DB**](https://learn.microsoft.com/azure/cosmos-db/) service to store customer history data. It uses the [**Azure OpenAI**](https://learn.microsoft.com/azure/ai-services/openai/) service to vectorize the user query (with **`text-embeddings-ada-002`**), conduct AI-assisted evaluation (with **`gpt-4`**) and generate the chat response (with **`gpt-35-turbo`**).
 
The Contoso Chat application teaches you how to:

* Build a retail copilot application _using the RAG pattern_.
* Ideate & iterate on application _using the Promptflow framework_.
* Build & manage the solution _using the Azure AI platform & tools_.
* Provision & deploy the solution _using the Azure Developer CLI_.
* Support Responsible AI practices _with evaluation & content safety_.

Once deployed, you can integrate the chat AI (backend) with a chat UI (frontend) as shown, to deliver the retail copilot experience. To get more details on the applications scenario, architecture, codebase, and developer workflow, check out the [documentation](docs/README.md) section of this repo.

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

![Architecture Digram](docs\img\architecture-diagram-contoso-retail.png)

### Demo Video (optional)

 🚧 Embed Advocacy generated video here
 
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