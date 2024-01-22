# 07. Create CosmosDB Resource

> [!NOTE]
_Continue here and create resource manually only if your Azure subscription was not pre-provisioned with a lab Resource Group_

_We'll create this on Azure Portal, not Azure AI Studio._

* []  **01** | Switch browser tab to +++**https://portal.azure.com**+++ 
    - Click on **"Create a resource"** on the home page
    - **Search** for +++Azure CosmosDB+++ in Create hub page.
    - Click the **Create** drop down in the matching result.
    - You should see **"Which API best suits your workload?"**
* []  **02** | Complete the Azure CosmosDB for NoSQL flow
    - Click **Create** on the "Azure CosmosDB for NoSQL" option
    - **Subscription** - leave default
    - **Resource Group** - select the resource group for AI project
    - **Account Name** - use +++contoso-chat-cosmosdb+++
    - **Location** - use +++Sweden Central+++ (same as others)
    - Leave other options at defaults.

> [!hint] If you get an error indicating the _Account Name_ already exists, just add a number to make it unique - e.g., _contoso-chat-cosmosdb-1_
    
* [] **03** | Review and Create resource
    - Click **"Review and Create"** for a last review
    - Click **"Create"** to confirm creation
    - You should see a "Deployment in progress" indicator

Deployment completes in minutes. Visit resource to verify creation.

---

🥳 **Congratulations!** <br/> You're Azure CosmosDB Resource is ready.
