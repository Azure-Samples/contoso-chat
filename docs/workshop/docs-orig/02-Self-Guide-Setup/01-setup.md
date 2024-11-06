# 1️⃣ | Getting Started (Self-Guided Workshop)

These are the instructions for **Self Guided** learners for this workshop. If you are participating in an intructor-led version of this workshop, please skip ahead to Section 3️⃣ [Explore App Infrastructure](./../03-Workshop-Build/03-infra.md). 

In this section, you will provision the required resources to your
Azure subscription, and validated your local development environment in GitHub Codespaces.

!!! info "Reminder! → You will need to have these [ 0️⃣ | Pre-requisites](./../00-Before-You-Begin/index.md) before you begin setup"


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

Your development environment is all set. Now it's time to provision infra.

---

!!! info "Next → 3️⃣ [Provision Infra](./../02-Self-Guide-Setup/02-provision.md) before we start building!"
