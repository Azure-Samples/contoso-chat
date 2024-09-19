# 3️⃣ | Validate Infra

!!! success "Let's Review where we are right now"

    1. We set up our development environment (GitHub Codespaces)
    1. We provisioned our infrastructure (Azure Resources)
    1. We connected our dev environment to our infra (Auth & Env Vars)
    1. We used SDK and CLI tools to push updates to infra (Data & App)


_In this section, we'll take a minute to understand what our Azure infrastructure looks like, and validate that the resources are deployed and initialized correctly. Here's a reminder of the Azure Application Architecure showing the key resources used. Let's dive in._

![ACA Architecture](./../img/aca-architecture.png)

_The Azure CosmosDB resources holds the "customer data" for our application. It is a noSQL database that contains JSON data for each customer, and the prior purchases they made_.

??? info "Step 1: Validate Azure Cosmos DB is ready in tab 3️⃣"

    1. Switch to the Azure Portal tab 3️⃣ - `rg-AITOUR` resource Overview
    1. Click the `Azure Cosmos DB account` resource - visit details page
    1. Click `Data Explorer` in top-nav menu on details page 
        - dismiss the popup dialog 
        - see: `contoso-outdoors` container with `customers` database
        - click `customers` - select `Items`
        - you should see: **12 data items in database**
    1. ✅ | Your Azure Cosmos DB resources is ready!

_The Azure AI Search resources contains the "product index" for our retailer's product catalog. It is the information "retrieval" service for RAG solutions, using sentence similarity and semantic ranking to return the most relevant results for a given customer query_.

??? info  "Step 2: Validate Azure AI Search is ready in tab 3️⃣"

    1. Switch to the Azure Portal tab 3️⃣ - `rg-AITOUR` resource Overview
    1. Click the `Search service` resource - visit details page
    1. Click `Search Explorer` in top-nav menu on details page 
        - see Search explorer with default index `contoso-products`
        - click "Search" with no other input
        - should see: Results dialog fill with index data
    1. ✅ | Your Azure AI Search resource is ready!

_The Azure AI project is the key AI resources for an application - and is associated with an Azure AI hub resources that manages admininstrative responsibilities like billing. The project maintains application state (including model deployments) for generative AI solutions._

??? info  "Step 3: Validate Azure AI Project is ready in tab 4️⃣"

    1. Switch to Azure AI Studio in tab 4️⃣ - start on Home page
    1. Click `All resources` in sidebar - _Note: this may say `All hubs`_.
    1. Verify that you see a Hub resource - _Note: you may also see an AI Services resource_
    1. Click the hub resource - you should see a project listed in hub overview page
    1. Click the project resource - visit `Deployments` in the sidebar
        - see `aoai-connection` and `aoai-safety-connection` sections
        - each has 3 model deployments - we care about three of these
            -gpt-35-turbo, gpt-4, text-embedding-ada-002
    1. ✅ | Your Azure AIProject resource is ready!

_Azure Container Apps (ACA) is an easy-to-use compute solution for hosting our chat AI application. The application is implemented as a FastAPI server that exposes a simple `/create_request` API endpoint to clients for direct use or integration with third-party clients_.

??? info  "Step 4: Validate Azure Container Apps is ready in tab 3️⃣"

    1. Switch to the Azure Portal tab 3️⃣ - `rg-AITOUR` resource Overview
    1. Click the `Azure Container App` resource - visit details page
    1. Click `Application Url` in **Essentials** section of Overview
    1. You should see: new tab 5️⃣ with page showing `{"message" : "Hello World" }" 
    1. ✅ | Your Azure Container App resource is ready **and** has app deployed!

_When iterating on a prototype application, we start with manual testing - using a single "test prompt" to validate our prioritzed scenario interactively, before moving to automated evaluations with larger test datasets. The FastAPI server exposes a `Swagger API` endpoint that can be used to conduct such testing in both local (Codespaces) and cloud (Container Apps). Let's try it!_

??? info  "Step 5: Test the Deployed Container App in tab 5️⃣ "

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

---

_Now you understand the application architecture, and have a sense for the retail copilot API, it's time to dig into the codebase and understand the three stages of our GenAIOps workflow - ideation, evaluation, and operationalization_.

!!! example "Next → [Let's Ideate Apps With Prompty!](./04-ideation.md) and learn about prompt engineering!"
