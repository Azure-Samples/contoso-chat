# 1️⃣ | Getting Started

These are the instructions for a **self-guided** tour of the Contoso Chat sample. This version is designed for **self-paced** learning but will require you to bring your own subscription and provision the resources yourself.

!!! warning "PRE-REQUISITES FOR THIS WORKSHOP"

    To participate in this workshop you will need the following:

    1. **Your own laptop.** Should have a modern browser, preferably Microsoft Edge.
    1. **A GitHub account.** A personal account with GitHub Codespaces access.
    1. **An Azure subscription.** With access to Azure OpenAI Model deployments.
    1. **Familiarity with VS Code.** Our default development environment.
    1. **Familiarity with Python**. Our default coding language.

---


## 1. Getting Started

Let's setup our development environment and kickstart the self-deployment process:


??? note "Step 0: Launch Browser, Fork Sample in tab 1️⃣ "

    1. Open a browser tab 1️⃣ 
    1. Navigate to ([Contoso Chat](https://aka.ms/aitour/contoso-chat)) sample
    1. Log into GitHub - use a personan login for optimal experience
    1. Fork the sample to your profile - uncheck `main` to get branches
    1. ✅ | You forked the sample successfully!


??? note "Step 1: Launch GitHub Codespaces in tab 2️⃣"

    1. Switch to `aitour-fy25` branch in your fork - click the **Code** button
    1. Select `Codespaces` tab - click `Create new codespaces on aitour-fy25`
    1. This will launch Codespaces in a new browser tab - tab 2️⃣,
    1. Verify that the tab shows a Visual Studio Code editor
    1. GitHub Codespaces is loading .. this will take a while.
    1. ✅ | Your Codespaces tab is live!


??? note "Step 2: View Azure Portal in tab 3️⃣"

    1. Open new browser tab 2️⃣
    1. Navigate to the [Azure Portal](https://portal.azure.com)
    1. Login with **your Azure username and password**
    1. Click on `Resource Groups` - leave this page open for now.
    1. ✅ | Your Azure Portal tab is live!

??? note "Step 4: View Azure AI Studio in tab 4️⃣"

    1. Open new browser tab 4️⃣
    1. Navigate to the [Azure AI Studio](https://ai.azure.com)
    1. Click `Sign in` - should auto-login with prior Azure credentials
    1. Click `All resources`  - leave this page open for now.
    1. ✅ | Your Azure AI Project tab is live!

??? note "Step 5: Authenticate with Azure from tab 2️⃣"

    1. Return to GitHub Codespaces tab 2️⃣
    1. Verify that terminal is visible - and cursor is ready
    1. Authenticate with Azure CLI
        - `az login --use-device-code`
        -  follow instructions and complete auth workflow
        - select the valid Azure subscription and tenant to use
        - ✅ | You are logged into Azure CLI
    1. Authenticate with Azure Developer CLI
        - `azd auth login`
        -  follow instructions and complete auth workflow
        - You should see: "Logged in to Azure"
        - ✅ | You are logged into Azure Developer CLI

??? note "Step 6: Provision Azure with `azd` tab 2️⃣"
    1. Stay in tab 2️⃣ - enter `azd up` and follow prompts
        1. Enter a new environment name - use `AITOUR`
        1. Select a subscription - pick the one from step 5.
        1. Select a location - pick `francecentral` or `swedencentral`
        1. You should see: _You can view detailed progress in the Azure Portal .._
    1. Process can take 15-20 minutes - when complete, you should get this message:
        1. **SUCCESS: Your up workflow to provision and deploy to Azure completed in 16 minutes 35 seconds.**
    1. ✅ | Your Azure infra is currently being provisioned..

??? note "Step 7: Track provisioning status in tab 3️⃣"
    1. Switch to the Azure Portal in tab 3️⃣
    1. Click on Resource Groups - see: `rg-AITOUR`
    1. Click on `rg-AITOUR` - see `Deployments` under **Essentials**
    1. Click `Deployments` - see Deployments page with activity and status ...
    1. Wait till all deployments complete - **this can take 20-25 minutes**
    1. See `Overview` page - **you should have 35 Deployment Items**
    1. See `Overview` page - **you should have 15 Deployed Resources**
    1. ✅ | Your Azure infra is ready and application is deployed!
