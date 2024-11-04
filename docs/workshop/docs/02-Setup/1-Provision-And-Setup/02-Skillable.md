# B. Skillable-Based 

!!! warning "If you are are NOT in an instructor-led session, use the [Self-Guided Setup](./01-Self-Guided.md) instead!"

---

The instructor-led sessions use [Skillable](https://skillable.com), a _lab-on-demand_ platform with a built-in Azure subscription, that pre-provisions the infrastructure for the lab to save you time. Your instructor should provide you a link or QR code for the Skillable Lab at the start of your session.

## 1. Launch Skillable VM

You may have completed this step in-venue, with instructor guidance. If not, please expand the section below to complete the task now. At the end of this step you should have:

- [X] The Skillable VM tab open, with the Azure subscription details shown.
- [X] The Skillable countdown timer visible, with start time of 1h 15 mins.
- [X] The instruction guide open, with this section in focus.

??? info "Browser Tab 1️ - Skillable VM"

    The lab instructor should have shared a Skillable Lab link (URL or QR Code).

    - Open the browser and navigate to the link - _verify the lab title is right_.
    - Click the **Launch** button - _wait till the page completes loading_.
        - (Left) You will see a login screen - _we can ignore this for now_
        - (Top Right) You will see a countdown timer - it should start at 1hr 15 mins. 
        - (Right) You should see an instruction pane - _we'll validate this, next_
    - Review the instruction pane details:
        - Check the lab title - should be _Build a Retail Copilot Code-First on Auzre AI_
        - Check the Azure subscription - should have _username & password_ details filled in
        - Check the Workshop guide link - should open to a hosted version of this guide.
     
    **Leave the Skillable tab open in your browser**. We'll use the Azure credentials in the next step. And we'll revisit this tab at the end, to complete lab teardown. You can also track remaining lab time in the countdown timer.

    ---

    ✅ **CONGRATULATIONS!** | You setup the Skillable VM tab!


## 2. Launch GitHub Codespaces

Our development environment uses a Visual Studio Code editor with a Python runtime. The Contoso Chat sample repository is instrumented with a [dev container](https://containers.dev) which specifies all required tools and dependencies. At the end of this step you should have:

- [X] Forked the sample repo to your personal GitHub profile.
- [X] Launched GitHub Codespaces to get the pre-built dev environment.

??? info "Browser Tab 2 - GitHub Codespaces"

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


    ---

    ✅ **Your GitHub Codespaces tab is active!**



??? info "STEP 3: Open Azure Portal Tab"

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

    ---

    ✅ **Your Azure Portal tab is active!**


??? info "STEP 4: Open Azure AI Studio Tab"

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


    ---

    ✅ **Your Azure AI Studio tab is active!**


??? info "STEP 5: Open Azure Container Apps Tab"

    [Azure Container Apps](https://learn.microsoft.com/azure/container-apps/overview) will host the endpoint used to serve the Contoso Chat application on the Contoso Outdoors website. We have deployed a container app, but have not yet pushed code to it. 

    1. Return to the Azure Portal, Tab 3️⃣
    1. Visit the `rg-AITOUR` Resource group page
    1. Click the `Container App` resource to display the Overview page
    1. Look for `Application Url` (at top right), and click it to launch in new tab (Tab 5️⃣)
        * This creates a new tab `"Welcome to Azure Container Apps!"` displaying the logo

    !!! info "Azure Container Apps (ACA) is an easy-to-use compute solution for hosting our chat AI application. The application is implemented as a FastAPI server that exposes a simple `/create_request` API endpoint to clients for direct use or integration with third-party clients."

    **✅ | CONGRATULATIONS!** - Your ACA Endpoint is ready!

    ---

    ✅ **Your Azure Container Apps tab is active!**


??? info "STEP 6: Review Current Status"

    !!! success "Let's Review where we are right now"

        1. Tab 1️⃣ = GitHub Repo (starting point)
        1. Tab 2️⃣ = GitHub Codespaces (development environment)
        1. Tab 3️⃣ = Azure Portal (provisioned resources)
        1. Tab 4️⃣ = Azure AI Studio (AI project & models)
        1. Tab 5️⃣ = Azure Container Apps (Deployment target)

    
    1. Return to your GitHub Codespaces tab, Tab 2️⃣.

    You should see the Visual Studio Online development environment. If you have used Visual Studio Code on the desktop, it will look very familiar. You will see these components:

    * Left sidebar: The Activity Bar, including the "Prompty" extension logo at the end
        ![Prompty logo](../img/prompty-logo.png)
    * Left pane: The Explorer pane, showing the files in the `contoso-chat` repository
    * Right pane: A preview of the main README.md file from the repository
    * Lower pane: A terminal pane, with a `bash` prompt ready to receive input

    If you don't see those yet, wait until they appear in your browser.

    **✅ | CONGRATULATIONS!** - Your CodeSpace is running!


??? info "STEP 7: Authenticate With Azure"


??? info "STEP 8: Complete Post-Provisioning"


??? info "STEP 9: Verify Setup Complete!"