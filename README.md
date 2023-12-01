# End to End LLM App development with Azure AI Studio and Prompt Flow

### Prerequisites

- Signup for an [Azure Subscription](https://azure.microsoft.com/free/)
- Download [VS Code](https://code.visualstudio.com/download)
- Create [AI Studio Resource](https://learn.microsoft.com/azure/ai-studio/how-to/create-azure-ai-resource)
- Create an [AI Studio Project](https://learn.microsoft.com/azure/ai-studio/how-to/create-projects)

## Setup the code and environment

### Clone the repo

```bash
git clone https://github.com/azure/contoso-chat
```

### Open the repo in VS Code

```bash
cd contoso-chat
code .
```

### Install the [Prompt Flow Extension](https://marketplace.visualstudio.com/items?itemName=prompt-flow.prompt-flow)

- Open the VS Code Extensions tab
- Search for "Prompt Flow"
- Install the extension

### Create a new local python environment
- [anaconda](https://www.anaconda.com/products/individual) or [venv](https://docs.python.org/3/library/venv.html) to manage python environments.

#### Using anaconda

```bash
conda create -n contoso-chat python=3.9
conda activate contoso-chat
pip install -r requirements.txt
```

#### Using venv

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```
### Create the prompt flow runtime

Follow the instructions and steps in the notebook `create-runtime.ipynb` under the `runtime` folder.

### Create data resources to be used in the prompt flow (TODO- finish this)

- Azure AI Search - [Create an Azure Cognitive Search service](https://docs.microsoft.com/en-us/azure/search/search-create-service-portal)


- Azure Open AI Connection - [Create an Azure Open AI Connection](https://learn.microsoft.com/en-us/azure/ai-services/openai/how-to/create-resource?pivots=web-portal)

- Azure Cosmos DB - [Create an Azure Cosmos DB](https://docs.microsoft.com/en-us/azure/cosmos-db/create-cosmosdb-resources-portal)

### Setup the Connections (TODO - Update this)
To run the prompt flow, the connections need to be set up. These can be setup as local connections or with the json confirguration connected to your workspace.

 - To setup local connections follow the instructions [here](https://microsoft.github.io/promptflow/how-to-guides/manage-connections.html)
 - To setup json connection follow the insturctions [here](https://microsoft.github.io/promptflow/cloud/azureai/consume-connections-from-azure-ai.html)

## Building a Prompt flow (TODO)

Now that the environment, extensions, and connections have been installed we can open up the prompt flow and take a look at what it does.

- Click on the flow.dag.yaml file in the explorer. If everything was installed and the python environment was activated you should see the following and select `visual editor` to view the propmt flow:


## Evaluating prompt flow results

Once the prompt flow is setup and working, its time to test it and evaluate the results. To do this we have included some evaluation prompt flows in this project that will use GPT-4 to test the prompt flow.

Follow the instructions and steps in the notebook `evaluate-prompt-flow.ipynb` under the `eval` folder.



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
