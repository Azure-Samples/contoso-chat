# 09. VSCode Config Azure

> [!NOTE]
_This assumes you have the Azure Resource Group and related resources provisioned correctly from prior steps. We'll now configure Visual Studio Code to use our provisioned Azure resources._

* []  **01** | Download the 'config.json' for this Azure AI project
    - Visit +++https://portal.azure.com+++ in a new browser tab
    - Click on your created resource group (_contoso-chat-rg_)
    - Click on your Azure AI project resource (_contoso-chat-aiproj_) 
    - Look for the **download config.json** option under Overview
    - Click to download the file to the Windows 11 VM 
    - Open the file and **Copy** the contents to clipboard.

* []  **02** | Update your VS Code project with these values
    - Switch browser tab to your Visual Studio Code editor
    - Open VS Code Terminal, enter: +++touch config.json+++
    - This creates an empty config.json file in root directory.
    - Open file in VS Code and **Paste** data from clipboard
    - Save the file.