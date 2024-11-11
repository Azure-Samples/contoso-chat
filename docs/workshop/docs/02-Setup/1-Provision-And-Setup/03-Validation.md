# Validate Your Setup

!!! success "Let's Review where we are right now"

    ![Dev Workflow](./../../img/workshop-developer-flow.png)

    Looking at our end-to-end developer workflow, we completed the `PROVISION` and `SETUP` stages. Before we dive into the `IDEATE` stage, let's take a minute to validate that we are ready to begin development.

    1. We set up our development environment (GitHub Codespaces)
    1. We provisioned our infrastructure (Azure Resources)
    1. We connected our dev environment to our infra (Auth & Env Vars)
    1. We used SDK and CLI tools to push updates to infra (Data & App)

It's time to organize our development environment and verify we are ready for ideation!

---

### 3.1 Azure Portal Tab

!!! tip "The Azure Portal helps us view the resources provisioned on Azure and check that they are setup correctly"

Here's a reminder of the Azure Application Architecure - let's check our provisioned Resource Group to make sure these resources were created.

![ACA Architecture](./../../img/aca-architecture.png)

1. Open a new browser tab and navigate to the link below:
    ``` title="Tip: Click the icon at far right to copy text"
    https://portal.azure.com
    ```

1. **Sign in** using the `Username` and `Password` displayed under "Azure Credentials" in the Skillable Lab window you launched in **Step 1** (above).
1. You will be presented with a "Welcome to Microsoft Azure" screen. Click **Cancel** to dismiss, or click **Get Started** if you'd like to take an introductory tour of the Azure Portal.
1. In the Navigate section, **Click** `Resource Groups`.
1. A resource group has been created for you, containing the resources needed for the RAG application. **Click** `rg-AITOUR`.
1. **Check:** Deployments (under "Essentials") - There are **35 succeeded** Deployments. 
1. **Check:** Resources (in Overview) - There are **15 resources** in the resource group.

---

### 3.2 Azure AI Studio Tab

!!! tip "The Azure AI Studio lets us view and manage the Azure AI project for our app."

