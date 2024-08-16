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

## 3. Provision Infrastructure

If you are participating in a live AI Tour workshop, you can skip ahead to Section 4.

### 3.0 Pre-Requisites

These are the resources and skill requirements for the workshop. **Note that in the case of the AI Tour, the subscription and infrastructure requirements will be taken care of for you.** For all others, you will need to verify you can meet all requirements. 

1. Azure Subscription - Signup for a free account.
1. Visual Studio Code - Download it for free.
1. GitHub Account - Signup for a free account.
1. [Access to Azure Open AI Services](https://learn.microsoft.com/en-us/azure/ai-services/openai/overview#how-do-i-get-access-to-azure-openai) - Learn about requirements.
1. [Azure OpenAI Model Quota](https://learn.microsoft.com/en-us/azure/ai-services/openai/quotas-limits) - We use `gpt-4`, `gpt-35-turbo` and `text-embedded-ada-002`
1. Standard tier of Azure AI Service - Required for Semantic Ranker
1. Machine to run deployment commands. You can launch Codespaces on this repository, or use your own hardware with a `bash` shell.

### 4.1 Fork Contoso Chat Repo

<details> 
<summary> Click to view instructions </summary>
</details>

### 4.2 Launch GitHub Codespaces

<details> 
<summary> Click to view instructions </summary>
</details>

### 4.3 Authenticate with Azure

<details> 
<summary> Click to view instructions </summary>
</details>


### 3.1 Clone the GitHub repository

```
git clone https://github.com/Azure-Samples
```

### 3.2 Self-Deploy Option

Execute the following commands a `bash` shell from the root directory of your cloned repository.

1. Log in using your Azure subscription credentials

```
azd auth login --use-device-code
```

Log into the Azure subscription you will use to deploy resources. 

```
azd up
```
    - For Environment Name, enter: CONTOSOCHAT
      - (You are free to choose a different name, for example if you already have resources with that name.)
    - For Subscription, select the default (your logged-in Azure subscription)    
    - For Azure Region we recommend: France Central (francecentral)

This process will take around 30--40 minutes to complete.

### 3.3 Pre-Provision Option 

<details> 
<summary> Click to view instructions </summary>
</details>

## 4. Setup Dev Environment

### 4.4 Verify Environment Vars

<details> 
<summary> Click to view instructions </summary>
</details>

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

### 8.1 Understant Azure AI Studio 

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

