---
page_type: sample
languages:
- azdeveloper
- python
- bash
- bicep
- prompty
products:
- azure
- azure-openai
- azure-cognitive-search
- azure-cosmos-db
urlFragment: contoso-chat
name: Contoso Chat - Retail RAG Copilot with Azure AI Studio and Prompty (Python Implementation)
description: Build, evaluate, and deploy, a RAG-based retail copilot that responds to customer questions with responses grounded in the retailer's product and customer data.
---
<!-- YAML front-matter schema: https://review.learn.microsoft.com/en-us/help/contribute/samples/process/onboarding?branch=main#supported-metadata-fields-for-readmemd -->


# Contoso Chat: Retail RAG Copilot with Azure AI Studio and Prompty

[![Open in GitHub Codespaces](https://img.shields.io/static/v1?style=for-the-badge&label=GitHub+Codespaces&message=Open&color=brightgreen&logo=github)](https://github.com/codespaces/new?hide_repo_select=true&machine=basicLinux32gb&repo=725257907&ref=main&devcontainer_path=.devcontainer%2Fdevcontainer.json&geo=UsEast)
[![Open in Dev Containers](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/azure-samples/contoso-chat)

## Table of Contents

- [Overview](#overview)
- [Features](#features) · [Architecture Diagram](#architecture-diagram) 
- [Pre-Requisites](#pre-requisites)
- [Getting Started](#getting-started) 
    - [GitHub Codespaces](#github-codespaces) 
    - [VS Code Dev Containers](#vs-code-dev-containers) 
    - [Local Environment](#local-environment) 
- [Development](#development) 
- [Testing](#testing) 
- [Deployment](#deployment)
- [Guidance](#guidance) - [Region Availability](#region-availability) · [Costs](#costs) · [Security](#security)
- [Workshop](#workshop) 🆕 · [Versions](#versions)
- [Resources](#resources) · [Code of Conduct](#code-of-conduct)
· [Responsible AI Guidelines](#responsible-ai-guidelines)


## Important Security Notice 

This template, the application code and configuration it contains, has been built to showcase Microsoft Azure specific services and tools. We strongly advise our customers not to make this code part of their production environments without implementing or enabling additional security features.  

For a more comprehensive list of best practices and security recommendations for Intelligent Applications, visit our [official documentation](https://learn.microsoft.com/azure/developer/ai/get-started-securing-your-ai-app).

> [!WARNING]  
>
> **Some of the features used in this repository are in preview.** Preview versions are provided without a service level agreement, and they are not recommended for production workloads. Certain features might not be supported or might have constrained capabilities. For more information, see [Supplemental Terms of Use for Microsoft Azure Previews](https://azure.microsoft.com/en-us/support/legal/preview-supplemental-terms/).

**Sample application code is included in this project**. You can use or modify this app code or you can rip it out and include your own.

---

## Overview

_Contoso Outdoor_ is an online retailer specializing in hiking and camping equipment for outdoor enthusiasts. The website offers an extensive catalog of products - resulting in customers needing product information and recommendations to assist them in making relevant purchases.

![Contoso Outdoor](./docs/img/app-scenario-ui.png)

This sample implements _Contoso Chat_ - a retail copilot solution for Contoso Outdoor that uses a _retrieval augmented generation_ design pattern to ground chatbot responses in the retailer's product and customer data. Customers can ask questions from the website in natural language, and get relevant responses with potential recommendations based on their purchase history - with responsible AI practices to ensure response quality and safety.

![Contoso Chat](./docs/img/app-scenario-ai.png)

The sample illustrates the end-to-end workflow (GenAIOps) for building a RAG-based copilot **code-first** with Azure AI and Prompty. By exploring and deploying this sample, you will learn to:

1. Ideate and iterate rapidly on app prototypes using [Prompty](https://prompty.ai)
1. Deploy and use [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/) models for chat, embeddings and evaluation
1. Use Azure AI Search (indexes) and Azure CosmosDB (databases) for your data
1. Evaluate chat responses for quality using AI-assisted evaluation flows
1. Host the application as a FastAPI endpoint deployed to Azure Container Apps
1. Provision and deploy the solution using the Azure Developer CLI
1. Support Responsible AI practices with content safety & assessments


## Features

The project template provides the following features:

- [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/) for embeddings, chat, and evaluation models
- [Prompty](https://prompty.ai) for creating and managing prompts for rapid ideati
- [Azure AI Search](https://azure.microsoft.com/products/ai-services/ai-search) for performing semantic similarity search
- [Azure CosmosDB](https://learn.microsoft.com/azure/cosmos-db/) for storing customer orders in a noSQL database 
- [Azure Container Apps](https://learn.microsoft.com/azure/container-apps/overview) for hosting the chat AI endpoint on Azure

It also comes with:
- Sample product and customer data for rapid prototyping
- Sample application code for chat and evaluation workflows
- Sample datasets and custom evaluators using prompty assets

### Architecture Diagram 
![Architecture](./docs/img/arch-contoso-retail-aca.png)

## Pre-requisites

To deploy and explore the sample, you will need:

1. An active Azure subscription - [Signup for a free account here](https://azure.microsoft.com/free/)
1. An active GitHub account - [Signup for a free account here](https://github.com/signup)
1. Access to Azure OpenAI Services - [Learn about Limited Access here](https://learn.microsoft.com/legal/cognitive-services/openai/limited-access)
1. Access to Azure AI Search - [With Semantic Ranker](https://learn.microsoft.com/en-us/azure/search/semantic-search-overview) (premiun feature)
1. Available Quota for: `text-embedding-ada-002`, `gpt-35-turbo`. and `gpt-4`

We recommend deployments to `swedencentral` or `francecentral` as regions that can support all these models. In addition to the above, you will also need the ability to:
 - provision Azure Monitor (free tier)
 - provision Azure Container Apps (free tier)
 - provision Azure CosmosDB for noSQL (free tier)

From a tooling perspective, familiarity with the following is useful:
 - Visual Studio Code (and extensions)
 - GitHub Codespaces and dev containers
 - Python and Jupyter Notebooks
 - Azure CLI, Azure Developer CLI and commandline usage

## Getting Started

You have three options for setting up your development environment:

1. Use GitHub Codespaces - for a prebuilt dev environment in the cloud
1. Use Docker Desktop - for a prebuilt dev environment on local device
1. Use Manual Setup - for control over all aspects of local env setup

**We recommend going with GitHub Codespaces** for the fastest start and lowest maintenance overheads. Pick one option below - click to expand the section and view the details.

### GitHub Codespaces

1. You can run this template virtually by using GitHub Codespaces. Click this button to open a web-based VS Code instance in your browser:

    [![Open in GitHub Codespaces](https://img.shields.io/static/v1?style=for-the-badge&label=GitHub+Codespaces&message=Open&color=brightgreen&logo=github)](https://github.com/codespaces/new?hide_repo_select=true&machine=basicLinux32gb&repo=725257907&ref=main&devcontainer_path=.devcontainer%2Fdevcontainer.json&geo=UsEast)

1. Once the codespaces environment is ready (this can take several minutes), open a new terminal in that VS Code instance - and proceed to the [Development](#development) step.

### VS Code Dev Containers

A related option is to use VS Code Dev Containers, which will open the project in your _local Visual Studio Code editor_ using the [Dev Containers extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers):

1. Install [Docker Desktop](https://www.docker.com/products/docker-desktop) (if not installed), then start it.
1. Open the project in your local VS Code by clicking the button below:
   
    [![Open in Dev Containers](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/azure-samples/contoso-chat)

1. Once the VS Code window shows the project files (this can take several minutes), open a new terminal in that VS Code instance - and proceed to the [Development](#development) step.

### Local environment

1. **Install the required tools** in your local device:
    - [Azure Developer CLI (azd)](https://aka.ms/install-azd)
    - [Python 3.10+](https://www.python.org/downloads/)
    - [Docker Desktop](https://www.docker.com/products/docker-desktop/)
    - [Git](https://git-scm.com/downloads)

    **Note for Windows users:** If you are _not_ using a container to run this sample, note that our post-provisioning hooks make use of shell scripts. While we update scripts for different local device environments, we recommend using [git bash](https://gitforwindows.org/) to run samples correctly.

1. **Initialize the project** in your local device:
    - Create a new folder `contoso-chat` and `cd` into it
    - Run this command to download project template. Note that this command will initialize a git repository, so you do not need to clone this repository.
        ```bash
        azd init -t contoso-chat-openai-prompty
        ```
1. **Install dependencies** for the project, manually. Note that this is done for you automatically if you use the dev container options above.
    ```bash
        cd src/api
        pip install -r requirements.txt
    ```

You can now proceed to the next step - [Development](#development) - where we will provision the required Azure infrastructure and deploy the application from the template using `azd`.


## Development

Once you've completed the setup the project (using [Codespaces](#github-codespaces), [Dev Containers](#vs-code-dev-containers), or [local environment](#local-environment)) you should now have a Visual Studio Code editor open, with the project files loaded, and a terminal open for running commands. Let's verify that all required tools are installed.

```bash
az version
azd version
prompty --version
python --version
```

We can now proceed with next steps - click to expand for detailed instructions.

<details>
<summary> 1️⃣ | Authenticate With Azure </summary>

1. Open a VS Code terminal and authenticate with Azure CLI. Use the `--use-device-code` option if authenticating from GitHub Codespaces. Complete the auth workflow as guided.

    ```bash
    az login --use-device-code
    ```
1. Now authenticate with Azure Developer CLI in the same terminal. Complete the auth workflow as guided. 

    ```bash
    azd auth login --use-device-code
    ```
1. You should see: **Logged in on Azure.** This will create a folder under `.azure/` in your project to store the configuration for this deployment. You may have multiple azd environments if desired.

</details>

<details>
<summary> 2️⃣ |  Provision-Deploy with AZD </summary>

1. Run `azd up` to provision infrastructure _and_ deploy the application, with one command. (You can also use `azd provision`, `azd deploy` separately if needed)

    ```bash
    azd up
    ```
1. You will be asked for  a _subscription_ for provisioning resources, an _environment name_ that maps to the resource group, and a _location_ for deployment. Refer to the [Region Availability](#region-availability) guidance to select the region that has the desired models and quota available.
1. The `azd up` command can take 15-20 minutes to complete. Successful completion sees a **`SUCCESS: ...`** messages posted to the console. We can now validate the outcomes.
</details>

<details>
<summary> 3️⃣ | Validate the Infrastructure </summary>

1. Visit the [Azure Portal](https://portal.azure.con) - look for the `rg-ENVNAME` resource group created above
1. Click the `Deployments` link in the **Essentials** section - wait till all are completed.
1. Return to `Overview` page - you should see: **35** deployments, **15** resources
1. Click on the `Azure CosmosDB resource` in the list
    - Visit the resource detail page - click "Data Explorer"
    - Verify that it has created a `customers` database with data items in it
1. Click on the `Azure AI Search` resource in the list
    - Visit the resource detail page - click "Search Explorer"
    - Verify that it has created a `contoso-products` index with data items in it
1. Click on the `Azure Container Apps` resource in the list
    - Visit the resource detail page - click `Application Url`
    - Verify that you see a hosted endpoint with a `Hello World` message on page
1. Next, visit the [Azure AI Studio](https://ai.azure.com) portal
    - Sign in - you should be auto-logged in with existing Azure credential
    - Click on `All Resources` - you should see an `AIServices` and `Hub` resources
    - Click the hub resource - you should see an `AI Project` resource listed
    - Click the project resource - look at Deployments page to verify models
1. ✅ | **Congratulations!** - Your Azure project infrastructure is ready!
</details>


<details>
<summary> 4️⃣ | Validate the Deployment </summary>

1. The `azd up` process also deploys the application as an Azure Container App
1. Visit the ACA resource page - click on `Application Url` to view endpoint
1. Add a `/docs` suffix to default deployed path - to get a Swagger API test page
1. Click `Try it out` to unlock inputs - you see `question`, `customer_id`, `chat_history`
    - Enter `question` = "Tell me about the waterproof tents"
    - Enter `customer_id` = 2
    - Enter `chat_history` = []
    - Click **Execute** to see results: _You should see a valid response with a list of matching tents from the product catalog with additional details_.
1. ✅ | **Congratulations!** - Your Chat AI Deployment is working! 

</details>


## Testing

We can think about two levels of testing - _manual_ validation and _automated_ evaluation. The first is interactive, using a single test prompt to validate the prototype as we iterate. The second is code-driven, using a test prompt dataset to assess quality and safety of prototype responses for a diverse set of prompt inputs - and score them for criteria like _coherence_, _fluency_, _relevance_ and _groundedness_ based on built-in or custom evaluators.

<details>
<summary> 1️⃣ | Manual Testing (interactive) </summary>
<br/>

The Contoso Chat application is implemented as a _FastAPI_ application that can be deployed to a hosted endpoint in Azure Container Apps. The API implementation is defined in `src/api/main.py` and currently exposes 2 routes:
 - `/` - which shows the default "Hello from Contoso Root" message
 - `/api/create_request` - which is chat AI endpoint to test prompts
 - `/api/give_feedback` - which is a feedback endpoint to provide feedback on chat bot resposnes
 
To test locally, follow these steps:

- From VScode open the solution in dev containe
- Set the `Run and debug` configuration to `Start Contoso API(backend) and Web(fronted)`
- Click the `Run and debug` button to start the backend and frontend
- Browse to `http://localhost:3000/` to access the frontend interface and test the chat bot with the UI 

To test the API directly, you can use the Swagger UI at `http://localhost:8000/docs` to test the API directly or use [api-test.http](./api-test.http) to send requests directly from VSCode [Rest client](https://marketplace.visualstudio.com/items?itemName=humao.rest-client) extension.

1. ✅ | **Congratulations!** - You successfully tested the app locally

</details>

<details>
<summary> 2️⃣ | AI-Assisted Evaluation (code-driven) </summary>
<br/>

Testing a single prompt is good for rapid prototyping and ideation. But once we have our application designed, we want to validate the _quality and safety_ of responses against diverse test prompts. The sample shows you how to do **AI-Assisted Evaluation** using Azure AI Evalaution SDK and write back evlations score to Application Insights

- Visit the `src/api/evaluators/` folder
- Open the `eval_pipeline.py` and configure quality metrics and evaluation settings
- In VSCode Set the `Run and debug` configuration to `Python Debugger: Current File`
- Click the `Run and debug` button to run evaluation pipeline
- Check the evaluation results in Azure Applcation Insights(gen-ai-insights) workbook or Azure AI Studio Tracing View 

</details>

## Observability

This solution uses OpenTelemetry (OTEL) to collect traces, metrics, and logs. The OTEL instrumentation captures telemetry data from all HTTP requests served by this application, including the Azure Open AI endpoints, and is compatible with [OTEL Semenatic Coventions for GenAI Systems](https://opentelemetry.io/docs/specs/semconv/gen-ai/)

> [!WARNING]  
>
> **Recording message content.** The environment variable [AZURE_TRACING_GEN_AI_CONTENT_RECORDING_ENABLED](./infra/main.bicepparam)determines if the actual message contents will be recorded in the traces. By default, message contents are not recorded. To include message contents in the trace, set the environment variable to "true" (case insensitive). Any other value will ensure the message contents are not recorded.

<details>
<summary> 1️⃣ | Local Tracing(Inner Loop) </summary>

To visualize telemetry data locally, use the [Aspire Dashboard](https://aspiredashboard.com/). This solution simplifies starting and stopping Aspire Dashboard:

1. Set the environment variable `OTEL_EXPORTER_OTLP_ENDPOINT` to `http://localhost:4317` to direct all telemetry data to Aspire Dashboard.
2. In VSCode, use Terminal > Run Task > Start Aspire Dashboard or Stop Aspire Dashboard command.</br>
![Aspire Dashbaord Task](./docs/img/start-aspire-dashboard.png)
3. Follow the instructions in the terminal to open Aspire Dashboard in your local browser or visit `http://localhost:62816/` and copy the token from the terminal.

![Aspire Dashbaord](./docs/img/local-aspire-traces.png)
</details>


<details>
<summary> 2️⃣ | Azure Monitor(Outer Loop)  </summary>

After deploying the Contoso chat app in Azure, visualize telemetry data using the Application Insights workbook. This workbook helps ensure your generative AI applications run efficiently and reliably at scale. Get real-time insights into performance metrics, usage patterns, and operational efficiency. Track data like execution times, token consumption, and error rates across sessions with detailed logs and visualizations to identify bottlenecks and optimize workflows.

Additonaly this dashboard consolidates user feedback and model evaluations to help you understand the quality of responses and identify areas for improvement in your generative AI applications by session and model. 

1. Visit the Azure Portal and navigate to the Application Insights resource created by the deployment.
2. Click on the Gen-AI-Insights workbook to visualize the data.

![Overview](./docs/img/gen-ai-insights-overview.png)
<br/>
Session details view provides detailed insights per user session.
![Session Detals](./docs/img/gen-ai-insights-session-overview.png)
</details>



## Deployment

The solution is deployed using the Azure Developer CLI. The `azd up` command effectively calls `azd provision` and then `azd deploy` - allowing you to provision infrastructure and deploy the application with a single command. Subsequent calls to `azd up` (e.g., ,after making changes to the application) should be faster, re-deploying the application and updating infrastructure provisioning only if required. You can then test the deployed endpoint as described earlier.

## Guidance

### Region Availability

This template currently uses the following models: `gpt35-turbo`, `gpt-4` and `text-embedding-ada-002`, which may not be available in all Azure regions, or may lack sufficient quota for your subscription in supported regions. Check for [up-to-date region availability](https://learn.microsoft.com/azure/ai-services/openai/concepts/models#standard-deployment-model-availability) and select a region during deployment accordingly

**We recommend using `francecentral`**

### Costs

Pricing for services may vary by region and usage and exact costs are hard to determine. You can _estimate_ the cost of this project's architecture with [Azure's pricing calculator](https://azure.microsoft.com/pricing/calculator/) with these services:

- Azure OpenAI - Standard tier, GPT-35-turbo and Ada models. [See Pricing](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/)
- Azure AI Search - Basic tier, Semantic Ranker enabled. [See Pricing](https://azure.microsoft.com/en-us/pricing/details/search/)
- Azure Cosmos DB for NoSQL - Serverless, Free Tier. [See Pricing](https://azure.microsoft.com/en-us/pricing/details/cosmos-db/autoscale-provisioned/#pricing)
- Azure Monitor - Serverless, Free Tier. [See Pricing](https://azure.microsoft.com/en-us/pricing/details/monitor/)
- Azure Container Apps - Severless, Free Tier. [See Pricing](https://azure.microsoft.com/en-us/pricing/details/container-apps/)


### Security

This template uses [Managed Identity](https://learn.microsoft.com/entra/identity/managed-identities-azure-resources/overview) for authentication with key Azure services including Azure OpenAI, Azure AI Search, and Azure Cosmos DB. Applications can use managed identities to obtain Microsoft Entra tokens without having to manage any credentials. This also removes the need for developers to manage these credentials themselves and reduces their complexity.

Additionally, we have added a [GitHub Action tool](https://github.com/microsoft/security-devops-action) that scans the infrastructure-as-code files and generates a report containing any detected issues. To ensure best practices we recommend anyone creating solutions based on our templates ensure that the [Github secret scanning](https://docs.github.com/code-security/secret-scanning/about-secret-scanning) setting is enabled in your repo.

## Workshop 

The sample has a `docs/workshop` folder with step-by-step guidance for developers, to help you deconstruct the codebase, and understand how to to provision, ideate, build, evaluate, and deploy, the application yourself, with your own data. 
 - The workshop may be offered as an _instructor-guided option_ (e.g., on [Microsoft AI Tour](https://aitour.microsoft.com))
 - The workshop can be completed at home as a **self-paced lab** with your own subscription.

### Lab Guide

1. [View Workshop Online](https://aka.ms/aitour/contoso-chat/workshop) - view a pre-built workshop version in your browser
1. **View Workshop Locally** - The workshop is built using Mkdocs. To preview it locally, 
    - install mkdocs: `pip install mkdocs-material`
    - switch to folder: `cd docs/workshop`
    - launch preview: `mkdocs serve` 
    - open browser to the preview URL specified

Have issues or questions about the workshop? Submit [a new issue](https://github.com/Azure-Samples/contoso-chat/issues/new) with a `documentation` tag.


## Resources

1. [Prompty Documentation](https://prompty.ai)
1. [Azure AI Studio Documentation](https://aka.ms/aistudio)
1. [Develop AI Apps using Azure AI Services](https://aka.ms/ai-apps-docs)
1. [Azure AI Templates with Azure Developer CLI](https://aka.ms/ai-studio/azd-templates)


## Code of Conduct

This project has adopted the [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/). Learn more here:

- [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/)
- [Microsoft Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/)
- Contact [opencode@microsoft.com](mailto:opencode@microsoft.com) with questions or concerns

For more information see the [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) or
contact [opencode@microsoft.com](mailto:opencode@microsoft.com) with any additional questions or comments.

## Responsible AI Guidelines

This project follows below responsible AI guidelines and best practices, please review them before using this project:

- [Microsoft Responsible AI Guidelines](https://www.microsoft.com/en-us/ai/responsible-ai)
- [Responsible AI practices for Azure OpenAI models](https://learn.microsoft.com/en-us/legal/cognitive-services/openai/overview)
- [Safety evaluations transparency notes](https://learn.microsoft.com/en-us/azure/ai-studio/concepts/safety-evaluations-transparency-note)

---




