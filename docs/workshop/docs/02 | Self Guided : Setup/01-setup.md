# 1️⃣ | Getting Started

These are the instructions for **Self Guided** learners for this workshop. By the end of this section, you should have provisioned your Azure infrastructure yourself, and validated your local development environment in GitHub Codespaces.

!!! info "First → Review [ 0️⃣ | Pre-requisites](./../00%20|%20Before%20You%20Begin/index.md) before you begin setup"


## 1. Setup Dev Environment

The workshop requires a laptop with a modern browser installed. All steps happen in the browser, using GitHub Codespaces to connect to a development container in the cloud. 

!!! tip "TIP: USE PRIVATE OR INCOGNITO MODE IN BROWSER"

      You may have an enterprise Azure or GitHub account that you are logged into, for work. To avoid conflicts for this workshop, we recommend opening a new browser window in incognito mode (private mode) for this workshop. Any modern browser will do - we recommend Microsoft Edge and using _Tab Groups_ to organize your work for clarity.
      
_In this section, you will create a copy of the repository in your profile and use it for exploration. Then GitHub Codespaces to get a pre-built development environment ready to go._

??? note "Step 0: Launch Browser, Fork Sample in tab 1️⃣ "

    1. Open a browser tab 1️⃣ 
    1. Navigate to ([Contoso Chat](https://aka.ms/aitour/contoso-chat)) sample
    1. Log into GitHub - use a personan login for optimal experience
    1. Fork the sample to your profile - uncheck `main` to get branches
    1. Verify that your fork has all branches - including `aitour-WRK550`
    1. ✅ | You forked the sample successfully!


??? note "Step 1: Launch GitHub Codespaces in tab 2️⃣"

    1. Switch to `aitour-WRK550` branch in your fork - click the **Code** button
    1. Select `Codespaces` tab - click `Create new codespaces on aitour-WRK550`
    1. This will launch Codespaces in a new browser tab - let's call it tab 2️⃣,
    1. Verify that the tab shows a Visual Studio Code editor instance
    1. GitHub Codespaces is loading .. this takes a few minutes so let's move on.
    1. ✅ | Your Codespaces tab is live!


??? note "Step 2: View Azure Portal in tab 3️⃣"

    1. Open new browser tab 3️⃣
    1. Navigate to the [Azure Portal](https://portal.azure.com)
    1. Login with **your Azure username and password**
    1. Click on `Resource Groups` - leave this page open and move on.
    1. ✅ | Your Azure Portal tab is live!

??? note "Step 4: View Azure AI Studio in tab 4️⃣"

    1. Open new browser tab 4️⃣
    1. Navigate to the [Azure AI Studio](https://ai.azure.com)
    1. Click `Sign in` - should auto-login with prior Azure credentials
    1. Click `All resources`  - leave this page open and move on.
    1. ✅ | Your Azure AI Project tab is live!

??? note "Step 5: Authenticate with Azure from tab 2️⃣"

    1. Return to GitHub Codespaces tab 2️⃣
    1. Verify that VS Code is ready - you see a terminal with active cursor
    1. Authenticate with Azure CLI
        - run: `az login --use-device-code` 
        - follow instructions and complete auth workflow (in a new tab)
        - select the valid Azure subscription and tenant to use
        - dismiss this tab and return to tab 2️⃣
        - ✅ | You are logged into Azure CLI
    1. Authenticate with Azure Developer CLI
        - run: `azd auth login`
        - follow instructions and complete auth workflow (in a new tab)
        - dismiss this tab and return to tab 2️⃣
        - You should see: "Logged in to Azure"
        - ✅ | You are logged into Azure Developer CLI

## 2. Provision Azure Infrastructure

??? note "Step 6: Provision infra with `azd` in tab 2️⃣"
    1. Stay in tab 2️⃣ - enter `azd up` and follow prompts
        1. Enter a new environment name - use `AITOUR`
        1. Select a subscription - pick the same one from step 5.
        1. Select a location - pick `francecentral` (or `swedencentral`)
        1. You should see: _"You can view detailed progress in the Azure Portal ..."_
    1. Provisioning takes a while to complete - let's track status next.
    1. ✅ | Your Azure infra is currently being provisioned..

??? note "Step 7: Track provisioning status in tab 3️⃣"
    1. Switch to the Azure Portal in tab 3️⃣
    1. Click on Resource Groups - see: `rg-AITOUR`
    1. Click on `rg-AITOUR` - see `Deployments` under **Essentials**
    1. Click `Deployments` - see Deployments page with activity and status ...
    1. Wait till all deployments complete - **this can take 20-25 minutes**
    1. See `Overview` page - **you should have 35 Deployment Items**
    1. See `Overview` page - **you should have 15 Deployed Resources**
    1. Return to tab 2️⃣ and look at terminal - you should see:
        1. **SUCCESS: Your up workflow to provision and deploy to Azure completed in XX minutes YY seconds.**
    1. ✅ | Your Azure infra is ready!

The last step provisions the Azure infrastructure **and** deploys the first version of your application. 

---

!!! info "Next → 2️⃣ [Validate Setup](./02-validate.md) before you begin building"
