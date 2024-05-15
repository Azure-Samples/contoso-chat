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

## 3. Setup Browser Tabs

> [!tip] 
> **Check off Tasks As You Go:** This will let you track your progress through the lab.


* []  **01** | Launch the Edge Browser. **Open it in full-screen mode.**

* []  **02** | _Tab 1_: Open a new tab for **GitHub interactions**.
    - Navigate to  +++**https://aka.ms/contoso-chat/msbuild2024-lab**+++
    - Log into GitHub - user your GitHub profile credentials.
    - Leave this tab open (Tab 1)

* []  **03** | _Tab 2_: Open a new tab for the **Azure Portal**.
    - Navigate to  +++**https://portal.azure.com**+++ in a new tab.
    - You should see - _A Microsoft Azure login dialog_.
    - Enter Username: +++**@lab.CloudPortalCredential(User1).Username**+++
    - Enter Password: +++**@lab.CloudPortalCredential(User1).Password**+++ and click.
    - You should see - _Your Azure Subscription home page._
    - Leave this tab open (Tab 2)
    
* []  **04** | _Tab 3_: Open a new tab for **Azure AI Studio.**
    - Navigate to +++**https://ai.azure.com**+++ in a new tab.
    - Click _Sign in_ - no need to re-enter Username/Password.
    - You should see: _You are logged in with your Azure profile._
    - Leave this tab open. (Tab 3)

---

🚀 | **Next** -  Let's get GitHub Codespaces setup for development in the browser!

===

