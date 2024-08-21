<style>
button {
  background-color: #4CAF50;
  color: white;
  border: none;
  padding: 10px 20px;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  font-size: 16px;
  margin: 4px 2px;
  cursor: pointer;
}
</style>

<script>
function copyToClipboard() {
  const code = document.getElementById('codeBlock').innerText;
  navigator.clipboard.writeText(code).then(() => {
    alert('Code copied to clipboard!');
  }).catch(err => {
    console.error('Failed to copy: ', err);
  });
}
</script>



# Workshop Instructions

<pre>
<code id="codeBlock">
TEST
</code>
</pre>

<button onclick="copyToClipboard()">Copy to Clipboard</button>

!!! note "Microsoft AI Tour 2024 Registration Is Live"

    The workshop is offered as an **instructor-led** session (WRK550) on the **Prototype to Production** track:

    > Use Azure AI Studio to build, evaluate, and deploy a customer support chat app. This custom copilot uses a RAG architecture built with Azure AI Search, Azure CosmosDB and Azure OpenAI to return responses grounded in the product and customer data.

    - [**Register to attend**](https://aitour.microsoft.com/) at a tour stop near you.
    - [**View Lab resources**](https://aka.ms/aitour/wrk550) to continue your journey.

The workshop supports 3 delivery formats:
 
1. **Instructor Led** 👉🏽 Bring your laptop. You get a subscription with pre-provisioned infra.
1. **Partner Led** 👉🏽 Bring your laptop. You may need your own subscription and self-deploy infra.
1. **Self-guided** 👉🏽 Bring your laptop and your own subscription. You must self-deploy infra.

Provisioning infrastructure (e.g., in self-deploy mode) takes **35-40** minutes. The workshop itself can be completed in **60-75 minutes** in-venue. The self-guided option allows you to explore this at your own pace beyond the default workshop scope.

---

**Table of Contents**

1. [Learning Objectives](#1-learning-objectives)
2. [Pre-Requisites](#2-pre-requisites)
3. [Provision Infrastructure](#3-provision-infrastructure)
    - [3.1 Pre-Provision Option](#31-pre-provision-option)
    - [3.2 Self-Deploy Option ](#32-self-deploy-option)
    - [3.3 Validate Infrastructure](#33-validate-infrastructure)
4. [Setup Dev Environment](#4-setup-dev-environment)
    - [4.1 Fork Contos Chat](#41-fork-contoso-chat-repo)
    - [4.2 Launch GitHub Codespaces](#42-launch-github-codespaces)
    - [4.3 Authenticate With Azure](#43-authenticate-with-azure)
    - [4.4 Verify Environment Variables](#44-verify-environment-vars)
5. [Build a Custom Copilot](#5-build-a-custom-copilot)
    - [5.1 ](#51-install-vs-code-extensions)
    - [5.2 ](#52-create-chatprompty-v1)
    - [5.3 ](#53-create-chat_requestpy-v1)
    - [5.4 ](#54-create-flexflowyaml-app)
    - [5.5 ](#55-run-your-copilot-app)
6. [Evaluate a Custom Copilot](#6-evaluate-a-custom-copilot)
    - [6.1 ](#61-understand-the-metrics)
    - [6.2 ](#62-understand-the-tools)
    - [6.3 ](#63-create-evaluation-dataset)
    - [6.4 ](#64-create-evaluation-flow)
    - [6.5 ](#65-evaluate-your-copilot-v1)
7. [Chat with Your Data (RAG)](#7-chat-with-your-data-rag)
    - [7.1 ](#71-understand-rag-pattern)
    - [7.2 ](#72-setup-ai-search-index)
    - [7.3 ](#73-setup-azure-cosmosdb)
    - [7.4 ](#74-update-chatprompty-v2)
    - [7.5 ](#75-update-chat_requestpy-v2)
8. [Deploy & Test Copilot](#8-deploy--test-the-copilot)
    - [8.1 ](#81-understant-azure-ai-studio)
    - [8.2 ](#82-view-copilot-deployment)
    - [8.3 ](#83-test-copilot-deployment)
9. [Integrate with Contoso Web](#9-integrate-with-contoso-web)
    - [9.1 ](#91-fork-contoso-web-repo)
    - [9.2 ](#92-launch-github-codespaces)
    - [9.3 ](#93-set-environment-variables)
    - [9.4 ](#94-preview-contoso-web)
    - [9.5 ](#95-test-contoso-web-ui)
10. []()
    - [10.1 ](#101-cleanup-resource)
    - [10.2 ](#102-star-or-watch-repo)
    - [10.3 ](#103-browse-resources)

_If you find this sample useful, consider giving us a star on GitHub! If you have any questions or comments, consider filing an Issue on the [source repo](https://github.com/Azure-Samples/contoso-chat)_.

## 1. Learning Objectives

In this workshop, you will learn how to:

* Use Azure AI Studio as a code-first platform for building custom copilots​

* Prototype a custom copilot on VS Code with powerful tools (Prompty, Promptflow, Codespaces)​

* Optimize your custom copilot with manual testing & AI-assisted evaluation (Quality, Safety)​

* Operationalize your custom copilot by deploying to Azure AI Studio (Monitoring, Filters, Logs)​

* Customize the sample to suit your application scenario (data, functions, frameworks, models)

If you've gotten this far, you have already:

* Launched the Lab instructions
* Reviewed pre-requisites for this workshop
* Forked the repository for this workshop
* Launched GitHub Codespaces
* Opened this file in VS Code Online

## 2. Log into your Azure account from the terminal

We have provided you with a temporary Azure subscription for you to use with this workshop. It is pre-deployed with all the resources you will need.

You can find the username and password at the bottom of the Lab Instructions window titled "Build a Retail Copilot Code-First on Azure AI".

* Find the username and password for your Azure subscription in the Lab Instructions window.

* Click the Terminal Pane in the VS Code online window

    * It's just below these instructions, in the bottom-right corner of your browser

* Copy the command below and paste it into the command line, and hit ENTER:

    * azd auth login --use-device-code

* Copy the code show to your clipboard, and then click enter. 

    * A new browser window will open

* If you are prompted to select an account, click "Use another account"

    * This can happen if you have previously used this browser to log Azure using yout own account, for example

* Copy your username from the Lab Instructions window, paste it in, and click Next

* Copy your username from the Lab Instructions window, paste it in, and click Sign In

* At the prompt "Are you trying to sign in to Microsoft Azure CLI?", click Continue

* Close the "Microsoft Azure Cross-platform Command Line Interface" tab

## 3. Try out the completed app

There is a complete working contoso-web app deployed by Skillable

* Click on the URL to launch the contoso-web app

* Observe logged-in state of Sarah Lee

* Scroll through the page to see the product catalog

* Click on the Cozy Nights Sleeping Bag to see the product information page

    * Description, features, reviews, FAQ, return policy, cautions, user guide, warranty, technical specifications

* Click Back to return to home page

* Click "chat" icon

* Questions to ask:

```
What can you do?
What is a good sleeping bag for winter use?
How much is the Cozy Nights Sleeping bag?
How should I take care of it?
What did I order last time?
```
## 3. Explore the resources

We have deployed several resources to your Azure Subscription that will be used in this RAG architecture. 

First, lets take a look at the resources as they appear in the Azure Portal. Then, we'll use the Codespaces terminal to take a look at some of them in a little more detail.

### 3.1 Visit Azure Portal

* Open a new browser tab for the Azure Portal 
    - **Navigate to** https://portal.azure.com **in a new tab**.
    - You may be prompted to **log in**, in which case use the Username and Password provided in the Skillable Lab window.
 
* Launch the "Resource Groups" tool
    - **Click the hamburger menu** (in the top-left corner)
    - Select **Resource Groups**

* Explore the contents of the resource group
    - **Click** the name of the resource group: **rg-AITOUR**
    - You will see: Overview page with 14 resources listed.
    - Look at the Type column and see that you have the following resources deployed:
        - **Search service**: (Azure AI Search, a vector database to store product information)
        - **Azure Cosmos DB account**(Azure CosmosDB, a relational database to store customer data and orders)    
        - **Azure AI services** (endpoints for OpenAI models used in the application)
        - **Azure AI hub** (a hub in Azure AI Studio collecting the shared resources used in the app)
        - **Azure AI project** (the project in Azure AI Studio containing the assets for the RAG application)

### Customer data: CosmosDB

Customer data is sourced from a collection of JSON files and then loaded into Cosmos DB.

* **Explore** the JSON files in [../data/customer_info](../data/customer_info), for example [customer_info_1.json](../data/customer_info/customer_info_1.json)
    * Customer id, name, age, contact info, membership tier
    * Product Purchase history
        * Product info, purchase date, price
* The script used to load the data into Cosmos DB has already been run for you. Take a look at the Notebook version [../data/customer_info/create-cosmos-db.ipynb](../data/customer_info/create-cosmos-db.ipynb), but don't run any cells
* **Open the notebook** [../data/customer_info/investigate-cosmos-db.ipynb](../data/customer_info/investigate-cosmos-db.ipynb)
* **Run each of the cells** to take a look at the data in Cosmos DB

### Product purchase history: CosmosDB

The product data you see in CosmosD was sourced from a CSV file:

* **Open** [../data/product_info/products.csv](../data/product_info/products.csv)
  * Product id
  * Name
  * Price
  * Category
  * Brand
  * Description

Observe that these details match those in the customer order history stored in Cosmos DB.

### Product information: Azure AI Search

TODO: Have the user use the CLI to do some test searches on the Azure AI Search.

### Model endpoints: Azure AI Studio

 1. Once provisioning completes, monitor progress for app deployment.
    - Visit the [Azure AI Studio](https://ai.azure.com/build)
    - Click Sign In if necessary
    - Look for an AI Project associated with the above resource group
    - Click `Deployments` to track the status of the application deployment
 1. Test the deployed endpoint from Azure AI Studio
    - Click the newly-created `chat-deployment-xx` endpoint listed
    - In the details page, click the `Test` tab for a built-in testing sandbox
    - In the `Input` box, enter a new query in this format and submit it:
        ```
        {"question": "Tell me about hiking shoes", "customerId": "2", "chat_history": []}
        ```
    - If successful, the response will be printed in the area below this prompt.

You can find your deployed retail copilot's _Endpoint_ and _Primary Key_ information on the deployment details page in the last step. Use them to configure your preferred front-end application (e.g., web app) to support a customer support chat UI capability that interacts with the deployed copilot in real time.  

## 5. Build A Custom Copilot

### 5.1 Install VS Code Extensions

<details> 
<summary> Click to view instructions </summary>
</details>

### 5.2 Create `chat.prompty` (v1)

<details> 
<summary> Click to view instructions </summary>
</details>

### 5.3 Create `chat_request.py` (v1)

<details> 
<summary> Click to view instructions </summary>
</details>

### 5.4 Create `flex.flow.yaml` (app)

<details> 
<summary> Click to view instructions </summary>
</details>

### 5.5 Run your copilot app

<details> 
<summary> Click to view instructions </summary>
</details>


## 6. Evaluate A Custom Copilot

### 6.1 Understand the metrics

<details> 
<summary> Click to view instructions </summary>
</details>

### 6.2 Understand the tools

<details> 
<summary> Click to view instructions </summary>
</details>

### 6.3 Create evaluation dataset

<details> 
<summary> Click to view instructions </summary>
</details>

### 6.4 Create evaluation flow 

<details> 
<summary> Click to view instructions </summary>
</details>

### 6.5 Evaluate your copilot (v1)

<details> 
<summary> Click to view instructions </summary>
</details>


## 7. Chat with your data (RAG)

### 7.1 Understand RAG Pattern

<details> 
<summary> Click to view instructions </summary>
</details>

### 7.2 Setup AI Search Index

<details> 
<summary> Click to view instructions </summary>
</details>

### 7.3 Setup Azure CosmosDB

<details> 
<summary> Click to view instructions </summary>
</details>

### 7.4 Update `chat.prompty` (v2)

<details> 
<summary> Click to view instructions </summary>
</details>

### 7.5 Update `chat_request.py` (v2)

<details> 
<summary> Click to view instructions </summary>
</details>

### 7.6 Run your copilot application

<details> 
<summary> Click to view instructions </summary>
</details>

### 7.7 Evaluate your copilot (v2)

<details> 
<summary> Click to view instructions </summary>
</details>


## 8. Deploy & Test the Copilot

### 8.1 Understand Azure AI Studio 

<details> 
<summary> Click to view instructions </summary>
</details>

### 8.2 View Copilot Deployment

<details> 
<summary> Click to view instructions </summary>
</details>

### 8.3 Test Copilot Deployment

<details> 
<summary> Click to view instructions </summary>
</details>


## 9. Integrate with Contoso Web
### 9.1 Fork Contoso-Web Repo

<details> 
<summary> Click to view instructions </summary>
</details>

### 9.2 Launch GitHub Codespaces

<details> 
<summary> Click to view instructions </summary>
</details>

### 9.3 Set Environment Variables

<details> 
<summary> Click to view instructions </summary>
</details>

### 9.4 Preview Contoso Web 

<details> 
<summary> Click to view instructions </summary>
</details>

### 9.5 Test Contoso Web UI

<details> 
<summary> Click to view instructions </summary>
</details>

## 10. Wrap-Up

### 10.1 Cleanup Resource

<details> 
<summary> Click to view instructions </summary>
</details>

### 10.2 Star or Watch Repo

<details> 
<summary> Click to view instructions </summary>
</details>

### 10.3 Browse Resources

<details> 
<summary> Click to view instructions </summary>
</details>

