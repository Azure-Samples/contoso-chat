[🏠 Table Of Contents](#table-of-contents) ⎯ [⚙️ Appendix](#appendix)

---

## Hello @lab.User.FirstName 👋🏽. 

This is a proctored 45-min lab on **Build, Evaluate & Deploy a RAG-based retail copilot with Azure AI** associated with the 1-hour instructor-led [Lab322 Session](https://build.microsoft.com/sessions/852fa54a-9756-4681-8cd5-ae9632b635ca) offered once daily at Microsoft Build 2024. 

> [+hint]
> Familiarize yourself with the instructor and proctors for this session. Lab instructions are organized in numbered sections and steps to make them easier to reference when asking questions.

## Pre-requisites

> [+alert]
> You must have the following to participate in this lab:

 * A **GitHub Account** for GitHub Codespaces usage. (mandatory) 
 * Familiarity with **Python and Jupyter Notebooks**.
 * Familiarity with **Azure**, **Visual Studio Code** and **GitHub**.

## Table Of Contents

- [**Lab Overview**](#lab-overview)
    - [01. Get Started](#1-get-started)
    - [02. Launch GitHub Codespaces](#2-launch-github-codespaces)
    - [03. Verify Azure Is Provisioned](#3-verify-azure-is-provisioned)
    - [04. VSCode Azure Login](#4-vscode-azure-login)
    - [05. VSCode Azure Config](#5-vscode-azure-config)
    - [06. VSCode Config Env](#6-vscode-config-env)
    - [07. VSCode Populate Search](#7-vscode-populate-search)
    - [08. VSCode Populate Database](#8-vscode-populate-database)
    - [09. VSCode Config Connections](#9-vscode-config-connections)
    - [10. Azure Config Connections](#10-azure-config-connections)
    - [11. PromptFlow Explore Codebase](#11-promptflow-explore-codebase)
    - [12. PromptFlow Open Visual Editor](#12-promptflow-open-visual-editor)
    - [13. PromptFlow Run Flow ](#13-promptflow-run-flow)
    - [14. PromptFlow Evaluate Flow](#14-promptflow-evaluate-flow)
    - [15. Push PromptFlow To Azure ](#15-push-promptflow-to-azure)
    - [16. PromptFlow Deploy Flow](#16-promptflow-deploy-flow)
    - [**Lab Recap**](#lab-recap)
- [**Appendix**](#appendix)

===

[🏠 Table Of Contents](#table-of-contents) ⎯ [⚙️ Appendix](#appendix)

---

## Lab Overview

This lab gives you hands-on experience with **End-to-End LLM Application Development (LLMOps)** by teaching you to _build, run, evaluate, and deploy_ a RAG-based application ("Contoso Chat") using **Azure AI Studio** and **Prompt Flow**.

## Learning Objectives

By the end of this lab, you should be able to:

1. Explain **LLMOps** concepts & benefits.
1. Explain **Prompt Flow** concept & benefits.
1. Explain **Azure AI Studio** features & usage.
1. Use **Prompt Flow** on Visual Studio Code
1. Design **RAG-based LLM Applications**
1. Build, run, evaluate & deploy RAG-based LLM apps **on Azure**.


## Pre-Requisites

The lab environment is pre-configured with an Azure subscription **and pre-provisioned with the required Azure resources** to jumpstart your journey. We assume some familiarity with the following concepts:
1. Machine Learning & Generative AI _concepts_
1. Python & Jupyter Notebook _programming_
1. Azure, GitHub & Visual Studio Code _tooling_

## Development Environment

You'll use the following resources in this lab:
 - [Contoso Chat](https://github.com/Azure-Samples/contoso-chat) - as the target application.
 - [Github Codespaces](https://github.com/codespaces) - as the dev container
 - [Visual Studio Code](https://code.visualstudio.com/) - as the default editor
 - [Azure AI Studio (Preview)](https://ai.azure.com) - for AI projects
 - [Azure ML Studio](https://ml.azure.com) - for minor configuration
 - [Azure Portal](https://portal.azure.com) - for managing Azure resources
 - [Prompt Flow](https://github.com/microsoft/promptflow) - for streamlining end-to-end LLM app dev

===

[🏠 Table Of Contents](#table-of-contents) ⎯ [⚙️ Appendix](#appendix)

---

## 1. Get Started


> [!hint] 
> **First time using Skillable?** Tip: The green "T" (e.g., +++**@lab.VirtualMachine(BuildBaseVM).Username**+++) indicate values that are _automatically input for you_ at the current cursor location in VM, with one click. This reduces your effort and minimizes input errors.

**Let's get started by logging into the VM and organizing our space!**

-  [] **01** | Log in using these credentials.
    - Username: will already be set to **@lab.VirtualMachine(BuildBaseVM).Username**.
    - Password: enter +++**@lab.VirtualMachine(BuildBaseVM).Password**+++ and click.
    - You should see: _A Windows 11 Desktop._

* []  **02** | Launch the Edge Browser
    - Open it in full-screen mode.
    - All workshop tasks will happen in-browser.

* []  **03** | Open Azure Portal in a new tab and authenticate.
    - Navigate to  +++**https://portal.azure.com**+++ in a new tab.
    - You should see: _A Microsoft Azure login dialog_.
    - Enter Username: +++**@lab.CloudPortalCredential(User1).Username**+++
    - Enter Password: +++**@lab.CloudPortalCredential(User1).Password**+++ and click.
    - You should see: _Your Azure Subscription home page._
    - **This is your Azure Portal tab**. Leave it open.
    
* []  **04** | Open Azure AI Studio in a new tab.
    - Navigate to +++**https://ai.azure.com**+++ in a new tab.
    - Click the _Sign in_ button. (no need to re-enter Username/Password)
    - You should see: _You are logged in with your Azure profile._
    - **This is your Azure AI Studio tab**. Leave it open.

* []  **05** | Open Azure ML Studio in a new tab.
    - Navigate to +++**https://ml.azure.com**+++ in a new tab
    - You should see: _You are already logged in with your Azure profile._
    - **This is your Azure ML Studio tab**. Leave it open.

You should now have a full-screen browser with 3 tabs open - to Azure Portal, Azure AI Studio and Azure ML Studio respectively. We'll use each of these at specific points in the workshop so leave them open and let's move on. 

---

🥳 **Congratulations!** <br/>  You successfully logged into Azure and Azure AI platform sites!!

===

[🏠 Table Of Contents](#table-of-contents) ⎯ [⚙️ Appendix](#appendix)

---

## 2. Launch GitHub Codespaces 

This workshop will use the [Azure-Samples/contoso-chat](https://aka.ms/aitour/contoso-chat) sample as the base. This is configured with "devcontainer.json" - meaning you can launch it in GitHub Codespaces to get a pre-built development environment with no added effort.

> [!Important] **Note:** You will need a GitHub account to use GitHub Codespaces. **We recommend using a personal account (or a secondary account that is not linked to your corporate profile) for this purpose**. You will be able to complete the workshop within the free GitHub Codespaces quota available for personal accounts.

* []  **01** | Log into GitHub
    - Open a new browser tab
    - Navigate to  +++**https://aka.ms/aitour/contoso-chat**+++
    - **Login using _your_ GitHub credentials.**

> [!note] 
> **Note:** If you use a GitHub Enterprise account that requires single sign-on authentication, authentication may fail. In that case, [create a free GitHub account here](https://github.com/signup) and use that instead.

* []  **02** | Fork the repo into your profile
    - Navigate to +++**https://aka.ms/aitour/contoso-chat**+++
    - Click the fork button the repo
    - Check "Copy the 'main' branch" only
    - Click "Create fork"
    - Wait for the fork to complete in your profile.

* []  **03** | Launch a Codespace
    - In your forked repo, click _'Code'_ dropdown
    - Select the "Codespaces" tab (next to the "Local" tab)
    - Click _"Create codespace on main"_
    - You should see a new browser tab: _'Setting up your codespace'_
    - In 3-4 minutes, this will be replaced by an interface resembling Visual Studio code, but running in the browser.

You should now have a _fourth browser tab_ with GitHub Codespaces running. Keep this tab open. **This is your Visual Studio Code tab**.


---

🥳 **Congratulations!** <br/> Your development environment is ready!


===

[🏠 Table Of Contents](#table-of-contents) ⎯ [⚙️ Appendix](#appendix)

---

## 3. Verify Azure Is Provisioned

> [!note] 
> Your Azure subscription should come pre-configured with resources for the workshop. Let's check this.


* []  **01** | Check that your subscription is pre-provisioned.
    - Switch to your Azure Portal tab - +++**https://portal.azure.com**+++
    - Click the _'Resource Groups'_ option
    - Verify that a Resource Group called **contoso-chat-rg** is listed.
* []  **02** | Click the Resource Group to view details. 
    - Verify it contains the following resources (refer to the "Type" column in the table).
        - an "Azure AI hub" resource
        - an "Azure AI services" resource
        - an "Azure AI project" resource
        - a "Search service" (Azure AI Search) resource
        - a "Azure Cosmos DB account" resource

* []  **03** | Check that required models were deployed
    - Switch to your Azure AI Studio tab - +++**https://ai.azure.com**+++
    - Click on the **Build** tab to see the list of AI projects
    - Click the listed AI project for details. 
    - Click on the **Deployments** item in the sidebar to see Deployments
    - **You may need to Refresh the list** to see updates.
    - Verify that the following models are listed
        - gpt-35-turbo
        - gpt-4
        - text-embedding-ada-002
* []  **04** | Check that required connections were created
    - Click the **Settings** icon on the sidebar (bottom left)
    - Look for the **Connections** panel and click **View all**
    - Verify that the listed connections have **these two names**
        - contoso-search
        - aoai-connection
    - We create the third connection (contoso-cosmos) later.


---

🥳 **Congratulations!** <br/> Your Azure subscription is provisioned correctly!



===

[🏠 Table Of Contents](#table-of-contents) ⎯ [⚙️ Appendix](#appendix)

---

## 4. VSCode Azure Login

> [!note] 
> Our development environment comes pre-configured with the Azure CLI (`az`) that we can now use from the command-line, to authenticate our Visual Studio Code session with Azure.

* []  **01** | Visit the browser tab where you launched GitHub Codespaces.
    - You should see a Visual Studio Code editor 
    - You should see a terminal open in editor

> [!hint]
> If the Visual Studio Code Terminal is not open at this time, just click the hamburger menu (top left). Then look for the _Terminal_ option & Open a New Terminal.

* []  **02** | Use Azure CLI from terminal, to login
    - Enter command: +++az login --use-device-code+++ 
    - Open +++https://microsoft.com/devicelogin+++ in new tab
    - Copy-paste code from Azure CLI into the dialog you see here
    - On success, close this tab and return to VS Code tab

---

🥳 **Congratulations!** <br/> You're logged into Azure on VS Code.

===

[🏠 Table Of Contents](#table-of-contents) ⎯ [⚙️ Appendix](#appendix)

---

## 5. VSCode Azure Config

> [!note] 
> Your Azure subscription comes with pre-provisioned resources for this workshop. Let's take a minute to copy the configuration details to our local environment, so we can use them from our code later.

* []  **01** | Download the 'config.json' for this Azure AI project
    - Visit +++https://portal.azure.com+++ in a new browser tab
    - Click on your created resource group (_contoso-chat-rg_)
    - Click on your Azure AI project resource (_contoso-chat-aiproj_) 
    - Look for the **download config.json** option under Overview
    - Click to download the file to the Windows 11 VM 
    - Open the file and **Copy** the contents to clipboard.

* []  **02** | Update your VS Code project with these values
    - Switch browser tab to your Visual Studio Code editor
    - Open VS Code Terminal, enter: +++touch config.json+++
    - This creates an empty config.json file in root directory.
    - Open file in VS Code and **Paste** data from clipboard
    - Save the file.

---

🥳 **Congratulations!** <br/> You're configured to use Azure from VS Code.

===

[🏠 Table Of Contents](#table-of-contents) ⎯ [⚙️ Appendix](#appendix)

---

## 6. VSCode Config Env

> [!hint]
_We'll now configure service endpoints and keys as env vars for programmatic access from Jupyter Notebooks. This step requires Copy-Paste actions. If you have trouble pasting into the VS Code window, right-click and choose **Paste** from the menu._

* []  **01** | Keep your Visual Studio Code editor open in one tab
    - Open VS Code Terminal, enter: +++cp .env.sample .env+++
    - This should copy "local.env" to a new **.env** file.
    - Open ".env" in Visual Studio Code, keep tab open.

> [!warning]
Your Virtual Machine will have a _local.env_ file on the desktop. **If you don't see that file, skip to step 03 | Update the Azure OpenAI environment variables** below

* []  **02** | Copy pre-existing _local.env_ values to **.env**
    - Delete the contents of .env file created above (Ctrl-A, DEL)
    - Open the file _local.env_ on your desktop in Notepad 
    - Copy its entire contents to the clipboard (Ctrl-A, Ctrl-C)
    - Paste the clipboard contents into **.env** (Control-V)
    - Save the **.env** file.

🥳 **Congratulations!** <br/> Your VS Code env variables are updated!
You can skip the remaining sections below, and advance to the next page.

---
<br/>

> [!warning]
**Do the steps below only if you were unable to do step 02.** If you did not have a pre-existing _local.env_ file and need to configure the values manually, continue from here.

> [!hint] 
To configure values, replace the placeholders (e.g. `<YOUR_OPEN_AI_KEY>`) by **deleting them first** then copying in values. Do **NOT** retain the < and > brackets.

* []  **03** | Update the Azure OpenAI environment variables
    - Open +++https://ai.azure.com+++ in a new tab
    - Click **"Build"**, then open your AI project page.
    - Click **"Settings"**, click **"Show endpoints"** in the first tile
    - Copy **Azure.OpenAI** endpoint value, <br/> To "CONTOSO_AI_SERVICES_ENDPOINT" value in ".env"
    - Copy **Primary key** value <br/> To "CONTOSO_AI_SERVICES_KEY" value in ".env"

* []  **04** | Update the Azure AI Search environment variables
    - Open +++https://portal.azure.com+++ in a new tab
    - Open your Azure AI Search **"Search service"** resource page (_search-contosoXXXXX_)
    - Copy **Uri** value under Overview page <br/> To "CONTOSO_SEARCH_ENDPOINT" in ".env"
    - Navigate to the **"Keys"** blade (left pane) and copy **Primary admin key** to "CONTOSO_SEARCH_KEY" in ".env"

* []  **05** | Locate the Azure CosmosDB environment variables
    - Open +++https://portal.azure.com+++ in a new tab
    - Open your **Azure Cosmos DB account** resource page
    - Navigate to the **Keys** blade from the left pane
    - Copy **URI** value, <br/> To "COSMOS_ENDPOINT" value in ".env"
    - Copy **PRIMARY KEY** value <br/> To "COSMOS_KEY" value in ".env"

* []  **06** | Save the ".env" file.

---

🥳 **Congratulations!** <br/> Your VS Code env variables are updated!

===

[🏠 Table Of Contents](#table-of-contents) ⎯ [⚙️ Appendix](#appendix)

---

## 7. VSCode Populate Search

> [!NOTE]
_This assumes you setup the Azure AI Search resource earlier. In this section, we'll populate it with product data and create the index._

* []  **01** | Return to the Visual Studio Code editor tab
    - Locate the "data/product_info/" folder
    - Open the **create-azure-search.ipynb** Jupyter Notebook.

* []  **02** | Run the notebook to populate search index
    - Click **Select Kernel** (top right)
    - Pick "Python Environments" and select recommended option
    - Click **Clear All Outputs** then **Run All**
    - Verify that all code cells executed correctly.

* []  **03** | Verify the search index was created
    - Open +++https://portal.azure.com+++ to Azure AI Search resource
    - Click the **Indexes** option in sidebar to view indexes
    - Verify that the **contoso-products** search index was created.

---

🥳 **Congratulations!** <br/> Your Azure AI Search index is ready!

===

[🏠 Table Of Contents](#table-of-contents) ⎯ [⚙️ Appendix](#appendix)

---

## 8. VSCode Populate Database

> [!NOTE]
_This assumes you setup the Azure CosmosDB resource earlier. In this section, we'll populate it with customer data._

* []  **01** | Return to the Visual Studio Code editor tab
    - Locate the "data/customer_info/" folder
    - Open the **create-cosmos-db.ipynb** Jupyter Notebook.

* []  **02** | Run the notebook to populate customer database
    - Click **Select Kernel**, set recommended Python environment 
    - Click **Clear All Outputs** then **Run All** & verify completion

* []  **03** | Verify the customer database was created
    - Open +++https://portal.azure.com+++ to Azure CosmosDB resource
    - Click the **Data Explorer** option in sidebar to view data
    - Verify that the **contoso-outdoor** container was created
    - Verify that it contains a **customers** database

---

🥳 **Congratulations!** <br/> Your Azure CosmosDB database is ready!

===

[🏠 Table Of Contents](#table-of-contents) ⎯ [⚙️ Appendix](#appendix)

---

## 9. VSCode Config Connections

> [!NOTE]
_This assumes you completed all Azure resource setup and VS Code configuration for those resources. Now let's setup **local Connections** so we can run the prompt flow in VS Code later._

* []  **01** | Return to the Visual Studio Code editor tab

* []  **02** | Setup a local third-party backend to store keys
    - Open the Visual Studio Code terminal 
    - Type +++pip install keyrings-alt+++ and hit Enter
    - Installation should complete quickly

* []  **03** | Run the notebook to set local prompt flow connections
    - Locate the "connections/" folder
    - Open the **create-connections.ipynb** Jupyter Notebook.
    - Click **Select Kernel**, set recommended Python environment 
    - Click **Clear All Outputs** then **Run All** & verify completion

* []  **04** | Validate connections were created
    - Return to Visual Studio Code terminal
    - Type +++pf connection list+++ and hit Enter
    - Verify 3 connections were created *with these names* <br/> **"contoso-search", "contoso-cosmos", "aoai-connection"**

---

🥳 **Congratulations!** <br/> Your *local connections* to the Azure AI project are ready!

===

[🏠 Table Of Contents](#table-of-contents) ⎯ [⚙️ Appendix](#appendix)

---

## 10. Azure Config Connections

We've configured our local connections. Now it's time to do the same in the cloud, so we can use them in the later steps for deployment. In the earlier step, we verified that two of three connections are already setup for us, namely _contoso-search_ and _aoai-connection_. We just need to **create the custom connection** for _contoso-cosmos_.

> [!IMPORTANT]
> _This is a custom connection you will need to setup manually_. **Note that it uses Azure ML Studio (for now).** We expect this to change in future to allow all connections to be provisioned from Azure AI Studio instead.

* []  **01** | Create the **Custom Connection** (+++contoso-cosmos+++) 
    - Visit +++https://ml.azure.com+++ 
    - Under **Recent Workspaces**, click project (_contoso-chat-aiproj_)
    - Select **Prompt flow** (sidebar), then **Connections** (tab)
    - Click **Create** and select **Custom** from dropdown
    - **Name**: +++contoso-cosmos+++
    - **Provider**: Custom (default)
    - **Key-value pairs**: Add 4 entries (get env var values from .env)
        - key: +++key+++, <br/> value: use the "COSMOS_KEY" value from .env <br/> **check "is secret"**
        - key: +++_endpoint_+++ , <br/> value: use the "COSMOS_ENDPOINT" value from .env 
        - key: +++_containerId_+++, value: +++customers+++
        - key: +++_databaseId_+++, value: +++contoso-outdoor+++
    - Click **Save** to complete step. 
    
* []  **02** | Let's verify all three connections now exist in Azure AI Studio
    - Visit +++https://ai.azure.com+++ and navigate to "Build".
    - Select your Azure AI project from list, click to see details page.
    - Click **Settings** icon (sidebar, bottom left)
    - Look for the **Connections** panel and click **View all**
    - Verify that you see all 3 connections:
        - contoso-search
        - aoai-connection
        - contoso-cosmos

---

🥳 **Congratulations!** <br/> Your *cloud connections* to the Azure AI project are ready!

===

[🏠 Table Of Contents](#table-of-contents) ⎯ [⚙️ Appendix](#appendix)

---

## 11. PromptFlow Explore Codebase

> [!NOTE]
> Our environment, resources and connections are configured. Now, let's learn about prompt flow and how it works. A **prompt flow is a DAG (directed acyclic graph)** made of up **nodes** connected together in a **flow**. Each node is a **function tool** (written in Python) that can be edited and customized to suit your needs.

* []  **01** | Let's explore the Prompt Flow extension
    - Click the "Prompt Flow" icon in the Visual Studio Code sidebar (**Note:** The Prompt Flow icon is a _stylized "P"_ and may be hidden behind a "..." icon in the Visual Studio Code sidebar on devices with smaller display sizes)
    - You should see a slide-out menu with the following sections
        - **Quick Access** - Create new flows, install dependencies etc,
        - **Flows** - Lists flows in project (defined by _flow.dag.yaml_)
        - **Tools** - Lists available _function_ tools (used in flow nodes)
        - **Batch Run History** - flows run against data or other runs
        - **Connections** - Lists connections & helps create them
    - We'll revisit this later as needed, when executing prompt flows.

* []  **02** | Let's understand prompt flow folders & structure
    - Click the "Explorer" icon (top icon in the Visual Studio Code sidebar)
    - Promptflow can create [three kinds of flows](https://microsoft.github.io/promptflow/how-to-guides/init-and-test-a-flow.html#initialize-flow):
        - standard = basic flow folder structure
        - chat = enhances standard flow for **conversations**
        - evaluation = special flow, **assesses** outputs of other flows
    - Explore the "contoso_chat" folder for a chat flow:
        - **flow.dag.yaml** - defines the flow (inputs, outputs, nodes)
        - **source code** (.py, .jinja2) - function _tools_ used by flow
        - **requirements.txt** - defines Python dependencies for flow
    - Explore the "eval/" folder for examples of eval flows
        - **eval/groundedness** - tests for single metric (groundedness)
        - **eval/multi_flow** - tests for multiple metrics (groundedness, fluency, coherance, relevance)
        - **eval/evaluate-chat-prompt-flow.ipynb** - shows how these are used to evaluate the_contoso_chat_ flow.

* []  **03** | Let's explore a prompt flow in code
    - Open Visual Studio Code file: _contoso-chat/**flow.dag.yaml**_ 
    - You should see a declarative file with these sections:
        - **environment** - requirements.txt to install dependencies
        - **inputs** - named inputs & properties for flow 
        - **outputs** - named outputs & properties for flow 
        - **nodes** - processing functions (tools) for workflow

The "prompt flow" is defined by the **flow.dag.yaml** but the text view does not help us understand the "flow" of this process. Thankfully, the Prompt Flow extension gives us a **Visual Editor** that can help. Let's explore it.

---

🥳 **Congratulations!** <br/> You're ready to explore a prompt flow visually!

===

[🏠 Table Of Contents](#table-of-contents) ⎯ [⚙️ Appendix](#appendix)

---

## 12. PromptFlow Open Visual Editor

> [!hint]
> In the previous section, you should have opened Visual Studio Code, navigated to the _contoso-chat_ folder, and opened the _flow.dag.yaml_ file in the editor pane. We also assume you have the _Prompt Flow_ extension installed correctly (see VS Code extensions sidebar).
    
* []  **01** | View _contoso-chat/flow.dag.yaml_ in the Visual Studio Code editor
    - Make sure your cursor is at the top of the file in editor panel.
    - You should see a line of menu options similar to the image below. _Note: This is an example and not an exact screenshot for this project_. **It may take a couple of seconds for the menu options to appear** so be patient.
    ![Visual Editor](https://github.com/Azure-Samples/contoso-chat/raw/main/images/visualeditorbutton.png)

* []  **02** | Click _Visual editor_ link **or** use keyboard shortcut: <kbd>Ctrl + k<kbd>,<kbd>v<kbd> 
    - You should get a split screen view with a visual graph on the right and sectioned forms on the left, as show below. _Note: This is an example and not an exact screenshot for this project_.
    ![](https://github.com/Azure-Samples/contoso-chat/raw/main/images/promptflow.png)
    - Click on any of the "nodes" in the graph on the right
        - The left pane should scroll to the corresponding declarative view, to show the node details.
        - Let's explore **our** prompt flow components visually, next.

* []  **03** | Explore prompt flow **inputs**. These start the flow.
    - **customer_id** - to look up customer in CosmosDB
    - **question** - the question that customer is asking
    - **chat_history** - the conversation history with customer

* []  **04** | Explore prompt flow **nodes**. These are the processing functions.
    - **queston_embedding** - use _embedding model_ to embed question text in vector search query
    - **retrieve_documents** - uses query to retrieve most relevant docs from AI Search index
    - **customer_lookup** - looks up customer record in parallel, from Azure Cosmos DB database
    - **customer_prompt** - populate customer prompt "template" with customer & search results
    - **llm_response** - uses _chat completion model_ to generate a response to customer query using this enhanced prompt
* []  **04** | Explore prompt flow **outputs**. These end the flow.
    - Returns the LLM-generated response to the customer

This defines the _processing pipeline_ for your LLM application from user input, to returned response. To _execute_ the flow, we need a valid Python runtime. We can use the default runtime available to use in GitHub Codespaces to run this from Visual Studio Code. Let's do that next.

---

🥳 **Congratulations!** <br/> You're ready to run your Prompt flow.

===

[🏠 Table Of Contents](#table-of-contents) ⎯ [⚙️ Appendix](#appendix)

---

## 13. PromptFlow Run Flow

> [!hint]
> Let's now return to the Visual Studio Code editor from the earlier step. It should still be in the _contoso-chat_ folder, with the_flow.dag.yaml_ opened in the Visual Editor view. Let's now try to **run the prompt flow in our local environment** and verify that it works.

> [!warning]
> On occasion, you may see an error that indicates the prompt flow failed. Scroll down to the bottom of this section for troubleshooting possible issues. It will likely be due to connection setup issues or some issue with prompt flow properties. **Ask your instructor or proctor for help if necesssary**.

* []  **01** | View _contoso-chat/flow.dag.yaml_ in the Visual Studio Code editor
    - Make sure your cursor is at the top of the file in editor panel.
    - Make sure you are in the Visual editor with a view like this. _Note: this is an example screenshot, and not the exact one for this lab_.
        ![](https://github.com/Azure-Samples/contoso-chat/raw/main/images/promptflow.png)
    
* []  **02** | Run the prompt flow locally
    - _Tip:_ Keep VS Code terminal open to view console output. 
    - Look at the 2nd line (starting with **"+LLM"**) in Visual Editor.
    - Look for a 'tool' icon at right: _It should show a valid Python env_.
    - Look for a 'play' icon next to it: _The tooltip should read "Run All"_.
    - Click _Run All_ (or use "<kbd>Shift</kbd> + <kbd>F5</kbd>" on keyboard)
    - Select "Run it with standard mode" in dropdown
    
* []  **03** | Explore inputs and outputs of flow
    - The _Inputs_ section will have these values:
        - **chat_history**: prior turns in chat (default=blank)
        - **question**: customer's most recent question
        - **customerid**: to help look up relevant customer context (e.g., order history) to refine response with more relevant context. This is the basis for RAG (retrieval-augmented generation).
    - The _Contoso Outdoors_ web app provides these inputs (in demo)
    - Note the contents of the _Flow run outputs_ tab under "Outputs" section
        - Use the navigation tools to show the **complete answer**: _Is it a good answer to the input question?_
        - Use the nvaigation tools to explore the **returned context** (products relevant to the customer's question). _Are these good selections for context?

* []  **04** | Explore Individual Flow Nodes
    - Observe node status colors in VS Code (green=success, red=error)
    - Click any node. The left pane will scroll to show execution details.
    - Click the _Code:_ link in component to see function executed here.

* []  **05** | Explore Run Stats & Traces
    - Click the "Terminal" tab. It should show final response returned. 
    - Click the "Prompt Flow" tab. Select a node in visual editor.
        - Tab shows "node name, Tokens, duration" stats for node.
        - Click the line in table. You should see more details in pane.

* []  **06** | Try a new input
    - In Inputs, **change question** to _"What is a good tent for a beginner?"_
    - Click **Run All**, explore outputs as before.
    - In Inputs, **change customerId** (to value between 1 and 12)
    - Click **Run All**, compare this output to before.
    - Experiment with other input values and analyze outputs.

> [!warning]
> **TROUBLESHOOTING TIPS**:

1. **Update AOAI Connection**. Sometimes the Azure OpenAI key gets set incorrectly. Let's fix it.
    - Click the prompt flow extension icon in the VS Code editor
    - Scroll down to the **Connections** pane in the activity bar that slides out
    - Identify the **aoia-connection** listed under Azure OpenAI Connections
    - Right click and select **Update Connection**
    - Follow the text guidance to update just the connection key
    - Enter the new value of the key from the "CONTOSO_AI_SERVICES_KEY" in **.env**.
    - Run thee flow to see if error is fixed.

1. **Fix Deployment Name**. Check if a failing node has an empty _deployment name_. Let's fix it.
    - Click the failing node in the visual editor to open the corresponding details pane
    - Look for the deployment name property
    - If present, check that the value is not empty.
    - If value is empty, click to see if the valid value shows up, and select it.
    - Run the flow to see if error is fixed. 

---

🥳 **Congratulations!** <br/> You ran your contoso-chat prompt flow successfully in the local runtime on GitHub Codespaces. Next, we want to _evaluate_ the performance of the flow.

===

[🏠 Table Of Contents](#table-of-contents) ⎯ [⚙️ Appendix](#appendix)

---

## 14. PromptFlow Evaluate Flow

> [!NOTE]
> You've built and run the _contoso-chat_ prompt flow locally using the Visual Studio Code Prompt Flow extension and SDK. Now it's time to **evaluate** the quality of your LLM app response to see if it's performing up to expectations. Let's dive in.

* []  **01** | First, run **evaluate-chat-prompt-flow.ipynb**
    - Locate the "eval/" folder
    - Open **evaluate-chat-prompt-flow.ipynb**.
    - Click **Select Kernel**, use default Python env
    - Click **Clear All Outputs**, then **Run All** 
    - Execution **takes some time**. Until then ....

* []  **02** | Let's explore what the notebook does
    - Keep Jupyter notebook open "Editor" pane
    - Open VS Code "Explorer" pane, select **Outline**
    - You should see these code sections:
        - Local Evaluation - **Groundedness**
        - Local Evaluation - **Multiple Metrics**
        - AI Studio Azure - **Batch run, json dataset**
        - Cloud Evaluation - **Multi-flow, json dataset**
    - Let's understand what each does.

* []  **03** | Local Evalution : Explore **Groundedness**
    - Evaluates **contoso-chat** for _groundedness_ 
    - This [**measures**](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in#ai-assisted-groundedness-1) how well the model's generated answers align with information from the source data (user-defined context).
    - **Example**: We test if the answer to the question _"Can you tell me about your jackets"_ is grounded in the product data we indexed previously. 

* []  **04** | Local Evaluation : Explore **Multiple Metrics**
    - Evaluates **contoso-chat** using [4 key metrics](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in#metrics-for-multi-turn-or-single-turn-chat-with-retrieval-augmentation-rag):
    - **Groundedness** = How well does model's generated answers align with information from the source (product) data?
    - **Relevance** = Extent to which the model's generated responses are pertinent and directly related to the given questions.
    - **Coherence** = Ability to generate text that reads naturally, flows smoothly, and resembles human-like language in responses.
    - **Fluency** = Measures the grammatical proficiency of a generative AI's predicted answer.

> [!NOTE]
> The above evaluation tests ran against a single test question. For more comprehensive testing, we can use Azure AI Studio to run **batch tests** using the same evaluation prompt, with the **data/salestestdata.jsonl** dataset. Let's understand how that works.

* []  **05** | Base Run : **With evaluation JSON dataset**
    - Use Azure AI Studio with automatic runtime
    - Use "data/salestestdata.jsonl" as _batch test data_
    - Do a _base-run_ using contoso-chat prompt flow
    - View results in notebook - visualized as table

* []  **06** | Eval Run : **With evaluation JSON dataset**
    - Use Azure AI Studio with automatic runtime
    - Use "data/salestestdata.jsonl" as _batch test data_
    - Do multi-flow eval with _base run as variant_
    - View results in notebook - visualized as table
    - Results should now show the 4 eval metrics
    - Optionally, click **Web View** link in final output
        - See **Visualize outputs** (Azure AI Studio)
        - Learn more on [viewing eval results](https://learn.microsoft.com/azure/ai-studio/how-to/flow-bulk-test-evaluation#view-the-evaluation-result-and-metrics)

* []  **07** | Review Evaluation Output
    - Check the Jupyter Notebook outputs
    - Verify execution run completed successfully
    - Review evaluation metrics to gain insight  

---

🥳 **Congratulations!** <br/> You've evaluated your contoso-chat flow for single-data and batch data runs, using single-metric and multi-metric eval flows. _Now you're ready to deploy the flow so apps can use it_. 
===

[🏠 Table Of Contents](#table-of-contents) ⎯ [⚙️ Appendix](#appendix)

---

## 15. Push PromptFlow To Azure

>[!note] 
> We can run the prompt flow in local (Visual Studio Code) and cloud (Azure) runtime environments. In this section, we'll push the prompt flow to the cloud and validate that it runs there, so it is ready for the _Deployment_ step later. 

* []  **01** | Return to the Visual Studio Code tab
    - Locate the "deployment/" folder
    - Open **push_and_deploy_pf.ipynb**.
    - Click **Select Kernel**, use default Python env
    - Click **Clear All Outputs**, then **Run All** 
    - This should complete in just a few minutes.

* []  **02** | Verify Prompt Flow was created
    - Click the **flow_portal_url** link in output
    - It should open Azure AI Studio to flow page
    - Verify that the visual DAG is for contoso-chat

* []  **03** | Setup Automated Runtime in Azure
    - Click **Select runtime** dropdown 
    - Select Automatic Runtime, click **Start**
    - Takes a few mins, watch progress indicator.chat

---

🥳 **Congratulations!** <br/> Your runtime is getting ready for the **Deployment** step later on.

===

[🏠 Table Of Contents](#table-of-contents) ⎯ [⚙️ Appendix](#appendix)

---

## 16. PromptFlow Deploy Flow

> [!hint]
> Till now, you've explored, built, tested, and evaluated, the prompt flow _from Visual Studio Code_, as a developer. Now it's time to _deploy the flow to production_ so applications can use the endpoint to make requests and receive responses in real time.

**Deployment Options**: We will be [using Azure AI Studio](https://learn.microsoft.com/azure/ai-studio/how-to/flow-deploy?tabs=azure-studio) to deploy our prompt flow from a UI. You can also deploy the flow programmatically [using the Azure AI Python SDK](https://learn.microsoft.com/azure/ai-studio/how-to/flow-deploy?tabs=python). 

**Deployment Process**: The deployment consists of these steps.
 - Upload the prompt flow to Azure AI Studio
 - Create a runtime and run the flow in Azure, to test it works
 - Deploy the prompt flow, to get a hosted endpoint
 - Use deployed endpoint (from built-in test in Azure AI Studio)
 - Optionally, use deployed endpoint (from a real app).

>[!note] **1: Upload Prompt Flow** to Azure AI Studio. 

We completed this in the previous step.

>[!note] **2: Create a runtime** and run the flow in Azure.

We started this process in the previous step, and were waiting on the automatic runtime creation to complete. Let's continue from there.

* []  **01** | Run Prompt Flow in Azure
    - On runtime setup being complete, you should see a ✅
    - Now click the blue **Run** or **Chat** button (visible at the end of that row)
    - Run should complete in a few minutes.
    - Verify that all graph nodes are green (success)

>[!note] **3: Deploy the prompt flow** to get a hosted endpoint

* []  **01** | Click the **Deploy** option in flow page
    - Opens a Deploy wizard flow
    - Keep defaults, click **Review+Create**.
    - Review configuration, click **Create**.

* []  **02-A** | Check **Deployment status** (option A)
    - Navigate to +++https://ai.azure.com+++
    - Click Build > Your AI Project (_contoso-chat-aiproj_)
    - Click **Deployments** and hit Refresh
    - You should see "Endpoint" listing with _Updating_
    - Refresh periodically till it shows _Succeeded_

* []  **02-B** | Check **Deployment status** (option B)
    - Navigate to +++https://ml.azure.com+++
    - Click the notifications icon (bell) in navbar
    - This should slide out a list of status items
    - Watch for all pending tasks to go green.

> [!alert]
> The deployment process **can take 10 minutes or more**. Use the time to explore other things. Note that the deployment **may** fail with an _image_ related error. This is due to ongoing updates to the platform that cannot be anticipated in advance. If that happens, you will **not be able to complete the next steps today** but we encourage you to revisit the lab on your own later, when the update issue may be resolved.

* []  **03** | Deployment succeeded
    - Go back to the Deployments list in step **02-A**
    - Click your deployment to view details page.
    - **Wait** till page loads and menu items update
    - You should see a menu with these items
        - **Details** - status & endpoint info
        - **Consume** - code samples, URL & keys
        - **Test** - interactive testing UI
        - **Monitoring** and **Logs** - for LLMOps

* []  **04** | Consume Deployment
    - Click the **Consume** tab
    - You should see 
        - the REST URL for endpoint
        - the authentication keys for endpoint
        - code snippets for key languages
    - Use this if testing from an app. In the next step, we'll explore using a built-in test instead.

>[!note] **4: Use Deployed Endpoint** with a built-in test. 

* []  **05** | Click the **Test** option in deployment page
     - Enter +++What can you tell me about your jackets?+++ for **question**
     - Click **Test** and watch _Test result_ pane
     - Test result output should show LLM app response

Explore this with other questions or by using different customer Id or chat_history values if time permits.

---

🥳 **Congratulations!** <br/> You made it!! You just _setup, built, ran, evaluated, and deployed_ a RAG-based LLM application using Azure AI Studio and Prompt Flow.

===

[🏠 Table Of Contents](#table-of-contents) ⎯ [⚙️ Appendix](#appendix)

---

## Lab Recap


> [!warning] **DON'T FORGET TO DELETE YOUR GITHUB CODESPACES TO SAVE QUOTA!**. 
> - Visit https://github.com/codespaces
> - Find the codespace you created in the "Owned by..." panel
> - Click the "..." menu at the end of codespace listing
> - Select "Delete Codespace"


> [!hint] What We Learned Today

**We started with a simple goal:** Build an LLM-based chat app that used Retrieval Augmented Generation (RAG) to answer questions relevant to a product catalog.

**We learned about LLM Ops:** Specifically, we identified a number of steps that need to be chained together in a workflow, to build, deploy & use **performant LLM Apps**.

**We learned about Azure AI Studio:** Specifically, we learned how to provision an Azure AI project using an Azure AI resource with selected Model deployments. We learned to build a RAG solution with Azure AI Search and Azure Cosmos DB. And we learned to upload, deploy, run, and test, prompt flows in Azure.

**We learned about Prompt Flow:** Specifically, we learned how to create, evalute, test, and deploy, a prompt flow using a VS Code extension to streamline end-to-end development for an LLM-based app. And we learned how to upload the flow to Azure AI Studio, and replicate the steps completely in the cloud.

Along the way, we learned what LLM Ops is and why having these tools to simplify and orchestrate end-to-end development workflows is critical for building the next generation of Generative AI applications at cloud scale.

> [!hint] What We Can Try Next

- **Explore Next Steps for LLMOpss**. 
    - Add GitHub Actions, Explore Intents 
    - See README: +++https://github.com/Azure-Samples/contoso-chat+++ README 
- **Explore Usage in Real Application.** 
    - Integrate & use deployed endpoint in web app
    - See README: +++https://github.com/Azure-Samples/contoso-web+++

> [!hint] Where Can You Learn More?

- **View Learning Resources**: [Azure AI Developer Hub](https://learn.microsoft.com/ai)
- **Join The Community**: [Azure AI Discord](https://aka.ms/aitour/contoso-chat/discord) (and grab a copy of slides)

---

⭐️ | **GIVE THE REPO A STAR ON GITHUB!** 

If you found this workshop useful, please give us a star on GitHub and help us make it better! 
 - **Repo**: +++https://github.com/Azure-Samples/contoso-chat+++ 

===

[🏠 Table Of Contents](#table-of-contents) ⎯ [⚙️ Appendix](#appendix)

---

## Appendix


> [!tip]
> This is a blank space for capturing any troubleshooting instructions or guidance for proctors.


* **01** | Users are on a device with smaller display or resolution
    - The screenshots and walkthrough will show the sidebar in the same screen since they used a large display.
    - Users with smaller displays will find these are hidden behind the **hamburger menu** option at top-left. 
    - They will need to click that to see the slide-out menu.

===


@lab.Activity(Provision)

```
$resourceGroupName = "contchat-rg"
$region = "swedencentral"
$localPath = "C:\Windows\System32\Scripts\contoso-chat\infra\main.bicep"

# Create Dir
if (Test-Path "C:\Windows\System32\Scripts") {
    Remove-Item -Recurse -Force "C:\Windows\System32\Scripts"
}
New-Item -ItemType Directory -Path "C:\Windows\System32\Scripts"

cd "C:\Windows\System32\Scripts"

# Clone the GitHub repository

$retryCount = 0
$maxRetries = 3

while ($retryCount -lt $maxRetries) {
    try {
        git clone https://github.com/pamelafox/contoso-chat.git -b pamelas-infra -q
        break
    }
    catch {
        Start-Sleep -Seconds 5
        $retryCount++
    }
}

if ($retryCount -eq $maxRetries) {
    Write-Host "Failed to clone the repository after $maxRetries attempts."
}

# Login
$username = "@lab.CloudPortalCredential(User1).Username"
$password = '@lab.CloudPortalCredential(User1).Password'
$AzCredential = New-Object -TypeName System.Management.Automation.PSCredential -ArgumentList ($username, (ConvertTo-SecureString -AsPlainText -Force -String $password))
Connect-AzAccount -Credential $AzCredential

# Force Subscription Context
Set-AzContext -Subscription '@lab.CloudSubscription.Id' -Tenant '@lab.CloudSubscription.TenantId'

# Create a new resource group
New-AzResourceGroup -Name $resourceGroupName -Location $region -Force

# Deploy the Bicep template
New-AzResourceGroupDeployment -ResourceGroupName $resourceGroupName -TemplateFile $localPath
```
===
