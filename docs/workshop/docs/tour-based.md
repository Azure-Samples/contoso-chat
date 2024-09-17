# Tour-Based Edition

The [Microsoft AI Tour](https://aka.ms/aitour) edition is meant to be used with the instructor-led **WRK550** workshops run using the Skillable lab platform. This version is designed for a **75 minute** in-venue session and provides you with an Azure subscription that is **pre-provisioned** with required resources. Just bring your own laptop (and charger) and dive in!

---


## 1. Getting Started

_Let's organize our development environment and get setup for the workshop._

??? note "Step 1: Launch Skillable"

    1. Open a new browser window
    1. Navigate to Skillable Lab (`link`) = Tab 1️⃣
    1. Click `Launch` - opens window with Login, Instructions = Tab 2️⃣
    1. Click `Resources` tab - find admin `Password`
    1. Click to fill password for login - confirm
    1. You should see: Windows 11 Desktop ✅
    1. Revisit `Resources` tab - look for `Azure Portal` section
    1. Verify `Subscription`, `Username`, `Password` assigned ✅

    **🌟 | CONGRATULATIONS!** - Your Skillable setup is ready.

??? note "Step 2: Launch GitHub Codespaces"

    1. Open a new browser tab = Tab 3️⃣
    1. Navigate to the workshop sample ([Contoso Chat](https://aka.ms/aitour/contoso-chat)) 
    1. Log into GitHub - use a personal login account
    1. Fork this sample to your profile - uncheck `main` to get branches
    1. Switch to `aitour-2025` branch in your fork
    1. Click green `Code` button, select `Codespaces` tab
    1. Click `Create new codespaces on aitour-fy25`
    1. This should launch a new browser tab = Tab 4️⃣
    1. Verify the new tab shows a VS Code editor ✅
    1. Codespaces is loading ... this take a while

    **🌟 | CONGRATULATIONS!** - Your Codespaces is running

??? note "Step 3: View Azure Portal"

    1. Open a new browser tab = Tab 5️⃣
    1. Navigate to the [Azure Portal](https://portal.azure.com)
    1. Sign in with Skillable `Username`-`Password` from Step 1.
    1. Click `Resource Groups` - refresh periodically if needed
    1. See: resource group `rg-AITOUR` created ✅
    1. Click resource group item - view details page
    1. Click `Deployments` - refresh, check if all `Succeeded` ✅
    1. Click `Overview` - check if `15 resources` created ✅

    **🌟 | CONGRATULATIONS!** - Your Azure Infra is Provisioned!

??? note "Step 4: View Azure AI Studio"

    1. Open a new browser tab = Tab 6️⃣
    1. Navigate to the [Azure AI Studio](https://ai.azure.com)
    1. Click `Sign in` - should auto-login with Azure credentials
    1. Click `All resources` - see: a hub resource listed
    1. Click hub resource - see: a project resource listed
    1. Click project resource, `Settings` - see: 5 connections listed
    1. Verify `aoai-connection` and `search-service-connection` setup ✅
    1. Click `Deployments` tab - see 4 models in each category
    1. Verify `gpt-4`, `gpt-35-turbo`, `text-embedding-ada-002` exist ✅

    **🌟 | CONGRATULATIONS!** - Your Azure AI Project was created!

??? note "Step 5: View Container Apps Endpoint"

    1. Return to Azure Portal = Tab 5️⃣
    1. Visit the `rg-AITOUR` Resource group page
    1. Click the `Container Apps` resource - see details page
    1. Look for `Application Url` - at top right
    1. Click to launch in new tab = Tab 7️⃣
    1. See: page with `Welcome to Container Apps`

    **🌟 | CONGRATULATIONS!** - Your ACA Endpoint is provisioned!


??? tip "This Completes Setup. Let's Review"

    _You should have 7 open tabs as follows_.

    1. Skillable Lab
    2. Skillable VM
    3. GitHub Repo
    4. GitHub Codespaces
    5. Azure Portal
    6. Azure AI Studio
    7. Azure Container Apps.

---

## 2. Setup Local Dev Env

_Let's get back to the GitHub Codespaces tab and configure our Visual Studio Code environment to work with our provisioned Azure backend._


??? note "Step 1: Validate Codespaces Ready"

    1. Return to GitHub Codespaces (tab 4️⃣) 
    1. See: VS Code editor with terminal open
    1. Verify: `Prompty Extension` in sidebar (left, bottom)
    1. Verify: Cursor ready in VS Code terminal (bottom)
    1. Verify Python installed: `python --version` ✅
    1. Verify Azure CLI installed: `az version` ✅
    1. Verify Azure Developer CLI installed: `azd version` ✅
    1. Verify Prompty installed: `prompty --version` ✅
    1. Verify FastAPI installed: `fastapi --version` ✅

??? note "Step 2: Authenticate with Azure via CLIs"

    1. Log into Azure CLI - `az login --use-device-code`
    1. Complete authflow - use default tenant, subscription
    1. You are now logged into Azure CLI ✅
    1. Log into Azure Developer CLI - `azd auth login`
    1. Complete authflow - see: "Logged in to Azure" ✅

??? note "Step 3: Refresh Azure Dev Env in local env"

    1. Run `azd env refresh -e AITOUR` in terminal
    1. Select default subscription
    1. Select `francecentral` as Azure location
    1. See: `SUCCESS: Environment refresh completed`
    1. See: `.azure/AITOUR/.env` created with values  ✅

??? note "Step 4: Run post-provisioning hooks"

    1. Run `azd hooks run postprovision` in terminal
    1. Run `bash infra/hooks/update-roles.sh` in terminal
    1. Run `bash infra/hooks/populate-data.sh` in terminal
    1. This will take a few minutes ....
    1. Builds and deploys container app ..
    1. Sets .env variables 