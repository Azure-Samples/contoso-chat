# End to End LLM App development with Azure AI Studio and Prompt Flow

> [!WARNING]  
> This is a special branch of the Contoso Chat repository setup for use with Lab322 at Microsoft Build 2024. It is a simplified branch of the _Contoso Chat v1_ implementation that was used on the Microsoft AI Tour. This version does **not** contain the latest features and capabilities showcased _Contoso Chat v2_ sample (namely: azd, prompty and flex-flow). Instead, this version aims at giving learners a hands-on look at _standard flows_ (using directed acyclic graphs (DAG) and .jnja templates) with the _pf_ command-line tool and _Promptflow_ Visual Studio Code extension.

---

**Table Of Contents**

## 1. Azure Provisioning

1. Log into Azure: `az login --use-device-code`
1. Set Azure Subscription: `az account set --subscription <name or id>`
1. Change to the provisioning directory: `cd provision-v1`
1. Run provisioning script: `sh provision.sh` (based on azure.yaml, infra/)

### 1.1 Validate Provisioning
> This should complete provisioning a resource group called **contoso-chat-rg** with these 10 resources. Note that the specific names don't matter (the table provides enough of a prefix to identify it) - just validate that you have the **type** of resource created.

| Resource Type | Name | Description |
|:---|:---|:---|
| Container registry  | _acrcontoso......._ | Build, store and manage container images |
| Application insights | _appi-contoso......._ | Monitor application health & performance |
| Log Analytics workspace | _apws-contoso......._ | Log data from Azure Monitor and other sources |
| Azure AI hub | _contoso-chat-sf-ai_|Top-level Azure resource for managing AI project access & billing|
| Azure AI project | _contoso-chat-sf-aiproj_ | Organize work for AI projects to support orchestration and save state |
| Azure Cosmos DB account | _cosmos-contoso......_ | Fully-managed NoSQL database for customer orders data |
| Key vault| _kv-contoso......._| Cloud service for secure storage of keys, secrets etc.|
| Azure AI service| _oai-contoso......._ | Market-ready AI services for customization (here: Azure OpenAI) |
| Search service |_search-contoso......._ | Information retrieval service for vector search in generative AI context |
| Storage account | _stcontoso......._ | Storage for data objects (blobs, files, queues, tables etc.) |
| | | |

Once the provisioning step is over, the script also does two _post-provisioning_ actions.
1. It creates a `.env` file in your local folder with the required environment variables from Azure.
1. It downloads the `config.json` file associated with your Azure AI project (Azure ML workspace)

The second is required to provide the Azure SDK (Python) with the required information _("subscription_id","workspace_name", "resource_group") for _configuring local clients_ for code-first interactions with our Azure backend. Some of the actions we need to take are: 
- Upload product data to the Azure AI Search service to create an index.
- Upload customer purchase data to the Azure Cosmos DB service to create a lookup database.
- Setup required promptflow connections to relevant Azure services, for orchestration of chat AI workflow.

Let's look at the first two steps in this section since they impact the Azure backend.

### 1.2 Populate Customer Database

### 1.3 Populate Search Index

<br/>

## 2. Local Env Setup

### 2.1 Explore `pf` tool

### 2.2 Explore `Promptflow` extension

### 2.3 Create `pf` connections to Azure

<br/>

## 3. Build Prompt Flow

<br/>

## 4. Evaluate Prompt Flow

<br/>

## 5. Deploy Prompt Flow

<br/>

## 6. What's Next?

<br/>

---

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
