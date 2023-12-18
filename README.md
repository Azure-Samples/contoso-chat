# End to End LLM App development with Azure AI Studio and Prompt Flow

## Prerequisites

- Signup for an [Azure Subscription](https://azure.microsoft.com/free/)
- Download [VS Code](https://code.visualstudio.com/download)
- Install the [Azure CLI](https://learn.microsoft.com/en-us/cli/azure/install-azure-cli) and run `az login` to get token credentials set.
- Create an [AI Studio Resource](https://learn.microsoft.com/azure/ai-studio/how-to/create-azure-ai-resource)
- Create an [AI Studio Project](https://learn.microsoft.com/azure/ai-studio/how-to/create-projects)

## Setup the code and environment

To setup the development environment you can leverage codespaces, a local environment that you configure with Anaconda or venv, or a vs code docker container environment that leverages the Devcontainer.

### Local development environment option (Anaconda or venv)

#### 1. Clone the repo

```bash
git clone https://github.com/azure/contoso-chat
```

#### 2. Open the repo in VS Code

```bash
cd contoso-chat
code .
```

#### 3. Install the [Prompt Flow Extension](https://marketplace.visualstudio.com/items?itemName=prompt-flow.prompt-flow)

- Open the VS Code Extensions tab
- Search for "Prompt Flow"
- Install the extension

#### 4. Create a new local python environment
- [anaconda](https://www.anaconda.com/products/individual) or [venv](https://docs.python.org/3/library/venv.html) to manage python environments.

##### Using anaconda

```bash
conda create -n contoso-chat python=3.9
conda activate contoso-chat
pip install -r requirements.txt
```

##### Using venv

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### Codespaces development option
For codespaces click on the green `code` button on the repository and select the `codespaces` tab. Click `create codespace...` to open the project in a Codespace container. This will automatically install all the dependencies and setup the environment. Proceed with "Create the prompt flow runtime in AI Studio".

### Local Devcontainer development Option
If you're using Visual Studio Code and **Devcontainer**, clone the project, open it with `code .` or as folder. VS Code will detect the devcontainer configuration and ask you to reopen the project in a container. Alternatively you will need to run this step manually. See the [Remote Container Extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers) for more information. Proceed with "Create the prompt flow runtime in AI Studio".

## Create the prompt flow runtime in AI Studio

Follow the instructions and steps in the notebook `create_compute_runtime.ipynb` under the `runtime` folder.

## Create Azure resources and populate with sample data

### 1.  Create Azure Open AI resource and deploy the models 
- Follow these instructions to [create an Azure Open AI resource](https://learn.microsoft.com/en-us/azure/ai-services/openai/how-to/create-resource?pivots=web-portal)
- Populate the `local.env` file with the endpoint and key from the Azure Open AI resource created in the previous step.
- Now that the service is created use Azure AI Studio to deploy the following models to be used in the prompt flow: `GPT-4`, `GPT-3.5 Turbo`, and the embedding model `text-embedding-ada-002`. Follow these instructions to [deploy the models.](https://learn.microsoft.com/en-us/azure/ai-studio/tutorials/deploy-copilot-ai-studio#deploy-a-chat-model)

### 2.  Azure AI Search service named `contoso-search`
- Follow these instructions to [create an Azure AI Search service](https://docs.microsoft.com/en-us/azure/search/search-create-service-portal)
- Populate the `local.env` file with the endpoint and key from the Azure AI Search service created in the previous step.
- Now that the resource is created in Azure, use the notebook code and instructions `create-azure-search.ipynb` under the `data\product_info` folder to create the index and populate with the sample data

### 3.  Create and populate the Azure Cosmos DB customer database 
- Follow these instructions to create the resource: [Create an Azure Cosmos DB](https://docs.microsoft.com/en-us/azure/cosmos-db/create-cosmosdb-resources-portal)
- Populate the `local.env` file with the endpoint and key from the Azure Cosmos DB resource created in the previous step.
- Now that the resource is created in Azure, use the notebook code and instructions `create-cosmos-db.ipynb` under the `data\customer_info` folder to create the database, container and populate with the sample data.

## Setup the connections locally and in Azure AI Studio
To run the prompt flow, the connections need to be set up both locally and in the Azure AI Studio. When setting up the connections in the Azure AI Studio, make sure to use the same names as the local connections. Follow the instructions below to setup the connections.

### 1. Create the cloud connections in Azure AI Studio
- Create the Azure AI Search connection named `contoso-search`. [Follow the instructions here to setup the Azure AI Search connection](https://learn.microsoft.com/en-us/azure/ai-studio/how-to/connections-add?tabs=azure-ai-search#create-a-new-connection)

- Create Cosmos DB Custom connection named `contoso-cosmos`. [Follow the instructions here to create the Custom connection to Cosmos DB](https://learn.microsoft.com/en-us/azure/ai-studio/how-to/connections-add?tabs=custom#connection-details). NOTE: Be sure to add all the key value pairs needed in this connection: `endpoint`, `key`, `databaseId`, `containerId`.

- Create Azure Open AI connection named `aoai-connection`. [Follow the instructions here to setup the Azure Open AI connection](https://learn.microsoft.com/en-us/azure/ai-studio/how-to/connections-add?tabs=azure-openai#create-a-new-connection)

### 2. Create the local connections
To simplify the local connection creation use the notebook `create-connections.ipynb` under the `connections` folder. This notebook will create the local connections with the naming above. Be sure to update the endpoints and keys in the notebook to create the connections to the resources created in Azure. If you prefer to create the connection mannually, [follow the instructions here](https://microsoft.github.io/promptflow/how-to-guides/manage-connections.html).

## Building a prompt flow

Now that the environment, resources and connections have been configured we can open up the prompt flow and take a look at how it works. 

### 1. Open the prompt flow in VS Code and understand the steps
The prompt flow is a DAG (directed acyclic graph) that is made up of nodes that are connected together to form a flow. Each node in the flow is a python function tool that can be edited and customized to fit your needs. 

Click on the `flow.dag.yaml` file in the explorer. If everything was installed and the python environment was activated you should see the following and select `visual editor` to view the prompt flow:

![Visual editor button](./images/visualeditorbutton.png)

This will open up the prompt flow in the visual editor.

![Alt text](./images/promptflow.png)

The prompt flow is made up of the following nodes:

- *input*s - This node is used to start the flow and is the entry point for the flow. It has the input parameters `customer_id` and `question`, and `chat_history`. The `customer_id` is used to lookup the customer information in the Cosmos DB. The `question` is the question the customer is asking. The `chat_history` is the chat history of the conversation with the customer.

- *question_embedding* - This node is used to embed the question text using the `text-embedding-ada-002` model. The embedding is used to find the most relevant documents from the AI Search index.

- *retrieve_documents* - This node is used to retrieve the most relevant documents from the AI Search index with the question vector.

- *customer_lookup* - This node is used to get the customer information from the Cosmos DB.

- *customer_prompt* - This node is used to generate the prompt with the information retrieved and added to the `customer_prompt.jinja2` template.

- *llm_response* - This node is used to generate the response to the customer using the `GPT-35-Turbo` model.

- *outputs* - This node is used to end the flow and return the response to the customer.

### 2. Run the prompt flow

Now that we have the prompt flow open in the visual editor, we can run the flow and see the results. To run the flow, click on the `Run` play button at the top. For more details on running the prompt flow, [follow the instructions here](https://microsoft.github.io/promptflow/how-to-guides/init-and-test-a-flow.html#test-a-flow).

## Evaluating prompt flow results

Once the prompt flow is setup and working, its time to test it and evaluate the results. To do this we have included some evaluation prompt flows in this project that will use GPT-4 to test the prompt flow.

Follow the instructions and steps in the notebook `evaluate-chat-prompt-flow.ipynb` under the `eval` folder.

## Deployment

Now that you have validated and corrected any issues with the prompt flow performance. Its time to push the solution to the cloud and deploy.

Follow the instructions and steps in the notebook `push_and_deploy_pf.ipynb` under the `deployment` folder.




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
