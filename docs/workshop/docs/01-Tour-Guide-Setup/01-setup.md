# 1️⃣ | Getting Started: Instructor-Led Workshop

!!! example "Microsoft AI Tour Attendees:  <br/> Already launched the Skillable Lab and verified credentials? [Move Directly to Step 2](#2-set-up-your-dev-environment) to save time."   

The instructions are for participants of the instructor-led **"WRK550: Build a Retail Copilot Code-First on Azure AI"** workshop offered on the Microsoft AI Tour (2024-2025). 

If you're not at an AI Tour event right now, you can register for an upcoming event in a city near you.

- [**Register to attend**](https://aitour.microsoft.com/) at a tour stop near you.
- [**View Lab resources**](https://aka.ms/aitour/wrk550) to continue your journey.

!!! quote "Did you already check the [Pre-requisites](./../00-Before-You-Begin/index.md) and verify you met the requirements?"

---

## 1. Launch Skillable Lab

The **WRK550 Lab** is run using the Skillable platform which provides you with a temporary Azure account (_username_, _password_, _subscription_) that comes pre-provisioned with the resources you need for this lab (_Azure AI project_, _Azure OpenAI models_, supporting _Azure resources_, and data). 

**Important:** Once the Skillable VM is activated, you will have a fixed time limit (75 minutes) to complete the workshop before the VM shuts down. You can track the remaining time in the display at the top-right corner of the Skillable Lab window.

!!! info "If you are currently in an AI Tour session and have already launched the Skillable Lab and verified credentials - move on to Section 2 below. Otherwise,  complete these two steps now."

1. Open a new browser window in incognito mode (window A)

    The workshop is conducted completely within a browser environment. You may have an enterprise Azure or GitHub account that you are logged into from your browser that may cause conflicts. To avoid this, we recommend opening a new browser window in **incognito mode** (private mode) with your preferred browser. 

1. Open the **WRK550 Lab** link provided by your instructor in your browser.
1. Click `Launch` - this opens the Skillable Lab in a new window with two panes (window B)
1. **Check**: You see a `Password` prompt in the left pane.
    - This is a virtual machine. We will not use it in this workshop.
1. **Check**: You see a **Build a Retail Copilot Code-First on Azure AI** tab in right pane
    - Follow the instructions in this pane to open the lab instructions.

Do not close the Skillable Lab (window B) - you will need the **Azure Credentials** shown in this window in the next step.

**✅ | CONGRATULATIONS!** - Your Skillable Lab is live!

## 2. Set Up Your Dev Environment

The **WRK550 Lab** requires a Python development runtime (with package dependencies), Visual Studio Code (with specific extensions) and Azure CLI tooling - before we can begin building. The sample comes pre-configured with a [`devcontainer.json`](https://containers.dev), allowing us to get a **pre-built development environment** using GitHub Codespaces, with no manual effort required.

_In this section, we'll fork the sample repo to our personal profiles - then launch GitHub Codespaces to activate that environment with a Visual Studio Code editor, right in the browser_.

### 2.1 Open GitHub in Tab 1️⃣

The source code for the application used in this workshop is available on GitHub. Let's log into GitHub and copy a fork of the source code to your GitHub account.

1. Open a new browser tab (Tab 1️⃣)
1. **Navigate to** the [contoso-chat workshop sample](https://aka.ms/aitour/contoso-chat) with this link:

    ```
    https://aka.ms/aitour/contoso-chat
    ```

1. **Sign into** GitHub - use your own GitHub account to log in
1. Click **Fork** in the top-right corner of the page

1. In the "Create a new fork" page, scroll down and **uncheck** the option "Copy the main branch only".

    !!! warning "If you forget to uncheck that option, you will need to delete your fork and try again."

1. Click the **Create Fork** button.

    * You should now be at the page `https://github.com/YOURUSERNAME/contoso-chat` within your own GitHub account.
   
    * You now have a copy (known as a fork) of this workshop repository in your own GitHub account! Feel free to play with it, you won't break anything.

**✅ | CONGRATULATIONS!** - Your have a personal copy of the sample to explore!

### 2.2: Launch Codespaces in Tab 2️⃣

GitHub Codespaces will be our development environment for this workshop. Let's launch CodeSpaces now, starting from the fork of the `contoso-chat` repository you just created.

!!! tip "Even a free GitHub account will have sufficient GitHub CodeSpaces credits to run this workshop. Be sure to delete the CodeSpace after the workshop to minimize use of your credits."

1. Use the branch selection drop-down on the left side that now reads **main** and select the branch **aitour-WRK550**.

    ![alt text](../img/branch.png)

1. Click the green **<> Code** button in the top-right part of the page, click the **Codespaces** tab, and then click **Create codespace on aitour-WRK550**.

1. This will launch a new browser tab (Tab 2️⃣). It will take a few minutes for the CodeSpace to be ready for use. In the meantime, continue with the next steps. 

### 2.3: Open Azure Portal in Tab 3️⃣

1. Open a new browser tab (Tab 3️⃣)
1. Navigate to the [Azure Portal](https://portal.azure.com):
    ```
    https://portal.azure.com
    ```
1. **Sign in** using the `Username` and `Password` displayed under "Azure Credentials" in the Skillable Lab window you launched in **Step 1** (above).
1. You will be presented with a "Welcome to Microsoft Azure" screen. Click **Cancel** to dismiss, or click **Get Started** if you'd like to take an introductory tour of the Azure Portal.
1. In the Navigate section, **Click** `Resource Groups`.
1. A resource group has been created for you, containing the resources needed for the RAG application. **Click** `rg-AITOUR`.
1. **Check:** Deployments (under "Essentials") - There are **35 succeeded** Deployments. 
1. **Check:** Resources (in Overview) - There are **15 resources** in the resource group.

**✅ | CONGRATULATIONS!** - Your Azure Infra is Provisioned!

### 2.4 Open Azure AI Studio in Tab 4️⃣

1. Open a new browser tab = Tab 4️⃣
1. Navigate to the [Azure AI Studio](https://ai.azure.com?feature.customportal=false#home):
    ```
    https://ai.azure.com
    ```

1. **Click** `Sign in` -- you will auto-login with the Azure credentials used to sign into the portal.
1. Under Management in the left pane, **click** `All hubs`. One hub resource will be listed.

    !!! warning "The AI Studio UI is evolving. Instead of `All hubs` you may see an `All resources` item in the left pane instead, with 2 resources listed in the right - one of which should be a _hub_ resource."

    !!! info "An [AI Studio hub](https://learn.microsoft.com/azure/ai-studio/concepts/ai-resources) collects resources like generative AI endpoints that can be shared between projects."

1. **Click** the listed hub resource name to display it. **Check:** 1 project is listed under `Projects`.

    !!! info "An [AI Studio project](https://learn.microsoft.com/azure/ai-studio/how-to/create-projects?tabs=ai-studio) is used to organize your work when building applications."

1. Under "Shared Resources" in the left pane, **click** `Deployments`. The right pane should show two `*-connection` groups. **Check:** 4 models are listed under each connection. 

    !!! info "The Model Deployments section lists Generative AI models deployed to this Hub. For this application, we will use the chat completion models `gpt-4` and `gpt-35-turbo`, and the embedding model `text-embedding-ada-002`." 

**✅ | CONGRATULATIONS!** - Your Azure AI Project is ready!

### 2.5: View Container Apps Endpoint in Tab 5️⃣

[Azure Container Apps](https://learn.microsoft.com/azure/container-apps/overview) will host the endpoint used to serve the Contoso Chat application on the Contoso Outdoors website. We have deployed a container app, but have not yet pushed code to it. 

1. Return to the Azure Portal, Tab 3️⃣
1. Visit the `rg-AITOUR` Resource group page
1. Click the `Container App` resource to display the Overview page
1. Look for `Application Url` (at top right), and click it to launch in new tab (Tab 5️⃣)
    * This creates a new tab `"Welcome to Azure Container Apps!"` displaying the logo

!!! info "Azure Container Apps (ACA) is an easy-to-use compute solution for hosting our chat AI application. The application is implemented as a FastAPI server that exposes a simple `/create_request` API endpoint to clients for direct use or integration with third-party clients."

**✅ | CONGRATULATIONS!** - Your ACA Endpoint is ready!

## 3. Make sure CodeSpaces has completed launching

1. Return to your GitHub Codespaces tab, Tab 2️⃣.

You should see the Visual Studio Online development environment. If you have used Visual Studio Code on the desktop, it will look very familiar. You will see these components:

  * Left sidebar: The Activity Bar, including the "Prompty" extension logo at the end
    ![Prompty logo](../img/prompty-logo.png)
  * Left pane: The Explorer pane, showing the files in the `contoso-chat` repository
  * Right pane: A preview of the main README.md file from the repository
  * Lower pane: A terminal pane, with a `bash` prompt ready to receive input

If you don't see those yet, wait until they appear in your browser.

**✅ | CONGRATULATIONS!** - Your CodeSpace is running!

---

> We verified our Skillable credentials worked, and launched our Codespaces environment!


!!! example "Next → Let's [Validate Our Setup](./02-validate.md) before we begin building"
