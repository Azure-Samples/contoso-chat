#  2️⃣ | Validate Setup

!!! success "Let's Review where we are right now"

    We should have the following windows and tabs open in our device:

    1. Window A = Skillable Lab (starting point)
    2. Window B = Skillable VM (with our Azure credentials)
    3. Tab 1️⃣ = GitHub Repo (starting point)
    4. Tab 2️⃣ = GitHub Codespaces (development environment)
    5. Tab 3️⃣ = Azure Portal (provisioned resources)
    6. Tab 4️⃣ = Azure AI Studio (AI project & models)
    7. Tab 5️⃣ = Azure Container Apps (Deployment target)

_We have our Azure infrastructure resources pre-provisioned, but we need to populate our data and deploy the initial application to Azure. Let's get this done_.


## 1. Check: VS Code Ready

_We had left GitHub Codespaces in loading mode - let's verify that loading completed and our Visual Studio Code IDE is ready!_.

??? info "Step 1: Validate Codespaces Ready in 2️⃣"

    1. Return to GitHub Codespaces tab 
    1. See: VS Code editor with terminal open
    1. Verify: `Prompty Extension` in sidebar (left, bottom)
    1. Verify: Cursor ready in VS Code terminal (bottom)


## 2. Check: Tools Installed

_We need specific tools for running, testing & deploying our app. Let's verify we have these installed_.

??? info "Step 2: Verify tools installed in 2️⃣"

    Copy/paste these commands into the VS Code terminal to verify required tools are installed
    
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
    python --version
    ```    
    ```bash
    fastapi --version
    ```


## 3. Authenticate: with Azure

_To access our Azure resources, we need to be authenticated from VS Code. Let's do that now. Since we'll be using both the `az` and `azd` tools, we'll authenticate in both_.

??? info "Step 3: Authenticate with Azure via CLIs in 2️⃣"

    1. Log into Azure CLI - `az login --use-device-code`
    1. Complete authflow - use default tenant, subscription
    1. You are now logged into Azure CLI ✅
    1. Log into Azure Developer CLI - `azd auth login`
    1. Complete authflow - see: "Logged in to Azure" ✅

## 4. Configure Azure Env Vars

_To build code-first solutions, we will need to use the Azure SDK from our development environment. This requires configuration information for the various resources we've provisioned. Let's retrieve those here._

??? info  "Step 4: Refresh Azure Dev Env in local env in 2️⃣"

    1. Run `azd env refresh -e AITOUR` in terminal
    1. Select default subscription
    1. Select `francecentral` as Azure location
    1. See: `SUCCESS: Environment refresh completed`
    1. See: `.azure/AITOUR/.env` created with values  ✅

## 5. Run Postprovision Hooks

_We can now use these configured tools and SDK to perform some post-provisioning tasks. This includes populating data in Azure AI Search (product indexes) and Azure Cosmos DB (customer data), and deploying the initial version of our application to Azure Container Apps_.

??? info  "Step 5: Run post-provisioning hooks in 2️⃣"

    1. Run `bash ./docs/workshop/src/0-setup/azd-update-roles.sh ` in terminal
    1. This will take a few minutes ....
    1. Run `azd hooks run postprovision` in terminal
    1. This will take a few minutes ....
    1. Builds and deploys container app ..
    1. Verify that you see a `.env` file in your repo ✅
    1. Refresh Container App in tab 5️⃣ - verify that you see "Hello world" ✅

---

_We are ready to start the development workflow segment of our workshop. But let's first check that all these setup operations were successful!_.

!!! example "Next → [Let's Validate our Infra](./../03-Workshop-Build/03-infra.md) before we start building!"
