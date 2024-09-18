#  2️⃣ | Validate Setup


??? note "Step 8: Validate Azure Cosmos DB is ready in tab 3️⃣"
    1. Switch to the Azure Portal tab 3️⃣ - `rg-AITOUR` resource Overview
    1. Click the `Azure Cosmos DB account` resource - visit details page
    1. Click `Data Explorer` in top-nav menu on details page 
        - dismiss the popup dialog 
        - see: `contoso-outdoors` container with `customers` database
        - click `customers` - select `Items`
        - you should see: **12 data items in database**
    1. ✅ | Your Azure Cosmos DB resources is ready!

??? note "Step 9: Validate Azure AI Search is ready in tab 3️⃣"
    1. Switch to the Azure Portal tab 3️⃣ - `rg-AITOUR` resource Overview
    1. Click the `Search service` resource - visit details page
    1. Click `Search Explorer` in top-nav menu on details page 
        - see Search explorer with default index `contoso-products`
        - click "Search" with no other input
        - should see: Results dialog fill with index data
    1. ✅ | Your Azure AI Search resource is ready!

??? note "Step 10: Validate Azure AI Project is ready in tab 4️⃣"
    1. Switch to Azure AI Studio in tab 4️⃣ - start on Home page
    1. Click `All resources` in sidebar - _Note: this may say `All hubs`_.
    1. Verify that you see a Hub resource - _Note: you may also see an AI Services resource_
    1. Click the hub resource - you should see a project listed in hub overview page
    1. Click the project resource - visit `Deployments` in the sidebar
        - see `aoai-connection` and `aoai-safety-connection` sections
        - each has 3 model deployments - we care about three of these
            -gpt-35-turbo, gpt-4, text-embedding-ada-002
    1. ✅ | Your Azure AIProject resource is ready!

??? note "Step 11: Validate Azure Container Apps is ready in tab 3️⃣"
    1. Switch to the Azure Portal tab 3️⃣ - `rg-AITOUR` resource Overview
    1. Click the `Azure Container App` resource - visit details page
    1. Click `Application Url` in **Essentials** section of Overview
    1. You should see: new tab 5️⃣ with page showing `{"message" : "Hello World" }" 
    1. ✅ | Your Azure Container App resource is ready **and** has app deployed!

??? note "Step 12: Test the Deployed Container App in tab 5️⃣ "
    1. Visit the `Application Url` page from Step 10 in tab 5️⃣
    1. Add a `/docs` suffix to that path - you should see: **FastAPI** page
    1. Expand the `POST` section by clicking the arrow
        - click `Try it out` to make inputs editable
        - enter `Tell me about your tents` for **question**
        - enter `2` for **customer_id**
        - enter []` for **chat_history**
        - enter **Execute** to run the query
    1. You should get a valid response with `answer` and `context`.
    1. ✅ | Your Contoso Chat AI is deployed - and works with valid inputs!

??? tip "This Completes Setup. Let's Review Status."

    At this stage you should have the following **5 tabs** open:

    1. Github Repo - starting tab 1️⃣
    1. GitHub Codespaces 2️⃣
    1. Azure Portal 3️⃣
    1. Azure AI Studio 4️⃣
    1. Azure Container Apps 5️⃣
    1. ✅ | All Azure resources are provisioned
    1. ✅ | Contoso Chat is deployed to ACA endpoint


We can now get to work on exploring the codebase and understanding how the application is architected, developed, evaluated, and deployed.