[🏠 Home](#pre-requisites) ⎯ [🧭 Table Of Contents](#table-of-contents)

---

## 4. Launch GitHub Codespaces 

> [!Important] **Note:** You need a GitHub account to use with GitHub Codespaces. **We recommend using a personal account (or a secondary account not linked to your corporate profile) for this purpose**. You can [create a free GitHub account](https://github.com/signup) if needed. The free tier of GitHub Codespaces is sufficient for this lab.

* []  **01** | Switch to Tab 1 (GitHub)
    - Navigate to +++**https://aka.ms/msbuild2024-lab**+++ 
    - Verify you are logged into GitHub

> [!Important] **Note:** You must uncheck the "Copy the main branch only" when forking the repo.

* []  **02** | Fork repo into your profile
    - Click the fork button on the repo.
    - Uncheck the _"Copy the 'main' branch" only_ (forks all branches)
    - Click "Create fork" and wait for process to complete.
    - **You should see** - a fork of the repo in your personal profile.

* []  **03** | Launch GitHub Codespaces on `msbuild2024-lab` branch
    - Click branches dropdown - select _msbuild-lab322_ branch.
    - Click _Code_ dropdown - select the _Codespaces_ tab
    - Click "Create codespace on msbuild2024-lab"
    - **You should see** - a new browser tab witg _'Setting up your codespace'_

This process takes a few minutes to complete. Let's keep going on the next task, and we'll check back on status later.

---

🚀 | **Next** - Let's verify Azure resources are provisioned while we wait ..


===

[🏠 Home](#pre-requisites) ⎯ [🧭 Table Of Contents](#table-of-contents)

---

## 5. Verify Azure Provisioning

> [!tip] 
> **Verify Azure Resources Were Provisioned**

* []  **01** | Switch to Tab 2 (Azure Portal) 
    - Navigate to +++**https://portal.azure.com**+++
    - Click _'Resource Groups'_ (bottom of page)
    - You should see - a resource group: **contoso-chat-rg**

* []  **02** | Click resource group - view details (by Type):
    - You should see 10 resources. These include
        - "Azure AI hub" 
        - "Azure AI services"
        - "Azure AI project"
        - "Search service" (Azure AI Search)
        - "Azure Cosmos DB account" 

> [!tip] 
> **Verify required OpenAI Models were deployed**. 

* []  **03** | Switch to Tab 3 (Azure AI Studio) 
    - Navigate to +++**https://ai.azure.com/build**+++
    - Click listed AI project for details. 
    - Click **Deployments** in sidebar (_Refresh_ if needed)
    - Verify that the following models are listed
        - gpt-35-turbo (for chat completion)
        - gpt-4 (for chat evaluation)
        - text-embedding-ada-002 (for text embedding)

* []  **04** | Check that Promptflow connections exist
    - Click **Settings** in the AI projects page sidebar
    - Look for **Connected Resources** - click _View All_.
    - Verify these connections exist (by name):
        - contoso-search
        - aoai-connection
    - We will create a third one (contoso-cosmos) manually later.

---

🚀 | **Next** - Let's see if our GitHub Codespaces enviornment is ready for development...

===

[🏠 Home](#pre-requisites) ⎯ [🧭 Table Of Contents](#table-of-contents)

---

## 6. Connect VSCode To Azure

> [!tip] 
> **Connect VSCode To Azure:** Let's configure IDE to talk to Azure.

* []  **01** |  Switch to Tab 1 (GitHub Codespaces launched earlier) 
    - ⏳ | You may need to wait a few minutes if setup is still ongoing ...
    - On completion, tab will refresh automatically
        - You should see - a Visual Studio Code editor 
        - You should see - a terminal open in editor (wait till prompt is active)

* []  **02** | Click in the VS Code terminal to use commandline
    - Enter command: +++az login --use-device-code+++ 
    - Open +++https://microsoft.com/devicelogin+++ in new tab
    - Copy-paste code from Azure CLI into the dialog you see here
    - On success, close this tab and return to VS Code tab

> [!Important] **Note:** Before you do this step, open the Azure Portal tab. Click the resource group details page. Click the **Deployments** tab to get the details page. Copy the name of the Deployments record (will be in the form _ContosoChatXXXX_) to use in the step below.

* []  **03** | Run the `setup-env.sh` to pre-populate config
    - Open the `provision-v1/setup-env.sh` file in VS Code
    - Update `name` (line 3) to Deployments name you copied above.
    - Switch to VS Code Terminal
    - Change directories: +++cd provision-v1/+++
    - Run the setup script using: +++sh setup-env.sh+++
    - Wait till script execution completes.

* []  **04** | Verify the following files were created
    - Open the file explorer panel in Visual Studio Code
    - You should see - `config.json` in root folder
    - You should see - `.env` in root folder
    - Open each file and make sure it is not empty

🥳 **Congratulations!** You've configured your VS Code environment for Azure use!

---

🚀 | **Next** - Run post-provision script (auto-populates data, pushes flows to Azure)

===

[🏠 Home](#pre-requisites) ⎯ [🧭 Table Of Contents](#table-of-contents)

---

## 7. Automate Azure Upload Tasks

> [!tip] 
> **Populate Data, Flows:** Run scripts that automatically pushes customer data, product indexes and a copy of application flows, to Azure for use in next steps.

* []  **01** | Run the postprovision script
    - Change directory to: +++cd provision-v1/+++
    - Run the setup script using: +++sh postprovision.sh+++
    - Wait till script execution completes.

* []  **02** | Verify Azure CosmosDB data was populated
    - Switch to Tab 2 (Azure Portal)
    - Click on your created resource group (_contoso-chat-rg_)
    - Click on your Azure Cosmos DB resource
    - Click the **Data Explorer** option in sidebar to view data
    - Verify that the **contoso-outdoor** container was created
    - Verify that it contains a **customers** database

* []  **03** | Verify Azure AI Search indexes was populated
    - Return to the resource group (_contoso-chat-rg_) page
    - Click on the Azure AI Search resource
    - Click the **Indexes** option in sidebar to view indexes
    - Verify that the **contoso-products** search index was created.

* []  **04** | Verify local promptflow connections were created
    - Return to Visual Studio Code terminal
    - Type +++pf connection list+++ and hit Enter
    - Verify 3 connections created: 
        - "contoso-search"'
        - "contoso-cosmos"
        - "aoai-connection"

* []  **05** | Verify promptflow app was uploaded to Azure
    - Navigate to +++**https://ai.azure.com/build**+++
    - Select the AI Project - click _Prompt Flow_ in sidebar
    - Look under the Flows tab - you may need to _Refresh_ for updates
    - Verify you see a flow listed - name may be in form `contoso-chat-xxxx`

---

🥳 **Congratulations!** Your application is ready to run locally, and on Azure

===

[🏠 Home](#pre-requisites) ⎯ [🧭 Table Of Contents](#table-of-contents)

---

## 8. Add Custom Connection 

> [!tip] 
> **Temporary Fix:** This step fixes a missing connection by having you add that in manually. Newer versions of the lab automate the process completely.

* []  **01** | Create the **Custom Connection** (+++contoso-cosmos+++) 
    - Navigate to Azure AI Studio tab - +++**https://ai.azure.com/build**+++
    - Select the AI Project and click _Settings_ in sidebar
    - Select the _New Connection_ option and click _Custom keys_ in available options
    - Under **Custom Keys** - Add 4 entries as shown below
        - key: +++key+++, value: use "COSMOS_KEY" value from .env 
        - key: +++_endpoint_+++, value: use "COSMOS_ENDPOINT" value from .env 
        - key: +++_containerId_+++, value: +++customers+++
        - key: +++_databaseId_+++, value: +++contoso-outdoor+++
        - **check "is secret" on the first key-value pair**
    - Set connection name: (+++contoso-cosmos+++) 
    - Click **Save** to complete step. 

* []  **02** | Verify all three connections now exist in Azure AI Studio
    - Navigate back to +++**https://ai.azure.com/build**+++
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

## 9. Understand Promptflow Application

> [!NOTE]
> So far, we've setup Azure resources, connected our VS Code development environment to Azure, and populated data required to build our retail copilot application. Now it's time to build and run that application **using Promptflow**. In this section, we'll quickly explore the application codebase.

* []  **01** | Explore the `contoso-chat` application source
    - Open the "Explorer" panel in VS Code
    - Click on the `contoso-chat` folder. You will see:
        - `flow.dag.yaml` - defining promptflow app (graph)
        - `customer_lookup.py` - code to look up customer data
        - `retrieve_documentation.py` - code to get search results
        - `customer_prompt.jnja2` - template for final prompt to LLM
        - `llm_response.jnja2` - template for llm response to user
    - See how this maps to RAG (retrieval augmented generation) pattern

* []  **02** | Explore the `flow.dag.yaml` application graph
    - Click the file to open it in the Visual Studio Code Editor
    - Study the default text file - you will see these sections:
        - **environment** - requirements.txt to install dependencies
        - **inputs** - named inputs & properties for flow 
        - **outputs** - named outputs & properties for flow 
        - **nodes** - processing functions (tools) for workflow

* []  **03** | Open `flow.dag.yaml` in the Visual Editor
    - Click on the `Visual editor` line (above **environment**)
    - You should see - a split screen with a graph to the right
    - You should see - a series of corresponding widgets to left

* []  **04** | Click any node in the graph (to right)
    - You wiill see the corresponding widget highlighted on left
    - Explore widget, see how properties map to node (input, output, function)
    - Explore `llm_response` for example of LLM processing node
    - Explore `customer_lookup` for example of Python function node
    - Explore `input` and `output` nodes to start and end flows

This defines the _processing pipeline_ for your LLM application from user input to returned response. To execute the flow, we need a Python runtime with the specified environment. Let's explore that next!

---

🥳 **Congratulations!** - You're ready to run your Prompt flow.

===

[🏠 Home](#pre-requisites) ⎯ [🧭 Table Of Contents](#table-of-contents)

---

## 10. Run Promptflow In VS Code

> [!hint]
> You should still be in the **Visual Editor** for the `flow.dag.yaml`. In this step, we'll _run_ the flow to see the application execute the user request (input).

* []  **01** | Let's revisit the Visual Editor pane for the promptflow.
    - You should see something like this (this is a sample image - your details may differ)
        ![](https://github.com/Azure-Samples/contoso-chat/raw/main/images/promptflow.png)
    - Look at the left pane in this split screen - and browse the top line of icons.
    
* []  **02** | Run the prompt flow locally
    - Look for an arrow icon with tooltip "Run all" next to the `Python env` string
    - Click the icon - you will see a drop-down menu with options
    - Select "Run it with standard mode" from dropdown
    - Wait till run completes
    
* []  **03** | Explore inputs and outputs of flow
    - On success, all nodes on right will show a green highlight.
    - If failures occur, specific nodes will show a red highlight
        - Click a failed node to get more insights, if this happens
    - Click the output node to see final outcome

* []  **04** | Explore Run Stats & Traces
    - Click the "Terminal" tab. It should show final response returned. 
    - Click the "Prompt Flow" tab. Select a node in visual editor.
        - Tab shows "node name, Tokens, duration" stats for node.
        - Click the line in table. You should see more details in pane.

* []  **05** | Try changing the input, re-run flow
    - In Inputs, **change question** to +++What else did I purchase?+++
    - Click **Run All** - how did the output change?
    - In Inputs, **change customerId** to +++12+++
    - Click **Run All** - how did the output change?
    - Experiment with other input values and analyze outputs.

---

🥳 **Congratulations!** You just built and ran the retail copilot in your local environment!

===

[🏠 Home](#pre-requisites) ⎯ [🧭 Table Of Contents](#table-of-contents)

---

## 11. Run Promptflow In Azure

> [!warning]
> 🚨 Work in Progress - FIX THESE INSTRUCTIONS

Needs Some Content


===

[🏠 Home](#pre-requisites) ⎯ [🧭 Table Of Contents](#table-of-contents)

---

## 12. Evaluate Promptflow in VS Code

> [!NOTE]
> You built and ran the retail copilot locally. Now it's time to **evaluate** the quality of the response, and see if you need to iterate on the prompt to improve it.

* []  **01** | Let's run the evaluation exercises
    - Open the Visual Studio Code "Explorer" panel
    - Click on the `exericses/` folder
    - Select the `5-evaluate-chat-prompt-flow.ipynb` notebook
    - In the opened editor pane, click **Select Kernel** (top right)
    - Select the default Python option (3.11.x)
    - Click **Clear All Outputs**. Then click **Run All** 

Wait till the notebook completes exeucting all cells. The notebook contains two main sections: **Local Evaluation - Groundedness** and **Local Evaluation - Multiple Metrics**. Let's understand what each one does.

* []  **02** | Local Evalution : Explore **Groundedness**
    - Evaluates our retail copilot for _groundedness_ 
    - This [**measures**](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in#ai-assisted-groundedness-1) how well the model's generated responses align with data you provided.
    - **Example**: We test if the answer to the question _"Can you tell me about your jackets"_ is grounded in the product data we indexed previously. 

* []  **03** | Local Evaluation : Explore **Multiple Metrics**
    - Evaluates our retail copilot using [4 key metrics](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in#metrics-for-multi-turn-or-single-turn-chat-with-retrieval-augmentation-rag):
    - **Groundedness** <br> How well does model's generated answers align with information from the source (product) data?
    - **Relevance** <br>  Extent to which the model's generated responses are pertinent and directly related to the given questions.
    - **Coherence**  <br>  Ability to generate text that reads naturally, flows smoothly, and resembles human-like language in responses.
    - **Fluency** <br>  Measures the grammatical proficiency of a generative AI's predicted answer.

* []  **04** | Review Evaluation Output
    - Check the Jupyter Notebook outputs
    - Verify execution run completed successfully
    - Review evaluation metrics to gain insights into response quality  

---

🥳 **Congratulations!** You evaluated your retail copilot for quality - and it passed! Now you can deploy it for real-world use!

===

[🏠 Home](#pre-requisites) ⎯ [🧭 Table Of Contents](#table-of-contents)

---

## 13. Deploy Promptflow in Azure

> [!warning]
> 🚨 Work in Progress - FIX THESE INSTRUCTIONS

>[!note] 
> We are automating push in previous step so add instructions to verify here

* []  **03** | Setup Automated Runtime in Azure
    - Click **Select runtime** dropdown 
    - Select Automatic Runtime, click **Start**
    - Takes a few mins, watch progress indicator.chat

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
    - [03. Setup Browser Tabs](#3-setup-browser-tabs)
    - [04. Launch GitHub Codespaces](#4-launch-github-codespaces)
    - [05. Verify Azure Provisioning](#5-verify-azure-provisioning)
    - [06. Connect VSCode To Azure](#6-connect-vscode-to-azure)
    - [07. Automate Azure Upload Tasks](#7-automate-azure-upload-tasks)
    - [08. Add Custom Connection](#8-add-custom-connection)
    - [09. Understand Promptflow Application](#9-understand-promptflow-application)
    - [10. Run Promptflow in VS Code](#10-run-promptflow-in-vs-code)
    - [11. Run Promptflow in Azure](#11-run-promptflow-in-azure)
    - [12. Evaluate Promptflow in VS Code](#12-evaluate-promptflow-in-vs-code)
    - [13. Deploy PromptFlow in Azure ](#13-deploy-promptflow-in-azure)
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
