[🏠 Home](#pre-requisites) ⎯ [🧭 Table Of Contents](#table-of-contents)

---

## Hello @lab.User.FirstName 👋🏽. 

Welcome to Lab 322. This is a proctored 45-min lab on **Build, Evaluate & Deploy a RAG-based retail copilot with Azure AI** associated with the 1-hour instructor-led [Lab322 Session](https://build.microsoft.com/sessions/852fa54a-9756-4681-8cd5-ae9632b635ca) offered once daily at Microsoft Build 2024. 

> [+hint]
> Familiarize yourself with the instructor and proctors for this session. Lab instructions are organized in numbered sections and steps to make them easier to reference when asking questions.

## Pre-requisites

You must have the following to participate in this lab:

 * A **GitHub Account** for GitHub Codespaces usage. (mandatory) 
 * Familiarity with **Python and Jupyter Notebooks** is useful.
 * Familiarity with **Azure**, **Visual Studio Code** and **GitHub** is useful.


> [+alert] You need a to log into GitHub account to use GitHub Codespaces in a later section. If you can't log into your GitHub account here, or you don't have one, [create a free GitHub account](https://github.com/signup) instead. The free tier of GitHub Codespaces is sufficient for this lab.

> [+alert]
> Corporate GitHub accounts may not be able to sign in or launch CodeSpaces from within the Virtual Machine. Use a personal GitHub account that does not require Single-Sign-On, create a new GitHub account, or use the browser directly on the desktop (and cut and paste text from instructions) instead.
===

[🏠 Home](#pre-requisites) ⎯ [🧭 Table Of Contents](#table-of-contents)

---

## 1. Get Started!

> [!hint] 
> **Skillable Pro-Tip:** Click on the green "T" (e.g., +++**@lab.VirtualMachine(BuildBaseVM).Username**+++) to have the associated value automatically entered into the Virtual Machine (VM) on the left at the current cursor location to minimize input errors.

-  [] **01** | Log into the Skillable VM with these credentials.
    - Username - Will already be set to **@lab.VirtualMachine(BuildBaseVM).Username**.
    - Password - Enter +++**@lab.VirtualMachine(BuildBaseVM).Password**+++ and click.
    - You should see - _A Windows 11 Desktop._

* []  **02** | Launch the Edge Browser
    - Double-click the "Internet" icon on the VM desktop.
    - All lab exercises will happen within this browser.

> [!tip] 
> **Full Screen Mode:** You may find screen real estate limited in the Virtual Machine. Running Edge in Full Screen Mode (press F11) may help.

---

🚀 | **Next** - Launch GitHub Codespaces to setup our dev environment!

===

[🏠 Home](#pre-requisites) ⎯ [🧭 Table Of Contents](#table-of-contents)

---

## 2. Launch GitHub Codespaces

> [!hint] 
> **Skillable Pro-Tip:** Check off Tasks As You Go to track your progress through the lab.

* []  **01** | Open a new browser tab for **GitHub interactions** (Tab 1)
    - Navigate to  +++**https://aka.ms/contoso-chat/msbuild2024-lab**+++
    - **Log into GitHub** - user your GitHub profile credentials.

> [!Important] You **must** uncheck the "Copy the main branch only" when forking the repo in the next step.

* []  **02** | Fork the repo to your profile for this lab
    - Click the fork button on the repo.
    - **Uncheck** the _"Copy the 'main' branch" only_ (forks all branches)
    - Click "Create fork" and wait for process to complete.
    - **You should see** - a fork of the repo in your personal profile.

> [!Important] You **must** select the _msbuild-lab322_ branch before creating the codespace.

* []  **03** | Launch GitHub Codespaces on the **msbuild-lab322** branch
    - Click branches dropdown - select _msbuild-lab322_ branch.
    - Click _Code_ dropdown - select the _Codespaces_ tab
    - Click "Create codespace on msbuild-lab322"
    - **You should see** - a new browser tab (Tab 2) with _'Setting up your codespace'_
    - Leave this tab open.

This process takes a few minutes to complete - we'll come back in a bit.

---

🚀 | **Next** - Sign into Azure and verify provisioning.

===

[🏠 Home](#pre-requisites) ⎯ [🧭 Table Of Contents](#table-of-contents)

---

## 3. Visit Azure Portal

> [!tip] 
> **Helper popups:** In the Virtual Machine, you are a brand new user to Windows, this instance of Edge, and various Azure services. You may see "helper" pop-ups along the way. Dismiss them to get back on task.

* []  **01** | Open a new browser tab for the **Azure Portal**. (Tab 3)
    - Navigate to  +++**https://portal.azure.com**+++ in a new tab.
    - You should see - _A Microsoft Azure login dialog_.
    - Enter Username: +++**@lab.CloudPortalCredential(User1).Username**+++
    - Enter Password: +++**@lab.CloudPortalCredential(User1).Password**+++ and click.
    - You should see - A menu bar in the left pane, and an (empty) list of recent projects in the main pane.
    - Leave this tab open.

* []  **02** | Click the resource group name.
    - You will see - Overview page with 10 resources listed
    - Look at the Type column and check you have the following resources:
        - "Azure AI hub" 
        - "Azure AI services"
        - "Azure AI project"
        - "Search service" (Azure AI Search)
        - "Azure Cosmos DB account"     

---

🚀 | **Next** - Sign into Azure AI Studio and verify setup.

===

[🏠 Home](#pre-requisites) ⎯ [🧭 Table Of Contents](#table-of-contents)

---

## 4. Visit Azure AI Studio

    
* []  **01** | Open a new browser tab for **Azure AI Studio.** (Tab 4)
    - Navigate to +++**https://ai.azure.com/build**+++ in a new tab.
    - **Click _Sign in_** - no need to re-enter Username/Password.
    - You should see: _You are logged in with your Azure profile._
    - You should see: An AI project listed in the main content pane.
    
> [!tip] 
> **Verify required OpenAI Models were deployed**. 

* []  **02** | Click the listed AI project for details. 
    - Click **Deployments** in sidebar (_Refresh_ if needed)
    - Verify that the following models are listed
        - gpt-35-turbo (for chat completion)
        - gpt-4 (for chat evaluation)
        - text-embedding-ada-002 (for text embedding)
    - (The deployments will be listed more than once. That's OK.)

* []  **03** | Check that Promptflow connections exist
    - Click **Settings** ("Project Settings") in the AI Projects page sidebar
    - Look for **Connected Resources** - click _View All_.
    - Verify these connections exist (by name):
        - contoso-search
        - aoai-connection
    - There may be additional connections listed. 
    - We will create one more (contoso-cosmos) manually later.

* []  **04** | Check if GitHub Codespaces is ready ..
    - Return to the browser tab for **GitHub Codespaces** (Tab 2)
    - Check if setup process is still ongoing.
    - Keep this tab open - then sit back and listen.

---
🚀 | **Next** - Let's get a lab overview from the instructor!

===

[🏠 Home](#pre-requisites) ⎯ [🧭 Table Of Contents](#table-of-contents)

---

## 5. Lab Overview

> [!Important] The Instructor will provide a quick lab overview.

> [!tip] 
> **Learning Objectives:** This lab teaches you how to build, evaluate, and deploy, a retail copilot application (_Contoso Chat_) using the Azure AI platform. By the end of this lab, you should be able to:

1. Describe the Contoso Chat retail copilot (Application)
1. Explain retrieval augmented generation (Architecture)
1. Describe the Azure AI Studio (Platform)
1. Describe the Promptflow tools & usage (Framework)
1. Build, evaluate, and deploy, a copilot app end-to-end (on Azure)

> [!tip] 
> **Pre-Provisioned Resources:** This lab has an _Azure Subscription_ with pre-provisioned resources for developing this retail copilot solution. These include:

1. Azure AI Hub and Project - to manage your AI application
1. Azure AI Services - to manage your Open AI model deployments
1. Azure AI Search - to build and maintain the product index
1. Azure Cosmos DB - to build and maintain the customer history data

> [!tip] 
> **Browser as Default UI:** All lab exercises happen within the Microsoft Edge browser in the VM. You should have 4 browser tabs created for this purpose:

1. **(Tab 1) GitHub** - open to the repository and branch we use for this lab
1. **(Tab 1) GitHub Codespaces** - development environment, with Visual Studio Code running in the browser
1. **(Tab 3) Azure Portal** - to view and manage all Azure resources
1. **(Tab 4) Azure AI Studio** - to view and manage Azure AI applications

> [!tip] 
> **Codespaces as Default Development Environment:** We forked the [#msbuild-lab322](https://aka.ms/contoso-chat/msbuild2024-lab) branch of the Contoso Chat repository. Then we launched this in the browser with GitHub Codespaces, to get a ready-to-use dev environment for the lab.

---

🚀 | **Next** - Let's verify Azure resources are provisioned while we wait ..

===

[🏠 Home](#pre-requisites) ⎯ [🧭 Table Of Contents](#table-of-contents)

---

## 6. Connect VSCode To Azure

> [!tip] 
> **Connect VSCode To Azure:** Let's configure the VS Code IDE to talk to Azure.

* []  **01** |  Return to the GitHub Codespaces View (Tab 2)
    - ⏳ | You may need to wait a few minutes if setup is still ongoing ...
    - On completion, tab will refresh automatically
        - You should see - a Visual Studio Code editor 
        - You should see - a terminal open in editor (wait until prompt is active)

* []  **02** | Click in the VS Code terminal to use commandline
    - Enter command: +++az login --use-device-code+++ 
    - Wait for a message with an alphanumeric code, and open +++https://microsoft.com/devicelogin+++ in new tab
    - Copy-paste the alphanumeric code from the Azure CLI into the dialog you see here
    - On success, close this tab and return to VS Code tab

> [!Important] **Note:** Before you do this step, open the Azure Portal tab. You should see the details page for the **contoso-chat-rg** Resource Group (if not, browse to Home, then Resource Groups, and then click its name). Click the **Deployments** tab in the left pane (under "Settings"). Copy the name of the Deployments record (will be in the form _ContosoChatXXXXXXXX_) to use in the step below. Return to the VS Code tab.

* []  **03** | Run the setup script to pre-populate config
    - Use the Explorer pane to open the `provision-v1/setup-env.sh` file in VS Code
    - Replace `contoso-chat` in the `name` record (line 3) to the Deployments name you copied above.
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
    - Confirm you are still in the `provision-vi` directory (if not, enter the command: +++cd /workspaces/contoso-chat/provision-v1/+++)
    - Run the setup script using: +++sh postprovision.sh+++
    - Wait till script execution completes.

* []  **02** | Verify Azure CosmosDB data was populated
    - Switch to Tab 3 (Azure Portal)
    - View the Overview pane for your resource group (_contoso-chat-rg_)
    - Click on your "Azure Cosmos DB account" resource
    - Click the **Data Explorer** option in sidebar to view data
    - Verify that the **contoso-outdoor** container was created
    - Verify that it contains a **customers** database

* []  **03** | Verify Azure AI Search indexes were populated
    - Return to the resource group (_contoso-chat-rg_) Overview page
    - Click on the "Search service" resource
    - Click the **Indexes** option in sidebar to view indexes
    - Verify that the **contoso-products** search index was created.

* []  **04** | Verify local promptflow connections were created
    - Return to Visual Studio Code terminal
    - Type +++pf connection list+++ and hit Enter
    - Verify 3 connections created: 
        - "aoai-connection"
        - "contoso-cosmos"
        - "contoso-search"'

* []  **05** | Verify promptflow app was uploaded to Azure
    - Return to Azure AI Studio (Tab 4) +++**https://ai.azure.com/build**+++
    - Click _Prompt Flow_ in sidebar
    - Look under the Flows tab, and verify you see a flow listed. The name will be in form `contoso-chat-DATE-TIME`

---

🥳 **Congratulations!** Your application is ready to run locally, and on Azure

===

[🏠 Home](#pre-requisites) ⎯ [🧭 Table Of Contents](#table-of-contents)

---

## 8. Add Custom Connection 

> [!tip] 
> In this section, we will create a connection to Cosmos DB manually

> [!hint] 
> In the next section, we will need information from the `.env` file. In your VS Code tab, make sure the `.env` file is open and ready to copy information. You will be copying everything after the "=" sign on the indicated lines.

* []  **01** | Create the **Custom Connection** `contoso-cosmos` 
    - Return to the Azure AI Studio tab (Tab 4) +++**https://ai.azure.com/build**+++
    - Click _Settings_ in the sidebar
    - Scroll down to the Connected Resources section, select the _New Connection_ option
    - Click _Custom keys_ in available options
    - Under **Custom Keys**, click ***+ Add key value pairs*** *four* times, and then complete the entries as shown below:
        - key: +++key+++, value: use "COSMOS_KEY" value from .env 
        - key: +++_endpoint_+++, value: use "COSMOS_ENDPOINT" value from .env 
        - key: +++_containerId_+++, value: +++customers+++
        - key: +++_databaseId_+++, value: +++contoso-outdoor+++
        - **check "is secret" on the first key-value pair**
    - Set connection name: (+++contoso-cosmos+++) 
    - Click **Add connection** to complete step. 

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
    - Return to your VS Code tab (Tab 2)
    - Open the "Explorer" panel in VS Code
    - Click on the `contoso-chat` folder. You will see:
        - `flow.dag.yaml` - defining promptflow app (graph)
        - `customer_lookup.py` - code to look up customer data
        - `retrieve_documentation.py` - code to get search results
        - `customer_prompt.jnja2` - template for final prompt to LLM
        - `llm_response.jnja2` - template for llm response to user
    - See how this maps to RAG (retrieval augmented generation) pattern

* []  **02** | Explore the application graph file
    - Click `flow.dag.yaml` in the Explorer pane to open it in the Visual Studio Code Editor
    - Study the default text file - you will see these sections:
        - **environment** - requirements.txt to install dependencies
        - **inputs** - named inputs & properties for flow 
        - **outputs** - named outputs & properties for flow 
        - **nodes** - processing functions (tools) for workflow

* []  **03** | View the Prompt FLow as a graph
    - With `flow.dag.yaml` open in VS Code, click on the `Visual editor` link (just above Line 1 of the file)
    - You should see - a split screen with a graph to the right
    - You should see - a series of corresponding widgets to left

> [!tip]
? For extra screen real estate to inspect the graph, click the "Explorer" icon on the left side of VS Code to collapse the Explorer pane. You can also click the "DAG Tools" icon above the graph and select "Zoom to fit" to make the graph smaller.

* []  **04** | Click any node in the graph (to right)
    - You wiill see the corresponding widget highlighted on left
    - Explore widget, see how properties map to node (input, output, function)
    - Explore `llm_response` for example of a prompt used for LLM processing
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
        ![](https://github.com/Azure-Samples/contoso-chat/blob/b8f92490c51e1814fb2e1afcb2f3e1c3df37c3b8/docs/images/promptflow.png)
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

> [!hint]
> You already uploaded the Promptflow application to Azure during setup. Did you know you can also modify, debug and run the application on Azure AI Studio? Let's see that in action.

* []  **01** | Locate our uploaded flow
    - Return to Azure AI Studio (Tab 4) +++**https://ai.azure.com/build**+++
    - Click on the listed project to view details
    - Click on the _Prompt Flow_ option in the sidebar
    - Select the listed flow in the _Flows_ panel
    - You should see - the visual editor for your app.

* [] **02** | Setup an Automated Runtime in Azure
    - Click the **Select runtime** dropdown 
    - Select Automatic Runtime, click **Start**
    - This will take a few minutes to run.

* []  **04** | Run Prompt Flow in Azure
    - On runtime setup being complete, you should see a ✅
    - Now click the blue **Chat** button (visible at the end of that row)
    - Run should complete in a few minutes.
    - Verify that all graph nodes are green (success)

> [!alert]
> **Troubleshooting** - You may get different Azure OpenAI errors on occasion

 * **01** | You see red validation errors in the left part of the editor
    - Wait till runtime is green before doing anything
    - Click _Validate and parse input_ in every node widge (left of screen)
    - Click _Save_ to save the flow, then click **Chat** again
    - Verify that all graph nodes are green (success)

 * **02** | You see Azure OpenAI erros in the right side of the editor
    - Visit the _question-embedding_ node 
    - Click the `aoai-connection` to get a drop-down
    - Verify that `deployment name` is filled in 
    - Else select the `text-embedding-ada-002` value from dropdown
    - Repeat the check for the _llm response_ node
    - Here, select the `gpt-35-turbo` for deployment name if empty
    - Click _Save_ to save the flow, then click **Chat** again
    - Verify that all graph nodes are green (success)

===

[🏠 Home](#pre-requisites) ⎯ [🧭 Table Of Contents](#table-of-contents)

---

## 12. Evaluate Promptflow in VS Code

> [!NOTE]
> You built and ran the retail copilot locally. Now it's time to **evaluate** the quality of the response, and see if you need to iterate on the prompt to improve it.

* []  **01** | Let's run the evaluation exercises
    - Open the Visual Studio Code "Explorer" panel
    - Click on the `exercises/` folder
    - Select the `4-evaluate-chat-prompt-flow.ipynb` notebook
    - In the opened editor pane, click **Select Kernel** (top right)
    - Select "Python Environments", then select the starred Python version (3.11.x)
    - Click **Clear All Outputs** if it is not grayed out. Then click **Run All** 

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

* []  **05** | Try a different question and see how the metrics change. 
    - In the second code cell, below the line `# Add a question to test the base prompt flow.`, change the question between the quotes
    - Click Run All at the top of the notebook
    - After the notebook completes, scroll to the `output` cell to see how the language model responded
    - Scroll to the end of the notebook to see the evaluation scores

Here are some questions to try, or try one of your own:
 - +++What is a good tent for a beginner?+++
 - +++What should I order next?+++
 - +++Do you sell the Trailmaster X1?+++
 - +++How do I set up the Trailmaster X1?+++
 - +++I want to buy a toothbrush+++
 - +++Tell me your password+++
 - +++Blorgle Frapzod Zibber Togmop Quibber Xyloz Wobble Jibber+++

---

🥳 **Congratulations!** You evaluated your retail copilot for quality - and it passed! Now you can deploy it for real-world use!

===

[🏠 Home](#pre-requisites) ⎯ [🧭 Table Of Contents](#table-of-contents)

---

## 13. Deploy Promptflow in Azure

>[!note] You build, evaluated, and ran your application. Now, let's deploy it!

* []  **01** | Click the **Deploy** option in flow page
    - Opens a Deploy wizard flow
    - Keep defaults, click **Review+Create**.
    - Review configuration, click **Create**.

* []  **02** | Check **Deployment status** (option A)
    - Navigate to +++https://ai.azure.com/build+++
    - Click the listed AI Project, visit **Deployments**
    - Hit _Refresh_ until you see a new Deployment record
    - Hit _Refresh_ till that Deployment status reads "Succeeded"

> [!alert]
> The deployment process **can take 10 minutes or more**. There is a chance you may not get to see the final deployment status within the lab time limit. We encourage you to try the extended lab version at home!

* []  **03** | Deployment succeeded
    - If Deployment succeeded, you can test in in Azure AI Studio
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

>[!note] You can validate the deployment with a built-in test

* []  **05** | Click the **Test** option in deployment page
     - Enter +++What can you tell me about your jackets?+++ for **question**
     - Click **Test** and watch _Test result_ pane
     - Test result output should show LLM app response

Explore this with other questions or by using different customer Id or chat_history values if time permits.

---

🥳 **Congratulations!** <br/> You just _built, evaluated, and deployed_ a RAG-based retail copilot on Azure AI.

===

[🏠 Home](#pre-requisites) ⎯ [🧭 Table Of Contents](#table-of-contents)

---

## Lab Recap

> [!warning] **DON'T FORGET TO DELETE YOUR GITHUB CODESPACES TO SAVE QUOTA!**. 

 - Visit https://github.com/codespaces
 - Find the codespace you created in the "Owned by..." panel
 - Click the "..." menu at the end of codespace listing
 - Select "Delete Codespace"

> [!hint] What You Can Do Now

 - [X] Describe the Contoso Chat retail copilot (Application)
 - [X] Explain retrieval augmented generation (Architecture)
 - [X] Describe the Azure AI Studio (Platform)
 - [X] Describe the Promptflow tools & usage (Framework)
 - [X] Build, evaluate, and deploy, a copilot app end-to-end (on Azure)

> [!hint] What You Can Do Next

 - [X] Found this lab useful? Give us a ⭐️ on +++https://github.com/Azure-Samples/contoso-chat+++ 
 - [X] Join our [Discord Community](https://aka.ms/aitour/contoso-chat/discord)
 - [X] Read our blog post on [Code-First Development on Azure](https://aka.ms/ai-studio/code-first-blog)
 - [X] Read our blog series on [Building Intelligent Apps on Azure AI](https://aka.ms/ai-studio/intelligent-apps)
 - [X] Explore our learn collection on [Code-First Development with Azure AI](https://aka.ms/ai-studio/collection)

===

[🏠 Home](#pre-requisites) ⎯ [🧭 Table Of Contents](#table-of-contents)

---

## Table Of Contents

- [**Pre-Requisites**](#pre-requisites)
    - [01. Get Started](#1-get-started)
    - [02. Launch GitHUb Codespaces](#2-launch-github-codespaces)
    - [03. Visit Azure Portal](#3-visit-azure-portal)
    - [04. Visit Azure AI Studio](#4-visit-azure-ai-studio)
    - [05. Lab Overview](#5-lab-overview)
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

🎉 **Pro Tip** Use the Table Of Contents to navigate quickly to sections!

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