# 3️⃣ | Explore App Infrastructure

!!! success "Let's Review where we are right now"

    1. We set up our development environment (GitHub Codespaces)
    1. We provisioned our infrastructure (Azure Resources)
    1. We connected our dev environment to our infra (Auth & Env Vars)
    1. We used SDK and CLI tools to push updates to infra (Data & App)


_In this section, we'll take a minute to understand what our Azure infrastructure looks like, and validate that the resources are deployed and initialized correctly. Here's a reminder of the Azure Application Architecure showing the key resources used. Let's dive in._

![ACA Architecture](./../img/aca-architecture.png)

## Step 1: Validate Azure Cosmos DB is populated

The Azure CosmosDB resource holds the customer data for our application. It is a noSQL database that contains JSON data for each customer, and the prior purchases they made.

1. Switch to the **Azure Portal** (Tab 3️⃣) and display the `rg-AITOUR` resource group Overview
1. **Click** the `Azure Cosmos DB account` resource name to visit its details page
1. **Click** `Data Explorer` in the top-nav menu 
    - dismiss the popup dialog to skip the movie
    - see: `contoso-outdoors` container with `customers` database
    - click `customers`, then select `Items`
    - you should see: **12 data items in database**

✅ | Your Azure Cosmos DB resource is ready!

## Step 2: Validate Azure AI Search is populated

The Azure AI Search resources contains the product index for our retailer's product catalog. It is the information **retrieval** service for **R**AG solutions, using sentence similarity and semantic ranking to return the most relevant results for a given customer query.

1. Switch to the Azure Portal (Tab 3️⃣) and display the  `rg-AITOUR` resource group Overview
1. Click the `Search service` resource name to visit its details page
1. Click `Search Explorer` in the top-nav menu  
    - see Search explorer with default index `contoso-products`
    - **click** "Search" with no other input
    - you will see: Results dialog filled with index data for the product database.

✅ | Your Azure AI Search resource is ready!

## Step 3: Test the Deployed Container App

When iterating on a prototype application, we start with manual testing - using a single "test prompt" to validate our prioritzed scenario interactively, before moving to automated evaluations with larger test datasets. The FastAPI server exposes a `Swagger API` endpoint that can be used to conduct such testing in both local (Codespaces) and cloud (Container Apps). Let's try it on a fully functional version of the endpoint!

1. Return to your deployed Azure Container App in Tab 5️⃣ 
1. Add a `/docs` suffix to the URL and browse to that path - you will see: **FastAPI** page
1. Expand the `POST` section by clicking the arrow
    - click `Try it out` to make inputs editable
    - enter `Tell me about your tents` for **question**
    - enter `2` for **customer_id**
    - enter `[]` for **chat_history**
    - enter **Execute** to run the endpoint with the provided parameters.

You will get a response body with `answer` and `context` components.

* `answer` is the chatbot's response to the customer's `question`, entered into the chat window
* `context` is the additional information provided to the Generative AI model, which it uses to ground its answer. In this app, that includes information about products relevant to the customer question. The products selected may depend on the `customer_id` and their associated order history. 
* The web app provides the `chat_history` from the chat window, which provides additional context for the generative AI model to ground its response.

✅ | Your Contoso Chat AI is deployed - and works with valid inputs!

---

_Now you understand the application architecture, and have a sense for the retail copilot API, it's time to dig into the codebase and understand the three stages of our GenAIOps workflow - ideation, evaluation, and operationalization_.

!!! example "Next → [Let's Ideate Apps With Prompty!](./04-ideation.md) and learn about prompt engineering!"
