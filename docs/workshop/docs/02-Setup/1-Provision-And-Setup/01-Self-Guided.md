# A. Self-Guided 

!!! warning "If you are are currently in an in-venue instructor-led session, use the [Skillable Setup](./02-Skillable.md) instead!"

---

## 1. Pre-Requisites

If you have not already done so, review the [Pre-Requisites](./../0-PreRequisites/index.md) for Self-Guided workshops and make sure you have a valid Azure subscription, GitHub account, and access to relevant Azure OpenAI models before you begin. Note that the main difference with this flow is that you will need to _provision your own infrastructure_ for the project.

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

### 2.5 Authenticate With Azure 🚨

### 2.6 Provision & Deploy App 🚨

---

## Next: Go To [Validate Setup](./03-Validation.md)
