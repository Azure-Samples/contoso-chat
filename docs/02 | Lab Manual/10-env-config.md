# 10. VSCode Config Env

> [!hint]
_This assumes you the Azure Resource Group and related resources were setup previously. We'll now configure service endpoints and keys as env vars for programmatic access from Jupyter Notebooks._

* []  **01** | Keep your Visual Studio Code editor open in one tab
    - Find the **local.env** file in the root directory
    - Open VS Code Terminal, enter: +++cp local.env .env+++
    - This should copy "local.env" to a new **.env** file.
    - Open ".env" in Visual Studio Code, keep tab open.

> [!hint] 
This involves multiple Copy-Paste actions. If you have trouble pasting into VS Code window, right-click and choose **Paste** from the menu.

* []  **02** | Update the Azure OpenAI environment variables
    - Open +++https://ai.azure.com+++ in a new tab
    - Click **"Build"**, then open your AI project page.
    - Click **"Settings"**, click **"Show endpoints"** in the first tile
    - Copy **Azure.OpenAI** endpoint value, <br/> To "CONTOSO_AI_SERVICES_ENDPOINT" value in ".env"
    - Copy **Primary key** value <br/> To "CONTOSO_AI_SERVICES_KEY" value in ".env"

* []  **03** | Update the Azure AI Search environment variables
    - Open +++https://portal.azure.com+++ in a new tab
    - Open your Azure AI Search resource page (_contoso-chat-aisearch_)
    - Copy **Uri** value under Overview page <br/> To "CONTOSO_SEARCH_SERVICE" in ".env"
    - Copy **Primary admin key** value under Keys page <br/> To "CONTOSO_SEARCH_KEY" in ".env"

* []  **04** | Locate the Azure CosmosDB environment variables
    - Open +++https://portal.azure.com+++ in a new tab
    - Open your Azure CosmosDB resource page, click **Keys**
    - Copy **URI** value, <br/> To "COSMOS_ENDPOINT" value in ".env"
    - Copy **PRIMARY KEY** value <br/> To "COSMOS_KEY" value in ".env"

* []  **05** | Save the ".env" file.

---

🥳 **Congratulations!** <br/> Your VS Code env variables are updated!
