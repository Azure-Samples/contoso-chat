# 14. Azure Config Connections

> [!NOTE]
_Your Azure resources are setup. Your local connections are configured. Now let's create **cloud connections** to run prompt flow in Azure later._

* []  **01** | Switch browser tab to +++**https://ai.azure.com**+++ 
    - Click the **"Build"** option in navbar.
    - Click your AI Project to view its details page.
    - Click the **"Settings"** option
    - Locate the "Connections" tab and click **"View All"**.

> [!IMPORTANT]
_Connection names used are critical and must match the names given below. Keep ".env" open for quick access to required values. **Do not copy the enclosing quotes** when you copy/paste values from ".env"._

* []  **02** | Click **New Connection** (create +++contoso-search+++) 
    - **Service** = "Azure AI Search (Cognitive Services" 
    - **Endpoint** = from .env "CONTOSO_SEARCH_SERVICE_ENDPOINT"
    - **API key** = from .env "CONTOSO_SEARCH_KEY"
    - **Connection name** = +++contoso-search+++

* []  **03** | Click **New Connection** (create +++aoai-connection+++) 
    - **Service** = "Azure OpenAI" 
    - **API base** = from .env "CONTOSO_AI_SERVICES_ENDPOINT"
    - **API key** = from .env "CONTOSO_AI_SERVICES_KEY"
    - **Connection name** = +++aoai-connection+++

> [!hint]
The next step uses Azure Machine Learning Studio instead of Azure AI Studio. We expect this to change with a future product update, allowing you to create _all_ connections from Azure AI Studio.

* []  **04** | Creating **Custom Connection** (+++contoso-cosmos+++) 
    - Visit +++https://ml.azure.com+++ instead
    - Under **Recent Workspaces**, click project (_contoso-chat-aiproj_)
    - Select **Prompt flow** (sidebar), then **Connections** (tab)
    - Click **Create** and select **Custom** from dropdown
    - **Name**: +++contoso-cosmos+++
    - **Provider**: Custom (default)
    - **Key-value pairs**: Add 4 entries (get env var values from .env)
        - key: +++key+++, value: "COSMOS_KEY", **check "is secret"**
        - key: +++_endpoint_+++ , value: "COSMOS_ENDPOINT"
        - key: +++_containerId_+++, value: +++customers+++
        - key: +++_databaseId_+++, value: +++contoso-outdoor+++
    - Click **Save** to complete step. 
    
* []  **06** | Click **Refresh** on menu bar to validate creation
    - Verify 3 connections were created *with these names* <br/> **"contoso-search", "contoso-cosmos", "aoai-connection"**

---

🥳 **Congratulations!** <br/> Your *cloud connections* to the Azure AI project are ready!
