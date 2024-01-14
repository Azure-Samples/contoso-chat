# 06. Create AI Search Resource

> [!NOTE]
_Continue here and create resource manually only if your Azure subscription was not pre-provisioned with a lab Resource Group_

This step is done on the Azure Portal, not Azure AI Studio.

* []  **01** | Switch browser tab to +++**https://portal.azure.com**+++ 
    - Click on **"Create a resource"** on the home page
    - **Search** for +++Azure AI Search+++ in Create hub page.
    - Click the **Create** drop down in the matching result.
* []  **02** | Complete the "Create a search service" flow
    - **Subscription** - leave default
    - **Resource Group** - select the resource group for AI project
    - **Service Name** - use +++contoso-chat-aisearch+++
    - **Location** - use +++East US+++ (*Note the changed region!!*)
    - **Pricing tier** - check that it is set to **Standard**
* [] **03** | Review and Create resource
    - Click **"Review and Create"** for a last review
    - Click **"Create"** to confirm creation
    - You should see a "Deployment in progress" indicator
* [] **04** | Activate Semantic Search capability
    - Wait for the deployment to complete'
    - Click **Go to resource** to visit AI Search resource page
    - Click the **Semantic Ranker** option in the sidebar (left)
    - Check **Select Plan** under Standard, to enable capability.
    - Click **Yes** on the popup regarding service costs. 
