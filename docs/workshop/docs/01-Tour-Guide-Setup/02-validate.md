#  2️⃣ | Validate Setup and Provision

!!! success "Let's Review where we are right now"

    We should have the following windows and tabs open in our device:

    1. Window A = Skillable Lab (starting point)
    2. Window B = Dev Environment (logged in with our Azure credentials)
    3. Tab 1️⃣ = GitHub Repo (starting point)
    4. Tab 2️⃣ = GitHub Codespaces (development environment)
    5. Tab 3️⃣ = Azure Portal (provisioned resources)
    6. Tab 4️⃣ = Azure AI Studio (AI project & models)
    7. Tab 5️⃣ = Azure Container Apps (Deployment target)

_We have our Azure infrastructure resources pre-provisioned, but we need to populate our data and deploy the initial application to Azure. Let's get this done now_.

## 1. Check: Tools Installed

We need specific tools for running, testing & deploying our app. Let's verify we have these installed.

Copy/paste these commands into the VS Code terminal to verify required tools are installed. 

```bash
python --version
```

```bash
az version
```

```bash
azd version
```

```bash
prompty --version
```    

```bash
fastapi --version
```

!!! tip "These tools have been installed into the GitHub CodeSpaces dev container for you. If you want to run this workshop in another environment like your desktop PC, you will have to install them first."

## 2. Authenticate with Azure

To access our Azure resources, we need to be authenticated from VS Code. Let's do that now. Since we'll be using both the `az` and `azd` tools, we'll authenticate in both.

From the VS Code Online Terminal pane (in Tab 2️⃣):

1. Log into the Azure CLI `az` using the command below. 

    ```
    az login --use-device-code
    ```

1. Copy the 8-character code shown to your clipboard, then control-click the link to visit [https://microsoft.com/devicelogin](https://microsoft.com/devicelogin) in a new browser tab.

1. Select the account with the Username shown in the Skillable Lab window. Click "Continue" at the `are you sure?` prompt, and then close the tab

1. Back in the Terminal, press Enter to select the default presented subscription and tenant.

1. You also need to log into the Azure Developer CLI, `azd`. Enter the command below at the terminal, and follow the same process to copy the code, select the account, and close the tab.
```
azd auth login --use-device-code
```
    - You won't need to enter the password again. Simply select your Skillable Lab account.

!!! success "You are now logged into Azure CLI and Azure Developer CLI"

## 3. Configure Azure Env Vars

To build code-first solutions, we will need to use the Azure SDK from our development environment. This requires configuration information for the various resources we've already provisioned for you in the `francecentral` region. Let's retrieve those now.

From the Terminal pane in Tab 2️⃣:

1. Run the commands below

```
azd env set AZURE_LOCATION francecentral -e AITOUR --no-prompt
```
```
azd env refresh -e AITOUR 
```

(Press ENTER to select the default Azure subscription presented). 

The file `.azure/AITOUR/.env` has been updated in our filesystem with information needed to build our app: connection strings, endpoint URLs, resource names and much more. You can open the file to see the values retrieved, or display them with this command:

```
azd env get-values
```

!!! info "No passwords or other secrets are included in the `.env` file. Authentication is controlled using [managed identities](https://learn.microsoft.com/entra/identity/managed-identities-azure-resources/overview) as a security best practice." 


## 4. Populate databases and deploy container app

_We can now use these configured tools and SDK to perform some post-provisioning tasks. This includes populating data in Azure AI Search (product indexes) and Azure Cosmos DB (customer data), and deploying the initial version of our application to Azure Container Apps_.

From the Terminal pane in Tab 2️⃣:

1. Run the command below. (This will take a few minutes to complete.)

    ```
    bash ./docs/workshop/src/0-setup/azd-update-roles.sh
    ```

    !!! info "This updates the security profile for the provisioned Cosmos DB database so you can add data to it. This step isn't needed when you deploy Cosmos DB yourself."

1. Once complete, run the command below:

    ```
    azd hooks run postprovision
    ```

    This command populates Azure Search and Cosmos DB with product and customer data from Contoso Outdoors. It also builds and deploys a shell endpoint to the container app, which we will update in the next section. This will take a few minutes.

    !!! info "If you're curious, the code to populate the databases is found in Python Notebooks in `data` folder of the repository."

1. Refresh the Container App in tab 5️⃣ - it will update to say "Hello world" ✅

---

_We are ready to start the development workflow segment of our workshop. But let's first check that all these setup operations were successful!_.

!!! example "Next → [Let's Explore the App Infrastructure](./../03-Workshop-Build/03-infra.md) before we start building!"