1. Open a new browser tab = Tab 4️⃣
1. Navigate to the [Azure AI Studio](https://ai.azure.com?feature.customportal=false#home):
    ``` title="Tip: Click the icon at far right to copy text"
    https://ai.azure.com
    ```

1. **Click** `Sign in` -- you will auto-login with the Azure credentials used to sign into the portal.
1. Under Management in the left pane, **click** `All hubs`. One hub resource will be listed.

    !!! warning "The AI Studio UI is evolving. Instead of `All hubs` you may see an `All resources` item in the left pane instead, with 2 resources listed in the right - one of which should be a _hub_ resource."

    !!! info "An [AI Studio hub](https://learn.microsoft.com/azure/ai-studio/concepts/ai-resources) collects resources like generative AI endpoints that can be shared between projects."

1. **Click** the listed hub resource name to display it. **Check:** 1 project is listed under `Projects`.

    !!! info "An [AI Studio project](https://learn.microsoft.com/azure/ai-studio/how-to/create-projects?tabs=ai-studio) is used to organize your work when building applications."

1. Under "Shared Resources" in the left pane, **click** `Deployments`. The right pane should show two `*-connection` groups. **Check:** 4 models are listed under each connection. 

    !!! info "The Model Deployments section lists Generative AI models deployed to this Hub. For this application, we will use the chat completion models `gpt-4` and `gpt-35-turbo`, and the embedding model `text-embedding-ada-002`." 


---

### 3.3 Azure Container App Tab

!!! tip "The Azure Container App provides the hosting environment for our copilot (API endpoint)"

[Azure Container Apps](https://learn.microsoft.com/azure/container-apps/overview) will host the endpoint used to serve the Contoso Chat application on the Contoso Outdoors website. The Azure provisioning should have deployed a default Azure Container App to this endpoint.

1. Return to the Azure Portal, Tab 3️⃣
1. Visit the `rg-AITOUR` Resource group page
1. Click the `Container App` resource to display the Overview page
1. Look for `Application Url` (at top right), and click it to launch in new tab (Tab 5️⃣)
    * This creates a new tab `"Welcome to Azure Container Apps!"` displaying the logo

!!! info "Azure Container Apps (ACA) is an easy-to-use compute solution for hosting our chat AI application. The application is implemented as a FastAPI server that exposes a simple `/create_request` API endpoint to clients for direct use or integration with third-party clients."



---

## 1.1. Check Azure Cosmos DB

The Azure CosmosDB resource holds the customer data for our application. It is a noSQL database that contains JSON data for each customer, and the prior purchases they made.

1. Switch to the **Azure Portal** (Tab 3️⃣) and display the `rg-AITOUR` resource group Overview
1. **Click** the `Azure Cosmos DB account` resource name to visit its details page
1. **Click** `Data Explorer` in the top-nav menu 
    - dismiss the popup dialog to skip the movie
    - see: `contoso-outdoor` container with `customers` database
    - click `customers`, then select `Items`
    - you should see: **12 data items in database**

✅ | Your Azure Cosmos DB resource is ready!

## 1.2. Check Azure AI Search 

The Azure AI Search resources contains the product index for our retailer's product catalog. It is the information **retrieval** service for **R**AG solutions, using sentence similarity and semantic ranking to return the most relevant results for a given customer query.

1. Switch to the Azure Portal (Tab 3️⃣) and display the  `rg-AITOUR` resource group Overview
1. Click the `Search service` resource name to visit its details page
1. Click `Search Explorer` in the top-nav menu  
    - see Search explorer with default index `contoso-products`
    - **click** "Search" with no other input
    - you will see: Results dialog filled with index data for the entire product database.
1. Enter `sleeping bag` in the text box, and click Search
    - Verify that the first result returned relates to a sleeping bag from the catalog
1. Enter `something to make food with` in the text box, and click Search       
    - Verify that the first result returned relates to a camping stove

✅ | Your Azure AI Search resource is ready!

## 1.3. Check Azure Container App

When iterating on a prototype application, we start with manual testing - using a single "test prompt" to validate our prioritzed scenario interactively, before moving to automated evaluations with larger test datasets. The FastAPI server exposes a `Swagger API` endpoint that can be used to conduct such testing in both local (Codespaces) and cloud (Container Apps). Let's try it on a fully functional version of the endpoint!

1. Return to your deployed Azure Container App in Tab 5️⃣ 
1. Add a `/docs` suffix to the URL and browse to that path - you will see: **FastAPI** page
1. Expand the `POST` section by clicking the arrow
    - click `Try it out` to make inputs editable
    - enter `Tell me about your tents` for **question**
    - enter `2` for **customer_id**
    - enter `[]` for **chat_history**
    - enter **Execute** to run the endpoint with the provided parameters.
    
You will get a response body with `question`, `answer` and `context` components. 

- **Check** `question` -  is the customer's question the same as that typed in the chat window on the Contoso Outdoor website
- **Check** `answer` -  is the chatbot's response to the customer's `question`, as generated by this RAG application
- **Check** `context` - is the additional information provided to the Generative AI model being used by it used to ground its answer.
    - In this app, that includes information about products relevant to the customer question.
    - The products selected may depend on `customer_id` and the associated order history. 
    - The web app provides `chat_history` from the chat window - which can serve as additional context that the model can use to ground the response.

!!! note "Exercise → Repeat exercise with a different customer ID (between 1 and 12). How did the response change?"


---


## 1.4. Let's Connect The Dots 💡

!!! info "Recall that the [Retrieval Augmented Generation](https://learn.microsoft.com/en-us/azure/ai-studio/concepts/retrieval-augmented-generation#how-does-rag-work) works by *retrieving* relevant knowledge from your data stores, and _augmenting_ the user query with it to create an enhanced prompt - which _generates_ the final response."

To implement this RAG pattern, we need to execute three steps:

1. **Setup data sources** and populate them with our data (product catalog, customer orders)
1. **Create [indexes](https://learn.microsoft.com/azure/ai-studio/concepts/retrieval-augmented-generation#how-does-rag-work)** for efficient information retrieval by LLMs (e.g., find matching products)
1. **Connect our Azure AI project** to access data/indexes code-first, for use in processing steps.

In the previous section we setup the data sources (provisioning infra) and populated them with data (post-provisioning scripts) as follows:

1. **Azure CosmosDB** - loaded **12 records** from `data/customer_info`, got _customers_ database.
1. **Azure AI Search** - loaded **20 records** from `data/product_info`, got _contoso-products_ index.

In this section, we verified these steps and checked off the first two items on our RAG checklist above. In the next section (Ideation with Prompty) we'll see how we achieve the third item with a code-first approach that makes use of the Azure AI Search, Azure CosmosDB and Azure OpenAI services through their Azure SDKs.

---

_Now you understand the application architecture, and have a sense for the retail copilot API, it's time to dig into the codebase and understand the three stages of our GenAIOps workflow - ideation, evaluation, and operationalization_.

!!! example "Next → [Let's Ideate Apps With Prompty!](./../../03-Ideate/index.md) and learn about prompt engineering!"
