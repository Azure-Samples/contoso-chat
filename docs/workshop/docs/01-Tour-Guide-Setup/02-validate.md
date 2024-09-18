#  2️⃣ | Validate Setup

!!! info "Let's Review: We should have these tabs open in browser"

    1. Tab A = Skillable Lab 
    2. Tab B = Skillable VM
    3. Tab 1️⃣ = GitHub Repo
    4. Tab 2️⃣ = GitHub Codespaces
    5. Tab 3️⃣ = Azure Portal
    6. Tab 4️⃣ = Azure AI Studio
    7. Tab 5️⃣ = Azure Container Apps.

_In this section we'll authenticate with Azure from our GitHub Codespaces environment, and do some post-provisioning steps to get us ready for development_.


## On GitHub Codespaces

Lets authenticate with Azure and configure local development environment to use  infrastructure.


??? note "Step 1: Validate Codespaces Ready in 2️⃣"

    1. Return to GitHub Codespaces tab 
    1. See: VS Code editor with terminal open
    1. Verify: `Prompty Extension` in sidebar (left, bottom)
    1. Verify: Cursor ready in VS Code terminal (bottom)
    1. Verify Python installed: `python --version` ✅
    1. Verify Azure CLI installed: `az version` ✅
    1. Verify Azure Developer CLI installed: `azd version` ✅
    1. Verify Prompty installed: `prompty --version` ✅
    1. Verify FastAPI installed: `fastapi --version` ✅

??? note "Step 2: Authenticate with Azure via CLIs in 2️⃣"

    1. Log into Azure CLI - `az login --use-device-code`
    1. Complete authflow - use default tenant, subscription
    1. You are now logged into Azure CLI ✅
    1. Log into Azure Developer CLI - `azd auth login`
    1. Complete authflow - see: "Logged in to Azure" ✅

??? note "Step 3: Refresh Azure Dev Env in local env in 2️⃣"

    1. Run `azd env refresh -e AITOUR` in terminal
    1. Select default subscription
    1. Select `francecentral` as Azure location
    1. See: `SUCCESS: Environment refresh completed`
    1. See: `.azure/AITOUR/.env` created with values  ✅

??? note "Step 4: Run post-provisioning hooks in 2️⃣"

    1. Run `bash ./docs/workshop/src/0-setup/azd-update-roles.sh ` in terminal
    1. This will take a few minutes ....
    1. Run `azd hooks run postprovision` in terminal
    1. This will take a few minutes ....
    1. Builds and deploys container app ..
    1. Verify that you see a `.env` file in your repo ✅
    1. Refresh Container App in tab 5️⃣ - verify that you see "Hello world" ✅


We completed all the post-provisioning steps and are now ready to get to work.

---

!!! info "Next → 3️⃣ [Validate Infra](./../03-Workshop-Build/03-infra.md) before we start building!
