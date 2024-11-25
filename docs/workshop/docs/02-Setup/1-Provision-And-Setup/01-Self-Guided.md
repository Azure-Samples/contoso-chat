# A. Self-Guided Setup

!!! info "Welcome to the Self-Guided Lab Track! · Want the In-Venue Skillable Track instead? [Go here](./02-Skillable.md)"

---

## 1. Review Pre-Requisites

You need a valid Azure subscription, GitHub account, and access to relevant Azure OpenAI models, to complete this lab on your own. You'll need to provision the infrastructure yourself, as described below. Review the [Pre-Requisites](/contoso-chat/02-Setup/0-PreRequisites#self-guided) section if you need more details.

---

## 2. Launch GitHub Codespaces

Our development environment uses a Visual Studio Code editor with a Python runtime. The Contoso Chat sample repository is instrumented with a [dev container](https://containers.dev) which specifies all required tools and dependencies. At the end of this step you should have:

- [X] Launched GitHub Codespaces to get the pre-built dev environment.
- [X] Fork the sample repo to your personal GitHub profile.

---

### 2.1 Navigate to GitHub & Login

1. Open a browser tab (T1) and navigate to the link below.
        ``` title="Tip: Click the icon at far right to copy link"
        https://aka.ms/contoso-chat/prebuild
        ```
1. You will be prompted to log into GitHub. **Login now with your GitHub profile.**

---

### 2.2 Setup GitHub Codespaces

1. You will see a page titled **"Create codespace for Azure-Samples/contoso-chat"**
    - Check that the Branch is `msignite-LAB401`
    - Click dropdown for **2-core** and verify it is `Prebuild ready`

    !!! tip "Using the pre-build makes the GitHub Codespaces load up faster."

1. Click the green "Create codespace" button
    - You should see a new browser tab open to a link ending in `*.github.dev`
    - You should see a Visual Studio Code editor view loading (takes a few mins)
    - When ready, you should see the README for the "Contoso Chat" repository
    
    !!! warning "Do NOT Follow those README instructions. Continue with this workshop guide!"

---

### 2.3 Fork Repo To Your Profile

The Codespaces is running on the original Azure Samples repo. Let's create a fork from Codespaces, so we have a personal copy to modify. For convenience, we'll follow [this process](https://docs.github.com/codespaces/developing-in-a-codespace/creating-a-codespace-from-a-template#publishing-to-a-repository-on-github) which streamlines the process once you make any edit.

1. Lets create an empty file from the VS Code Terminal.

    ``` title="Tip: Click the icon at far right to copy command"
    touch .workshop-notes.md
    ```

1. This triggers a notification (blue "1") in Source Control icon on sidebar
1. Click the notification to start the Commit workflow 
1. Enter a commit message ("Forking Contoso Chat") and click "Commit"
1. You will now be prompted to "Publish Branch" 
    - You should see 2 options (remote = original repo, origin = your fork)
    - Select the `origin` option (verify that the URL is to your profile)
1. This will create a fork of the repository in your profile
    - It also updates the GitHub Codespaces to use your fork for commits
    - You are now ready to move to the next step!

---

### 2.4 Verify Dependencies

Use the following commands in the VS Code terminal to verify these tools are installed.

```bash
python --version
```
```bash
fastapi --version
```
```bash
prompty --version
```
```bash
az version
```
```bash
azd version
```

You are now ready to connect your VS Code environment to Azure.

---

## 3. Authenticate With Azure 

To access our Azure resources, we need to be authenticated from VS Code. Return to the GitHub Codespaces tab, and open up a VS Code terminal. Then, complete these two steps:

!!! task "Step 1: Authenticate with `az` for post-provisioning tasks"

1. Log into the Azure CLI `az` using the command below. 

    ```
    az login --use-device-code
    ```

1. Copy the 8-character code shown to your clipboard, then control-click the link to visit [https://microsoft.com/devicelogin](https://microsoft.com/devicelogin) in a new browser tab.

1. Select the account with the Username shown in the Skillable Lab window. Click "Continue" at the `are you sure?` prompt, and then close the tab

1. Back in the Terminal, press Enter to select the default presented subscription and tenant.


!!! task "Step 2: Authenticate with `azd` for provisioning & managing resources"

1. Log into the Azure Developer CLI using the command below. 

    ```
    azd auth login --use-device-code
    ```

1. Follow the same process as before - copy code, paste it when prompted, select account.
1. Note: you won't need to enter the password again. Just select the Skillable lab account.

---

## 4. Provision & Deploy App

_This project is an `azd-template`! It defines infrastructure-as-code assets that are used by the Azure Developer CLI to provision and manage your solution infrastructure resources_.


1. Provision & deploy the solution with one command: ```azd up```

1. You will be prompted for various inputs:

    - Subscription - specify your own active Azure subscription ID
    - Environment name for resource group - we recommend using `AITOUR` 
    - Location for deployment - we recommend using `francecentral`

        !!! tip "Refer to [Region Availability](#region-availability) guidance and pick the option with desired models and quota available."

1. Wait for the process to complete. It may take 15-20 minutes or more.
1. On successful completion you will see a **`SUCCESS: ...`** message on the console.

---

## Next → [Validate Setup](./03-Validation.md)
