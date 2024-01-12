# 03. Create Azure AI Resource

* []  **01** | Let's check for pre-provisioned resources
    - Go to your Azure Portal tab - +++**https://portal.azure.com**+++
    - Click the _'Resource Groups'_ option
    - Check if a Resource Group is already listed
* []  **02** | _If listed_ click for details and verify that it has:
    - an Azure AI resource 
    - an Azure AI service resource
    - an Azure AI project resource
    - an Azure AI search resource
    - an Azure CosmosDB resource

> [!WARNING]
_If these resources exist, this means you have a pre-provisioned Azure subscription. **Skip directly to Section [08. VSCode Azure Login](#8-vscode-azure-login)**_

<br/>

> [!hint]
_Continue here and create resource manually **only if** your Azure subscription was not pre-provisioned with a lab Resource Group_

* []  **03** | Navigate to +++**https://ai.azure.com**+++ in a new tab
    - Click **Sign in**. _No username/password entry required_.
    - Click the **"Manage"** option in navbar.
    - Click **"+ New Azure AI resource"** 
    - You should see a dialog pop up
* [] **04** | Complete "Create a resource" dialog
    - **Resource name**: +++contoso-chat-ai+++
    - **Azure subscription** (leave default)
    - Click **"Create new resource group"**
    - **Resource group**: +++contoso-chat-rg+++
    - **Location**: Pick +++Sweden Central+++
* [] **05** | Click "Next" in dialog
    - Click **Create** to create resource
    - This takes a few minutes. Wait till done.
* [] **06** | Go back to "Manage" home page
    - Verify that the Azure AI resource is listed. 

---

🥳 **Congratulations!** <br/> You're Azure AI resource is ready.
