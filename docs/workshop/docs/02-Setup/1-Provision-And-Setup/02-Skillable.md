# B. Skillable-Based 

!!! warning "If you are are NOT in an instructor-led session, use the [Self-Guided Setup](./01-Self-Guided.md) instead!"

---

The instructor-led sessions use [Skillable](https://skillable.com), a _lab-on-demand_ platform with a built-in Azure subscription, that pre-provisions the infrastructure for the lab to save you time. Your instructor should provide you a link or QR code for the Skillable Lab at the start of your session.

## 1. Launch Skillable VM

You may have completed this step in-venue, with instructor guidance. If not, please expand the section below to complete the task now. At the end of this step you should have:

- [X] The Skillable VM tab open, with the Azure subscription details shown.
- [X] The Skillable countdown timer visible, with start time of 1h 15 mins.
- [X] The instruction guide open, with this section in focus.

??? example "Step 1.1 Launch Skillable VM"

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

---

## 2. Launch GitHub Codespaces

Our development environment uses a Visual Studio Code editor with a Python runtime. The Contoso Chat sample repository is instrumented with a [dev container](https://containers.dev) which specifies all required tools and dependencies. At the end of this step you should have:

- [X] Launched GitHub Codespaces to get the pre-built dev environment.
- [X] Fork the sample repo to your personal GitHub profile.

### 2.1 Navigate to GitHub & Login

1. Open a browser tab (T1) and navigate to the link below.
        ``` title="Tip: Click the icon at far right to copy link"
        https://aka.ms/contoso-chat/prebuild
        ```
1. You will be prompted to log into GitHub. **Login now**

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

### 2.3 Fork Repo To Your Profile

!!! tip "(OPTIONAL) You can also do this step using the GitHub CLI. Check out [this gist](https://gist.github.com/nitya/94dab67522f379e895a124ee32f5a5d3) for guidance."


The Codespaces is running on the original Azure Samples repo. Let's create a fork from Codespaces, so we have a personal copy to modify. 

!!! tip "We'll follow [this GitHub process](https://docs.github.com/codespaces/developing-in-a-codespace/creating-a-codespace-from-a-template#publishing-to-a-repository-on-github) triggered by repo edits. Check out [this gist](https://gist.github.com/nitya/97cf4c757c21e76f24ad9d51a85fb8ea) for guidance with screenshots"

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

### 2.4 Check Tools Installed

Use the following commands in the VS Code terminal to verify these tools are installed.

```bash title="Tip: Click the icon at far right to copy command"
python --version
```
```bash title="Tip: Click the icon at far right to copy command"
fastapi --version
```
```bash title="Tip: Click the icon at far right to copy command"
prompty --version
```
```bash title="Tip: Click the icon at far right to copy command"
az version
```
```bash title="Tip: Click the icon at far right to copy command"
azd version
```


### 2.5 Authenticate with Azure

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

!!! success "You are now logged into Azure CLI and Azure Developer CLI"

### 2.6 Configure Env Variables

To build code-first solutions, we will need to use the Azure SDK from our development environment. This requires configuration information for the various resources we've already provisioned for you in the `francecentral` region. Let's retrieve those now.

From the Terminal pane in Tab 2️⃣:

1. Run the commands below

```
azd env set AZURE_LOCATION francecentral -e AITOUR --no-prompt
```
```
azd env refresh -e AITOUR 
```

(Press ENTER to select the default Azure subscription presented). 

The file `.azure/AITOUR/.env` has been updated in our filesystem with information needed to build our app: connection strings, endpoint URLs, resource names and much more. You can open the file to see the values retrieved, or display them with this command:

```
azd env get-values
```

!!! info "No passwords or other secrets are included in the `.env` file. Authentication is controlled using [managed identities](https://learn.microsoft.com/entra/identity/managed-identities-azure-resources/overview) as a security best practice." 


### 2.7 Do Post-Provisioning

_We can now use these configured tools and SDK to perform some post-provisioning tasks. This includes populating data in Azure AI Search (product indexes) and Azure Cosmos DB (customer data), and deploying the initial version of our application to Azure Container Apps_.

From the Terminal pane in Tab 2️⃣:

1. Run the command below. (This will take a few minutes to complete.)

    ```
    bash ./docs/workshop/src/0-setup/azd-update-roles.sh
    ```

    !!! info "This updates the security profile for the provisioned Cosmos DB database so you can add data to it. This step isn't needed when you deploy Cosmos DB yourself."

1. Once complete, run the command below:

    ```
    azd hooks run postprovision
    ```

    This command populates Azure Search and Cosmos DB with product and customer data from Contoso Outdoors. It also builds and deploys a shell endpoint to the container app, which we will update in the next section. This will take a few minutes.

    !!! info "If you're curious, the code to populate the databases is found in Python Notebooks in `data` folder of the repository."

1. Refresh the Container App in tab 5️⃣ - it will update to say "Hello world" ✅

_We are ready to start the development workflow segment of our workshop. But let's first check that all these setup operations were successful!_.

---

## Next Step: [Validate Setup](./03-Validation.md)
