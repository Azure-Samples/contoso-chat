# 2.2 Skillable-Based Setup

This is the start of the instructor-led workshop track for Microsoft AI Tour attendees.

!!! quote "ARE YOU REVISITING THE LAB AT HOME AFTER AITOUR? → [JUMP TO SELF-GUIDED SETUP](./../2-Provisioning/01-Self-Guided.md) instead"  

---

## 1. Review Pre-Requisites

Need a refresher on the pre-requisites for the workshop? [Review them here](./../1-Pre-Requisites/index.md#microsoft-ai-tour).

---

## 2. Launch Skillable VM

To continue with Skillable-based Setup, you will need the **Lab Launch URL** (link or QR Code) given to you by your instructor at the start of the session. 

!!! quote "On completing this step, you should have the following:"

    - [X] The Skillable VM tab open, with the Azure subscription details shown.
    - [X] The Skillable countdown timer visible, with _at least 1h 15 mins_ remaining.
    - [X] This instruction guide open, with this section in focus.

**If you already completed this stage, [move directly to Step 2](#2-launch-github-codespaces)**. Otherwise, expand the section below to get detailed instructions, and complete the task now.

??? task "LAUNCH SKILLABLE LAB → Check subscription status, open instruction manual "
    1. **Get Skillable Lab Link**. The lab code is `WRK550`. The Lab instructor in-venue will share a link (URL or QR Code) to the Skillable lab at the start of the in-venue session. _Ask a proctor if you don't have that handy._
    1. Open the browser and navigate to the link - _verify it says WRK550_.
    1. Click the **Launch** button - _this may take a few minutes to complete_.
        - When ready, you should see a new browser tab or window.
        - You will see a `Login` screen at left - **do NOT log in. We won't use it**.
        - You will see a countdown timer at top right - **verify it has at least 1hr 15 minutes**
        - You will see an instructions panel at right - **we'll review this next**
    1. Review the **Instructions Panel** and verify it has the following:
        - Lab Title - should be _Build a Retail Copilot Code-First on Azure AI_
        - Azure subscription - should have _username & password_ details filled in
        - Workshop guide - should open to a hosted version of this page.
    1. **IMPORTANT**: Leave this Skillable Session tab open in your browser!
        - We will refer to the Azure credentials in the next step
        - You can track the remaining time for the session in this tab.
        - You will return to this at the end to "End Session" cleanly.

---

## 3. Launch GitHub Codespaces

The Contoso Chat sample repository has a [dev container](https://containers.dev) defined. We can activate this in GitHub Codespaces to get a prebuilt development environment with all required tools and depenencies installed. Let's do that now.

!!! quote "On completing this step, you should have the following:"
    - [X] Launched GitHub Codespaces to get the pre-built dev environment.
    - [X] Forked the sample repo to your personal GitHub profile.
    - [X] Verified that required command-line tools were installed.

!!! info "**TIP**: Use `Copy to clipboard` feature to copy commands and reduce errors"
    In the following sections, you will encounter _codeblocks_ that have commands you will need to run in the VS Code terminal. 
    Hover over the codeblock to get a _Copy to clipboard_ icon for quick copy-paste operations.

### 3.1 Navigate to GitHub & Login


1. Open a new browser tab. Navigate to the link below.


    ``` title=""
    https://aka.ms/contoso-chat/prebuild
    ```

1. You will be prompted to log into GitHub. **Login with your GitHub profile.**

### 3.2 Setup GitHub Codespaces

1. You see a page titled **"Create codespace for Azure-Samples/contoso-chat"**
    - Check branch is `contoso-chat-v4` 
    - Click dropdown for **2-core** and verify it is `Prebuild ready`

        !!! tip "Using the pre-build option makes your GitHub Codespaces load up faster."

1. Click the green "Create codespace" button
    - You should see a new browser tab open to a link ending in `*.github.dev`
    - You should see a Visual Studio Code editor view loading (takes a few mins)
    - When ready, you should see the README for the "Contoso Chat" repository
    
        !!! warning "**CLOSE THE README TAB.** We will not be using those instructions today."

### 3.3 Fork Repo To Your Profile

Your GitHub Codespaces is running on the _original_ Azure Samples repo for this sample. Let's fork this now, so we have a personal copy to modify and reviist. We will use the GitHub CLI to complete this in just a few quick steps!


1. Open the VS Code terminal and run this command to verify the GitHub CLI is installed.

    ```bash title=""
    gh --version
    ```
    
1. Next, run this command to authenticate with GitHub, with scope set to allow fork actions.

    ```bash title=""
    GITHUB_TOKEN="" gh auth login --hostname github.com --git-protocol https --web --scopes workflow 
    ```

    The command ensures we complete the auth workflow from the web browser using the Git protocol over a secure HTTPS connection, and scope limited to workflow actions. Using an empty GITHUB_TOKEN ensure we don't use an existing token with broader scope. 

1. Follow the prompts to complete auth flow. (Expand the sections below for an example)

    ??? task "1. Complete Device Activation flow"

        - Say "Yes" when prompted to authenticate with GitHub credentials
        - Copy the one-time code provided in the console
        - Press "Enter" to open the Device Activation window
        - Copy the code into that window as shown below

            Here is an example of what that looks like:

            ![Activation](./../../img/gh-cli-activation.png)

    ??? task "2. Confirm GitHub authorization scope"

        - You should see this authorization dialog on activation
        - Click the green "Authorize github" button to continue
        - This gives the GitHub CLI (this session) permission to do the fork

            ![Activation](./../../img/gh-cli-confirmation'.png)

    ??? task "3. Verify you are Logged in."

        - The console log should show you are logged in successfully

            ![Activation](./../../img//gh-cli-authflow.png)

1. Now, run this command to fork the repo.

    ``` title=""
    GITHUB_TOKEN="" gh repo fork --remote
    ```

    You should see a `Created fork..` followed by an `Added remote origin ..` message. On completion, you should have a fork of the repo in your personal profile _and_ your local Codespaces environment will now be setup to commit changes to your fork.

1. **Optional**. Visit your GitHub profile and check that the fork was created. It should be at the location in the form `https://github.com/<username>/contoso-chat` where `<username>` should be replaces by your GitHub profile.

### 3.4 Check Tools Installed

The workshop uses the following tools and commands: `python`, `fastapi`, `prompty`, `az`, `azd`. These are pre-installed for you, but you can optionally verify these to get a sense for their current versions.

??? task "(Optional: Expand to view details) Verify intalled tools." 

    ```bash title=""
    python --version
    ```
    ```bash title=""
    fastapi --version
    ```
    ```bash title=""
    prompty --version
    ```
    ```bash title=""
    az version
    ```
    ```bash title=""
    azd version
    ```


## 4. Authenticate with Azure

To access our Azure resources, we need to be authenticated from VS Code. Make sure the Terminal pane is active in the GitHub Codespaces tab. Then, complete both the steps below (click each to expland for instructions).

??? task "1. Authenticate with `az` for post-provisioning tasks"

    1. Log into the Azure CLI `az` using the command below. 

        ``` title=""
        az login --use-device-code
        ```

    1. Copy the 8-character code shown to your clipboard, then control-click the link to visit [https://microsoft.com/devicelogin](https://microsoft.com/devicelogin) in a new browser tab.

    1. Select the account with the Username shown in the Skillable Lab window. Click "Continue" at the `are you sure?` prompt, and then close the tab

    1. Back in the Terminal, press Enter to select the default presented subscription and tenant.


??? task "2. Authenticate with `azd` for provisioning & managing resources"

    1. Log into the Azure Developer CLI using the command below. 

        ``` title=""
        azd auth login --use-device-code
        ```

    1. Follow the same process as before - copy code, paste it when prompted, select account.
    1. Note: you won't need to enter the password again. Just select the Skillable lab account.

!!! success "CONGRATULATIONS. You are logged in from Azure CLI and Azure Developer CLI"

## 5. Configure Env Variables

To build code-first solutions, we will need to use the Azure SDK from our development environment. This requires configuration information for the various resources we've already provisioned for you in the `francecentral` region. Let's retrieve those now.

1. Run the commands below in the same Visual Studio Code terminal.

    ``` title=""
    azd env set AZURE_LOCATION francecentral -e AITOUR --no-prompt
    ```
    ``` title=""
    azd env refresh -e AITOUR 
    ```

    (Press ENTER to select the default Azure subscription presented). 

2. Verify the environment variables were refreshed.

    The above commands will have created a `.azure/AITOUR/.env` file in your GitHub Codespaces environment with all the configuration information we will need to build our app. You can open the file from the VS Code file explorer **or** you can run the command below to view the values in the terminal:

    ``` title=""
    azd env get-values
    ```

    !!! tip "Note that the `.env` file does not contain any secrets (passwords or keys). Instead, we use  [Azure Managed Identities](https://learn.microsoft.com/entra/identity/managed-identities-azure-resources/overview) for keyless authentication as a _security best practice_" 


## 6. Do Post-Provisioning

_We can now use these configured tools and SDK to perform some post-provisioning tasks. This includes populating data in Azure AI Search (product indexes) and Azure Cosmos DB (customer data), and deploying the initial version of our application to Azure Container Apps_.

Return to the Visual Studio Code Terminal above:

1. Run the command below. (This will take a few minutes to complete.)

    ``` title=""
    bash ./docs/workshop/src/0-setup/azd-update-roles.sh
    ```

    !!! info "We pre-provisioned the Azure resources for you using a service principal. In this step, we update the resource roles to allow user access so you can populate data in Azure AI Search and Azure Cosmos DB from code. This step is not required in self-guided mode where you provision all resources yourself."

1. Once complete, run the command below. It will take a few minutes to complete.

    ``` title=""
    azd hooks run postprovision
    ```

    !!! info "This step runs the Jupyter Notebooks found in the relevant `data/` subfolders, populating the Azure AI Search and Azure CosmosDB resources with product catalog (index) and customer profile (orders)."
This step should take just a few minutes to complete from the commandline.

---

!!! success "CONGRATULATIONS. Your Skillable-based Setup is Complete! We'll Validate this, next!"
