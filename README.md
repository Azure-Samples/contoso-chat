# End to End LLM App development with Azure AI Studio and Prompt Flow

## Prerequisites

- Signup for an [Azure Subscription](https://azure.microsoft.com/free/)
- Download [VS Code](https://code.visualstudio.com/download)

## Setup the code and environment

To setup the development environment you can leverage either GitHub Codespaces, a local Python environment (using Anaconda or venv), or a VS Code Dev Container environment (using Docker).

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

#### 3. Install required tools

1. Install the [Prompt Flow Extension](https://marketplace.visualstudio.com/items?itemName=prompt-flow.prompt-flow):

- Open the VS Code Extensions tab
- Search for "Prompt Flow"
- Install the extension

2. Install the [Azure CLI](https://learn.microsoft.com/cli/azure/install-azure-cli)

#### 4. Create a new local Python environment

Follow steps below for using either [anaconda](https://www.anaconda.com/products/individual) or [venv](https://docs.python.org/3/library/venv.html) to manage Python environments.

##### Using anaconda

```bash
conda create -n contoso-chat python=3.11
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

For GitHub Codespaces, click on the green `Code` button on the repository and select the `Codespaces` tab. Click `Create codespace...` to open the project in a Codespace container. This will automatically install all the dependencies and setup the environment.

Proceed with the "Create Azure resources" step below.

### Local Dev Container development Option

If you're using Visual Studio Code and **Dev Container**, clone the project, open it with `code .` or as folder. VS Code will detect the devcontainer configuration and ask you to reopen the project in a container. Alternatively you will need to run this step manually. See the [Dev Containers Extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers) for more information.

Proceed with the "Create Azure resources" step below.

## Create Azure resources

1. Use command `az login` to sign into the Azure Command Line SDK. If you're inside a dev container or Codespace, you may need to run `az login --use-device-code` instead.
2. Run the following command to create the Azure resources:

  ```bash
  ./provision.sh
  ```

  That script will create a resource group, Azure AI Search service, Azure OpenAI service with 3 model deployments, Azure Cosmos DB, and Azure AI Hub and Project. It will also create a `.env` file with the connection information for those resources, and a `config.json` file with the Azure AI Project information.
3. Create an Azure ML connection for Cosmos.
    1. Visit https://ml.azure.com
    2. Under Recent Workspaces, click project (contoso-chat-aiproj)
    3. Select Prompt flow (sidebar), then Connections (tab)
    4. Click Create and select Custom from dropdown
      * Name: contoso-cosmos
      * Provider: Custom (default)
      * Key-value pairs: Add 4 entries (get env var values from .env)
      * key: key, value: "COSMOS_KEY", check "is secret"
      * key: endpoint , value: "COSMOS_ENDPOINT"
      * key: containerId, value: customers
      * key: databaseId, value: contoso-outdoor
    5. Click Save to complete step.


## Populate with sample data

1. To create the search index and populate with sample data, run the code in the `data/product_info/create-azure-search.ipynb` notebook.
2. To create the database container and populate with sample data, run the code in the `data/customer_info/create-cosmos-db.ipynb` notebook. 
3.  To simplify the local PromptFlow connection creation, run the code in the `connections/create-connections.ipynb` notebook. This notebook will create local connections using the same name as the provisioned AI project connections. If you prefer to create the connection mannually, [follow the instructions here](https://microsoft.github.io/promptflow/how-to-guides/manage-connections.html).

## Building a prompt flow

Now that the environment, resources and connections have been configured, we can open up the prompt flow and take a look at how it works. 

### 1. Open the prompt flow in VS Code and understand the steps

The prompt flow is a DAG (directed acyclic graph) that is made up of nodes that are connected together to form a flow. Each node in the flow is a python function tool that can be edited and customized to fit your needs. 

Click on the `contoso-chat/flow.dag.yaml` file in the explorer. If everything was installed and the python environment was activated you should see the following. Select `visual editor` to view the prompt flow:

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

## Deployment with SDK

Now that you have validated and corrected any issues with the prompt flow performance. Its time to push the solution to the cloud and deploy.

Follow the instructions and steps in the notebook `push_and_deploy_pf.ipynb` under the `deployment` folder.

## Deploy with GitHub Actions

### 1. Create Connection to Azure in GitHub
- Login to [Azure Shell](https://shell.azure.com/)
- Follow the instructions to [create a service principal here](hhttps://github.com/microsoft/llmops-promptflow-template/blob/main/docs/github_workflows_how_to_setup.md#create-azure-service-principal)
- Follow the [instructions in steps 1 - 8  here](https://github.com/microsoft/llmops-promptflow-template/blob/main/docs/github_workflows_how_to_setup.md#steps) to add create and add the user-assigned managed identity to the subscription and workspace.

- Assign `Data Science Role` and the `Azure Machine Learning Workspace Connection Secrets Reader` to the service principal. Complete this step in the portal under the IAM.
- Setup authentication with Github [here](https://github.com/microsoft/llmops-promptflow-template/blob/main/docs/github_workflows_how_to_setup.md#set-up-authentication-with-azure-and-github)

```bash
{
  "clientId": <GUID>,
  "clientSecret": <GUID>,
  "subscriptionId": <GUID>,
  "tenantId": <GUID>
}
```
- Add `SUBSCRIPTION` (this is the subscription) , `GROUP` (this is the resource group name), `WORKSPACE` (this is the project name), and `KEY_VAULT_NAME` to GitHub.

### 2. Create a custom environment for endpoint
- Follow the instructions to create a custom env with the packages needed [here](https://learn.microsoft.com/en-us/azure/machine-learning/how-to-manage-environments-in-studio?view=azureml-api-2#create-an-environment)
  - Select the `upload existing docker` option 
  - Upload from the folder `runtime\docker`

- Update the deployment.yml image to the newly created environemnt. You can find the name under `Azure container registry` in the environment details page.

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
