# 19. PromptFlow: Deploy

> [!hint]
> Till now, you've explored, built, tested, and evaluated, the prompt flow _from Visual Studio Code_, as a developer. Now it's time to _deploy the flow to production_ so applications can use the endpoint to make requests and receive responses in real time.

**Deployment Options**: We will be [using Azure AI Studio](https://learn.microsoft.com/azure/ai-studio/how-to/flow-deploy?tabs=azure-studio) to deploy our prompt flow from a UI. You can also deploy the flow programmatically [using the Azure AI Python SDK](https://learn.microsoft.com/azure/ai-studio/how-to/flow-deploy?tabs=python). 

**Deployment Process**: We'll discuss the 4 main steps:
- First, upload the prompt flow to Azure AI Studio
- Next, test upload then deploy it interactively
- Finally, use deployed endpoint (from built-in test)
- Optionally: use deployed endpoint (from real app)

>[!note] **1: Upload Prompt Flow** to Azure AI Studio. 

* []  **01** | Return to the Visual Studio Code editor tab
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

* []  **04** | Run Prompt Flow in Azure
    - On completion, you should see a ✅
    - Now click the blue **Run** button
    - Run should complete in a few minutes.
    - Verify that all graph nodes are green (success)

>[!note] **2: Deploy Prompt Flow** now that it's tested

* []  **01** | Click the **Deploy** option in flow page
    - Opens a Deploy wizard flow
    - **Endpoint name:** use +++contoso-chat-aiproj-ep+++
    - **Deployment name:** use +++contoso-chat-aiproj-deploy+++
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
> The deployment process **can take 10 minutes or more**. Use the time to explore other things.

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

>[!note] **1: Use Deployed Endpoint** with a built-in test. 

* []  **01** | Click the **Test** option in deployment page
     - Enter "[]" for **chat_history**
     - Enter +++What can you tell me about your jackets?+++ for **question**
     - Click **Test** and watch _Test result_ pane
     - Test result output should show LLM app response

Explore this with other questions or by using different customer Id or chat_history values if time permits.

---

🥳 **Congratulations!** <br/> You made it!! You just _setup, built, ran, evaluated, and deployed_ a RAG-based LLM application using Azure AI Studio and Prompt Flow.
