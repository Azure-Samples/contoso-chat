# 1️⃣ | Getting Started

Thie instructions are for participants of the instructor-led **"WRK550: Build a Retail Copilot Code-First on Azure AI"** workshop offered on the Microsoft AI Tour (2024-2025). If you're not at an AI Tour event right now, you can register for an upcoming event in a city near you.

- [**Register to attend**](https://aitour.microsoft.com/) at a tour stop near you.
- [**View Lab resources**](https://aka.ms/aitour/wrk550) to continue your journey.


!!! quote "Did you already check the [Pre-requisites](./../00-Before-You-Begin/index.md) and verify you met the requirements?"

---

## 1. Launch Skillable Lab

The **WRK550 Lab** is run using the Skillable platform which provides you with an active Azure account (_username_, _password_, _subscription_) that comes pre-provisioned with the resources you need for this lab (_Azure AI project_, _Azure OpenAI models_, supporting _Azure resources_, and data). 

**Important:** Once the Skillable VM is activated, you will have a fixed time limit (75 minutes) to complete the workshop before the VM shuts down. You can track the remaining time in the display at the top-right corner of the Skillable VM.

_If you are currently in an AI Tour session and have already launched the Skillable lab and verified credentials - move on to Section 2 below! Otherwise,  complete these two steps now_.

??? abstract "Step 0: Launch Browser Window In Incognito Mode (window A)"

    The workshop is conducted completely within a browser environment. You may have an enterprise Azure or GitHub account that you are logged into that may cause conflicts. To avoid this, we recommend opening a new browser window in **incognito mode** (private mode) with your preferred browser. 

    - Open a new browser window in incognito or private mode

    **✅ | CONGRATULATIONS!** - Your Learning journey has begun!

??? abstract "Step 1: Launch Skillable VM and log in (window B)"

    1. Navigate to the **WRK550 Lab** link 
    1. Click `Launch` - open new window with split panes (window B)
    1. **Check**: You see `Login` prompt in left pane
    1. **Check**: You see a "Resources" tab in right pane
    1. **Check**: You see an `Azure Portal` section under Resources
    1. **Check**: You see `Subscription`, `Username`, `Password` in that section
    1. **Check**: You see an `Admin`/`Password` section lower in Resources tab
    1. Click login (left), then click admin `Password` (right) and confirm
    1. **Check**: You see a Windows 11 Desktop in the left pane
    1. Keep window B open - you will need credentials in the next step.

    **✅ | CONGRATULATIONS!** - Your Skillable VM is live!



## 2. Setup Dev Environment

The **WRK550 Lab** requires a Python development runtime (with package dependencies), Visual Studio Code (with specific extensions) and Azure CLI tooling - before we can begin building. The sample comes pre-configured with a [`devcontainer.json`](https://containers.dev), allowing us to get a **pre-built development environment** using GitHub Codespaces, with no manual effort required.

_In this section, we'll fork the sample repo to our personal profiles - then launch GitHub Codespaces to activate that environment with a Visual Studio Code editor, right in the browser_.

??? info "Step 2: Open GitHub in tab 1️⃣"

    1. Open a new browser tab = Tab 1️⃣
    1. Navigate to the workshop sample with this link - [Contoso Chat](https://aka.ms/aitour/contoso-chat)
    1. Log into GitHub - use a personal login account
    1. Fork the sample to your profile - uncheck `main` to get all branches
    1. Switch to your fork of the repo - check that you have the `aitour-WRK550` branch

    **✅ | CONGRATULATIONS!** - Your have a personal copy of the sample to explore!

??? info "Step 3: Launch Codespaces in tab 2️⃣"

    1. Use the branch dropdown - switch to the `aitour-WRK550` branch
    1. Click the green `Code` button - select the `Codespaces` tab
    1. Click the `Create new codespaces on aitour-WRK550` button
    1. This should launch a new browser tab = Tab 2️⃣
    1. **Check:** The loading tab should show a VS Code editor 
    1. Codespaces is loading ... this may take a while (leave it open)

    **✅ | CONGRATULATIONS!** - Your Codespaces is running!


??? info "Step 4: Open Azure Portal in tab 3️⃣"

    1. Open a new browser tab = Tab 3️⃣
    1. Navigate to the [Azure Portal](https://portal.azure.com)
    1. Sign in with Skillable `Username`-`Password` from **Step 1** (above).
    1. Click `Resource Groups` - refresh it periodically if needed
    1. **Check:** A resource group `rg-AITOUR` is created
    1. Click resource group item - see 'Overview' in details page
    1. **Check:** Deployments (under "Essentials") - **has 35 deployments**
    1. **Check:** Resources (in Overview) - **has 15 resources created**

    **✅ | CONGRATULATIONS!** - Your Azure Infra is Provisioned!

??? info "Step 5: Open Azure AI Studio in tab 4️⃣"

    1. Open a new browser tab = Tab 4️⃣
    1. Navigate to the [Azure AI Studio](https://ai.azure.com)
    1. Click `Sign in` - should auto-login with Azure credentials
    1. Click `All resources` - **Check:** one hub resource listed
    1. Click hub resource - **Check:** one project resource listed
    1. Click `Deployments` tab - **Check:** 4 models under `aoai-connection` 
    1. **Check:** Models include - `gpt-4`, `gpt-35-turbo`, `text-embedding-ada-002` 

    **✅ | CONGRATULATIONS!** - Your Azure AI Project is ready!

??? info "Step 5: View Container Apps Endpoint in tab 5️⃣"

    1. Return to Azure Portal = Tab 3️⃣
    1. Visit the `rg-AITOUR` Resource group page
    1. Click the `Container Apps` resource - see details page
    1. Look for `Application Url` - at top right
    1. Click to launch in new tab = Tab 5️⃣
    1. See: page with `"Azure Container Apps"` and logo

    **🌟 | CONGRATULATIONS!** - Your ACA Endpoint is alive!

---

> We verified our Skillable credentials worked, and launched our Codespaces environment!

!!! example "Next → Let's [Validate Our Setup](./02-validate.md) before we begin building"
