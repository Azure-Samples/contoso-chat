[🏠 Home](#pre-requisites) ⎯ [🧭 Table Of Contents](#table-of-contents)

---

## Hello @lab.User.FirstName 👋🏽. 

This is a proctored 45-min lab on **Build, Evaluate & Deploy a RAG-based retail copilot with Azure AI** associated with the 1-hour instructor-led [Lab322 Session](https://build.microsoft.com/sessions/852fa54a-9756-4681-8cd5-ae9632b635ca) offered once daily at Microsoft Build 2024. 

> [+hint]
> Familiarize yourself with the instructor and proctors for this session. Lab instructions are organized in numbered sections and steps to make them easier to reference when asking questions.

## Pre-requisites

> [+alert]
> You must have the following to participate in this lab:

 * A **GitHub Account** for GitHub Codespaces usage. (mandatory) 
 * Familiarity with **Python and Jupyter Notebooks** is useful.
 * Familiarity with **Azure**, **Visual Studio Code** and **GitHub** is useful.

## 1. Get Started!

> [!hint] 
> **Skillable Pro-Tip:** Click on the green "T" (e.g., +++**@lab.VirtualMachine(BuildBaseVM).Username**+++) to have the associated value automatically entered into the VM at the current cursor location to minimize input errors.

-  [] **01** | Log into the Skillable VM with these credentials.
    - Username - Will already be set to **@lab.VirtualMachine(BuildBaseVM).Username**.
    - Password - Enter +++**@lab.VirtualMachine(BuildBaseVM).Password**+++ and click.
    - You should see - _A Windows 11 Desktop._

Let's get a quick overview of the lab in the next section.

===

[🏠 Home](#pre-requisites) ⎯ [🧭 Table Of Contents](#table-of-contents)

---

## 2. Lab Overview

> [!tip] 
> **Learning Objectives:** This lab teaches you how to build, evaluate, and deploy, a retail copilot application (_Contoso Chat_) using the Azure AI platform. By the end of this lab, you should be able to:

1. Describe the Contoso Chat retail copilot (Application)
1. Explain retrieval augmented generation (Architecture)
1. Describe the Azure AI Studio (Platform)
1. Describe the Promptflow tools & usage (Framework)
1. Build, evaluate, and deploy, a copilot app end-to-end (on Azure)

> [!tip] 
> **Pre-Provisioned Resources:** This lab comes with an _Azure Subscription_ that has been pre-provisioned with the necessary resources for developing this retail copilot solution. These include:

1. Azure AI Hub and Project - to manage your AI application
1. Azure AI Services - to manage your Open AI model deployments
1. Azure AI Search - to build and maintain the product index
1. Azure Cosmos DB - to build and maintain the customer history data

> [!tip] 
> **Browser as Default UI:** We will be using the Microsoft Edge browser in the VM as the default user interface throughout this lab. We recommend keeping three tabs open to these three resources:

1. **(Tab 1) GitHub Codespaces** - local dev environment in browser (dev container)
1. **(Tab 2) Azure Portal** - to view and manage all Azure resources
1. **(Tab 3) Azure AI Studio** - to view and manage Azure AI applications

> [!tip] 
> **Codespaces as Default Dev Env:** We will use the [#msbuild-lab322](https://aka.ms/contoso-chat/msbuild2024-lab) branch of the Contoso Chat repository. We will launch this in the browser with GitHub Codespaces, to get a ready-to-use dev environment for the lab.

---

🚀 | **Next** - Let's launch the browser and setup our dev environment!

===

[🏠 Home](#pre-requisites) ⎯ [🧭 Table Of Contents](#table-of-contents)

---

## 3. Browser Setup

> [!tip] 
> **Check off Tasks As You Go:** This will let you track your progress through the lab.


* []  **01** | Launch the Edge Browser. **Open it in full-screen mode.**

* []  **02** | _Tab 1_: Open a new tab for **GitHub interactions**.
    - Navigate to  +++**https://aka.ms/contoso-chat/msbuild2024-lab**+++
    - Log into GitHub - user your GitHub profile credentials.
    - Leave this tab open | Tab 1 = Development Tab

* []  **03** | _Tab 2_: Open a new tab for the **Azure Portal**.
    - Navigate to  +++**https://portal.azure.com**+++ in a new tab.
    - You should see - _A Microsoft Azure login dialog_.
    - Enter Username: +++**@lab.CloudPortalCredential(User1).Username**+++
    - Enter Password: +++**@lab.CloudPortalCredential(User1).Password**+++ and click.
    - You should see - _Your Azure Subscription home page._
    - Leave this tab open | Tab 2 = Azure Portal
    
* []  **04** | _Tab 3_: Open a new tab for **Azure AI Studio.**
    - Navigate to +++**https://ai.azure.com**+++ in a new tab.
    - Click _Sign in_ - no need to re-enter Username/Password.
    - You should see: _You are logged in with your Azure profile._
    - Leave this tab open | Tab 3 = Azure AI Studio

---

🚀 | **Next** -  Let's get GitHub Codespaces setup for development in the browser!

===

[🏠 Home](#pre-requisites) ⎯ [🧭 Table Of Contents](#table-of-contents)

---

## 4. Launch GitHub Codespaces 

> [!Important] **Note:** You need a GitHub account to use with GitHub Codespaces. **We recommend using a personal account (or a secondary account not linked to your corporate profile) for this purpose**. You can [create a free GitHub account](https://github.com/signup) if needed. The free tier of GitHub Codespaces is sufficient for this lab.

* []  **01** | Switch to the GitHub tab (Tab 1) in the browser
    - Navigate to the  +++**https://aka.ms/msbuild2024-lab**+++ link
    - Verify you are logged into GitHub (from prior step)

* []  **02** | Fork the repo into your profile
    - Click the fork button on the repo.
    - Uncheck the _"Copy the 'main' branch" only_ to fork with all branches.
    - Click "Create fork" and wait for process to complete.
    - **You should see** - a fork of the repo in your personal profile.

* []  **03** | Launch GitHub Codespaces on `msbuild2024-lab` branch
    - Click branches dropdown - select _msbuild-lab322_ branch.
    - Click _Code_ dropdown - select the _Codespaces_ tab
    - Click "Create codespace on main"
    - **You should see** - a new browser tab witg _'Setting up your codespace'_

This process takes a few minutes to complete. Let's keep going on the next task, and we'll check back on status later.

---

🚀 | **Next** - Let's verify Azure resources are provisioned while we wait ..


===

[🏠 Home](#pre-requisites) ⎯ [🧭 Table Of Contents](#table-of-contents)

---

## 5. Verify Azure Is Provisioned

> [!tip] 
> **Look for Resource Group "contoso-chat-rg"**. And verify the right resources were created.

* []  **01** | Switch to Tab 2 (Azure Portal) in the browser
    - Navigate to the Azure Portal home page +++**https://portal.azure.com**+++
    - Click the _'Resource Groups'_ option
    - Verify that a Resource Group called **contoso-chat-rg** is listed.
* []  **02** | Click it to view details. Verify these resources exist (by Type):
    - "Azure AI hub" resource
    - "Azure AI services" resource
    - "Azure AI project" resource
    - "Search service" resource (Azure AI Search)
    - "Azure Cosmos DB account" resource

> [!tip] 
> **Verify required OpenAI Models were deployed**. And validate that related connections were created.

* []  **03** | Switch to Tab 3 (Azure AI Studio) in the browser
    - Navigate to Azure AI Studio "Build" section - +++**https://ai.azure.com/build**+++
    - Click the listed AI project for details. 
    - Click **Deployments** in sidebar, click _Refresh_ in details page.
    - Verify that the following models are listed
        - gpt-35-turbo
        - gpt-4
        - text-embedding-ada-002

* []  **04** | Check that relevant "connections" were created in AI project.
    - Click **Settings** in the AI projects page sidebar
    - Look for a **Connected Resources** or **Connections** panel - click _View All_.
    - Verify these connections exist (by name):
        - contoso-search
        - aoai-connection
    - We will be creating a third one (contoso-cosmos) manually later.

---

🚀 | **Next** - Let's see if our GitHub Codespaces enviornment is ready for development...

===

[🏠 Home](#pre-requisites) ⎯ [🧭 Table Of Contents](#table-of-contents)

---

## 6. VSCode Azure Login

> [!tip] 
> **Connect VSCode To Azure:** Once ready, the GitHub Codespaces environment will launch with a Visual Studio Code session (IDE) by default. In this step, we'll connect it to our Azure environment to access pre-provisioned resources.

* []  **01** |  Switch to Tab 1 (GitHub Codespaces launched earlier) 
    - Wait for setup to complete if still ongoing
    - On completion, tab will refresh automatically
    - You should see - a Visual Studio Code editor 
    - You should see - a terminal open in editor (wait till prompt is active)

* []  **02** | Click in the terminal to use the Azure CLI (`az`) tool:
    - Enter command: +++az login --use-device-code+++ 
    - Open +++https://microsoft.com/devicelogin+++ in new tab
    - Copy-paste code from Azure CLI into the dialog you see here
    - On success, close this tab and return to VS Code tab

🥳 **Congratulations!** You've connected your VS Code development environment to Azure!

---

🚀 | **Next** - Run post-provision script (auto-populates data, pushes flows to Azure)

===

[🏠 Home](#pre-requisites) ⎯ [🧭 Table Of Contents](#table-of-contents)

---

## 7. VSCode Config Env

> [!warning]
> 🚨 Work in Progress - TEST THESE UPDATED INSTRUCTIONS ARE CORRECT

> [!tip] 
> **Connect VSCode To Azure:** Run scripts that automate steps to populate data for key resources, and push the promptflow to Azure for use in a later deployment step.

* []  **01** | Run the postprovision script
    - Click in the terminal and change working directory: +++cd 1-provision/+++
    - Run the setup script using: +++sh postprovision.sh+++
    - Wait till script execution completes.

* []  **02** | Verify the following files were created
    - Open the file explorer panel in Visual Studio Code
    - Verify that `config.json` was created in the root folder
    - Click file to open in editor and verify it is not empty
    - Verify that `.env` was created in the root folder
    - Click file to open in editor and verify it is not empty

* []  **03** | Verify Azure CosmosDB data was populated
    - Switch to Tab 2 (Azure Portal)
    - Click on your created resource group (_contoso-chat-rg_)
    - Click on your Azure Cosmos DB resource
    - Click the **Data Explorer** option in sidebar to view data
    - Verify that the **contoso-outdoor** container was created
    - Verify that it contains a **customers** database

* []  **04** | Verify Azure AI Search indexes was populated
    - Return to the resource group (_contoso-chat-rg_) page
    - Click on the Azure AI Search resource
    - Click the **Indexes** option in sidebar to view indexes
    - Verify that the **contoso-products** search index was created.

* []  **05** | Verify local promptflow connections were created
    - Return to Visual Studio Code terminal
    - Type +++pf connection list+++ and hit Enter
    - Verify 3 connections were created *with these names* <br/> **"contoso-search", "contoso-cosmos", "aoai-connection"**

* []  **06** | Verify the local promptflow was uploaded to Azure
    - This allows us to run & test the same application in Azure AI Studio (pre-deploy)
    - Navigate to Azure AI Studio "Build" section - +++**https://ai.azure.com/build**+++
    - Select the AI Project - then click the _Prompt Flow_ tab in sidebar
    - Verify you are in the Flows tab - you may need to click _Refresh_ for updates
    - Verify that you can see a Flow listed - the name will be of the form `chat-flow-xxxx`

---

🥳 **Congratulations!** Your application is configured and ready to run (locally, and on Azure)

===

[🏠 Home](#pre-requisites) ⎯ [🧭 Table Of Contents](#table-of-contents)

---

## 8. Add Custom Cosmos Connection 

> [!tip] 
> **Temporary Fix:** The postprovision script sets up all promptflow connections by default. For now, we have to manually configure the one _custom connection_ required for Azure Cosmos DB. This is a temporary measure that is being automated in upcoming versions of the sample.

> [!warning]
> 🚨 Work in Progress - TEST THESE UPDATED INSTRUCTIONS ARE CORRECT

* []  **01** | Create the **Custom Connection** (+++contoso-cosmos+++) 
    - Navigate to Azure AI Studio "Build" section - +++**https://ai.azure.com/build**+++
    - Select the AI Project and click _Settings_ in sidebar
    - Select the _New Connection_ option and click _Custom keys_ in available options
    - Under **Custom Keys** - Add 4 entries as shown below
        - key: +++key+++, value: use "COSMOS_KEY" value from .env 
        - key: +++_endpoint_+++, value: use "COSMOS_ENDPOINT" value from .env 
        - key: +++_containerId_+++, value: +++customers+++
        - key: +++_databaseId_+++, value: +++contoso-outdoor+++
        - **check "is secret" on the first key-value pair**
    - Click **Save** to complete step. 

* []  **02** | Verify all three connections now exist in Azure AI Studio
    - Navigate to Azure AI Studio "Build" section - +++**https://ai.azure.com/build**+++
    - Select the AI Project and click _Settings_ in sidebar
    - Click **Connected Resources** - and select _View all_
    - Verify you see the following in the listed connections:
        - contoso-search
        - aoai-connection
        - contoso-cosmos

---

🚀 | **Next** - Let's run the promptflow on VS Code, and explore the code

===

[🏠 Home](#pre-requisites) ⎯ [🧭 Table Of Contents](#table-of-contents)

---

## 9. Understand Promptflow Codebase

> [!warning]
> 🚨 Work in Progress - FIX THESE INSTRUCTIONS

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

[🏠 Home](#pre-requisites) ⎯ [🧭 Table Of Contents](#table-of-contents)

---

## 10. Run Promptflow In VS Code

> [!warning]
> 🚨 Work in Progress - FIX THESE INSTRUCTIONS

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

[🏠 Home](#pre-requisites) ⎯ [🧭 Table Of Contents](#table-of-contents)

---

## 11. Run Promptflow in Azure

> [!warning]
> 🚨 Work in Progress - FIX THESE INSTRUCTIONS


===

[🏠 Home](#pre-requisites) ⎯ [🧭 Table Of Contents](#table-of-contents)

---

## 12. Evaluate Promptflow in VS Code

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

[🏠 Home](#pre-requisites) ⎯ [🧭 Table Of Contents](#table-of-contents)

---

## 13. Push PromptFlow To Azure

> [!warning]
> 🚨 Work in Progress - Remove this, should be done in Step 8 automatically

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

[🏠 Home](#pre-requisites) ⎯ [🧭 Table Of Contents](#table-of-contents)

---

## 14. PromptFlow Deploy Flow

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

[🏠 Home](#pre-requisites) ⎯ [🧭 Table Of Contents](#table-of-contents)

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

[🏠 Home](#pre-requisites) ⎯ [🧭 Table Of Contents](#table-of-contents)

---

## Table Of Contents

- [**Lab Overview**](#lab-overview)
    - [01. Get Started](#1-get-started)
    - [02. Lab Overview](#2-lab-overview)
    - [03. Browser Setup](#3-browser-setup)
    - [04. Launch GitHub Codespaces](#4-launch-github-codespaces)
    - [05. Verify Azure Is Provisioned](#5-verify-azure-is-provisioned)
    - [06. VSCode Azure Login](#6-vscode-azure-login)
    - [07. VSCode Config Env](#7-vscode-config-env)
    - [08. Azure Config Connections](#8-azure-config-connections)
    - [09. PromptFlow Explore Codebase](#9-promptflow-explore-codebase)
    - [10. PromptFlow Open Visual Editor](#10-promptflow-open-visual-editor)
    - [11. PromptFlow Run Flow ](#11-promptflow-run-flow)
    - [12. PromptFlow Evaluate Flow](#12-promptflow-evaluate-flow)
    - [13. Push PromptFlow To Azure ](#13-push-promptflow-to-azure)
    - [14. PromptFlow Deploy Flow](#14-promptflow-deploy-flow)
- [**Lab Recap**](#lab-recap)



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
