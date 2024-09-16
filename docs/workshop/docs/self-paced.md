# Self-Guided Edition

These are the instructions for a **self-guided** tour of the Contoso Chat sample. This version is designed for **self-paced** learning but will require you to bring your own subscription and provision the resources yourself.

!!! warning "PRE-REQUISITES FOR THIS WORKSHOP"

    To participate in this workshop you will need the following:

    1. **Your own laptop.** Should have a modern browser, preferably Microsoft Edge.
    1. **A GitHub account.** A personal account with GitHub Codespaces access.
    1. **An Azure subscription.** With access to Azure OpenAI Model deployments.
    1. **Familiarity with VS Code.** Our default development environment.
    1. **Familiarity with Python**. Our default coding language.

---


## 1. Getting Started

Let's setup our development environment and kickstart the self-deployment process:


??? note "Step 1: Launch GitHub Codespaces in tab 2️⃣"

    1. Open a browser tab 1️⃣ 
    1. Navigate to ([Contoso Chat](https://aka.ms/aitour/contoso-chat)) sample
    1. Log into GitHub - use a personan login for optimal experience
    1. Fork the sample to your profile - uncheck `main` to get branches
    1. Switch to `aitour-fy25` branch in your fork - click the **Code** button
    1. Select `Codespaces` tab - click `Create new codespaces on aitour-fy25`
    
    This should launch Codespaces in a new browser tab 2️⃣,

    1. Verify that the tab shows a Visual Studio Code editor
    1. GitHub Codespaces is loading .. this will take a while.
    1. ✅ | Your Codespaces tab is live!


??? note "Step 2: View Azure Portal in tab 3️⃣"

    1. Open new browser tab 2️⃣
    1. Navigate to the [Azure Portal](https://portal.azure.com)
    1. Login with **your Azure username and password**
    1. Click on `Resource Groups` - leave this open for later review.
    1. ✅ | Your Azure Portal tab is live!

??? note "Step 4: View Azure AI Studio in tab 4️⃣"

    1. Open new browser tab 4️⃣
    1. Navigate to the [Azure AI Studio](https://ai.azure.com)
    1. Click `Sign in` - should auto-login with prior Azure credentials
    1. Click `All resources`  - leave this open for later review
    1. ✅ | Your Azure AI Project tab is live!

??? note "Step 5: Authenticate with Azure from tab 2️⃣"

    1. Return to GitHub Codespaces tab 2️⃣
    1. Verify that terminal is visible and extensions installed
    1. Authenticate with Azure CLI
        - `az login --use-device-code`
        -  follow instructions and complete auth workflow
        - select the valid Azure subscription and tenant to use
        - ✅ | You are logged into Azure CLI
    1. Authenticate with Azure Developer CLI
        - `azd auth login`
        -  follow instructions and complete auth workflow
        - You should see: "Logged in to Azure"
        - ✅ | You are logged into Azure Developer CLI

??? note "Step 6: Provision Azure with `azd` tab 2️⃣"
    1. Stay in tab 2️⃣ - enter `azd up`
    1. Enter a new environment name - use `AITOUR`
    1. Select a subscription - pick the one from step 5.
    1. Select a location - pick `francecentral` or `swedencentral`
    1. You should see: _You can view detailed progress in the Azure Portal .._
    1. When done you see: **SUCCESS: Your up workflow to provision and deploy to Azure completed in 16 minutes 35 seconds.**
    1. ✅ | Your Azure infra is being provisioned ..

??? note "Step 7: Track provisioning status in tab 3️⃣"
    1. Switch to the Azure Portal in tab 3️⃣
    1. Click on Resource Groups - see: `rg-AITOUR`
    1. Click on `rg-AITOUR` - see `Deployments` under **Essentials**
    1. Click `Deployments` - see Deployments page with activity and status ...
    1. Wait till all deployments complete - **this can take 20-25 minutes**
    1. See `Overview` page - **you should have 35 Deployment Items**
    1. See `Overview` page - **you should have 15 Deployed Resources**
    1. ✅ | Your Azure infra and application are ready!

??? note "Step 8: Validate Azure Cosmos DB is ready in tab 3️⃣"
    1. Switch to the Azure Portal tab 3️⃣ - `rg-AITOUR` resource Overview
    1. Click the `Azure Cosmos DB account` resource - visit details page
    1. Click `Data Explorer` in top-nav menu on details page 
        - dismiss the popup dialog 
        - see: `contoso-outdoors` container with `customers` database
        - click `customers` - select `Items`
        - you should see: **12 data items in database**
    1. ✅ | Your Azure Cosmos DB resources is ready!

??? note "Step 9: Validate Azure AI Search is ready in tab 3️⃣"
    1. Switch to the Azure Portal tab 3️⃣ - `rg-AITOUR` resource Overview
    1. Click the `Search service` resource - visit details page
    1. Click `Search Explorer` in top-nav menu on details page 
        - see Search explorer with default index `contoso-products`
        - click "Search" with no other input
        - should see: Results dialog fill with index data
    1. ✅ | Your Azure AI Search resource is ready!

??? note "Step 10: Validate Azure AI Project is ready in tab 4️⃣"
    1. Switch to Azure AI Studio in tab 4️⃣ - start on Home page
    1. Click `All resources` in sidebar - _Note: this may say `All hubs`_.
    1. Verify that you see a Hub resource - _Note: you may also see an AI Services resource_
    1. Click the hub resource - you should see a project listed in hub overview page
    1. Click the project resource - visit `Deployments` in the sidebar
        - see `aoai-connection` and `aoai-safety-connection` sections
        - each has 3 model deployments - we care about three of these
            -gpt-35-turbo, gpt-4, text-embedding-ada-002
    1. ✅ | Your Azure AIProject resource is ready!


??? note "Step 11: Validate Azure Container Apps is ready in tab 3️⃣"
    1. Switch to the Azure Portal tab 3️⃣ - `rg-AITOUR` resource Overview
    1. Click the `Azure Container App` resource - visit details page
    1. Click `Application Url` in **Essentials** section of Overview
    1. You should see: new tab 5️⃣ with page showing `{"message" : "Hello World" }" 
    1. ✅ | Your Azure Container App resource is ready **and** has app deployed!

??? note "Step 12: Test the Deployed Container App in tab 5️⃣ "
    1. Visit the `Application Url` page from Step 10 in tab 5️⃣
    1. Add a `/docs` suffix to that path - you should see: **FastAPI** page
    1. Expand the `POST` section by clicking the arrow
        - click `Try it out` to make inputs editable
        - enter `Tell me about your tents` for **question**
        - enter `2` for **customer_id**
        - enter []` for **chat_history**
        - enter **Execute** to run the query
    1. You should get a valid response with `answer` and `context`.
    1. ✅ | Your Contoso Chat AI is deployed - and works with valid inputs!

??? tip "This Completes Setup. Let's Review Status."

    At this stage you should have the following **5 tabs** open:

    1. Github Repo - starting tab 1️⃣
    1. GitHub Codespaces 2️⃣
    1. Azure Portal 3️⃣
    1. Azure AI Studio 4️⃣
    1. Azure Container Apps 5️⃣
    1. ✅ | All Azure resources are provisioned
    1. ✅ | Contoso Chat is deployed to ACA endpoint


We can now get to work on exploring the codebase in 3 stages,


---

## 2. Ideation With Prompty

??? danger "Step 1: Create a New Prompty"

    - create an empty folder in root of repo (e.g., `sandbox`)
    - switch to that directory in terminal: `cd sandbox`
    - right click to create `New Prompty` - you see: `basic.prompty`
    - run the prompty: you will be prompted to sign into Azure - do it.
    - Result: **You should get an Error**
        - ❌ | ` Error: 404 The API deployment for this resource does not exist.`

??? success "Step 2: Update model configuration"
    - Copy the previous prompty to a new one: `cp basic.prompty chat-0.prompty`
    - Update this line as shown: `azure_deployment: ${env:AZURE_OPENAI_CHAT_DEPLOYMENT}`
    - Run the prompty - should run immediately.
    - Result: **You should get a valid response**
        - ✅ | "[info] Hello Seth! I'd be happy to tell you about our tents ..."

??? success "Step 3: Update prompt template, add sample"
    - Let's start refactoring the prompt in steps, till we get to the Contoso Chat version
    - First: `cp ../docs/workshop/src/chat-1.* .` to get the next iteration
        - `chat-1.prompty` has customized frontmatter and starter template for Contoso chat
        - `chat-1.json` has a sample test file we can use for validating it
    - Run `chat-1.prompty`
        - You see: **valid response**
        - Try changing max_tokens to 3000 - what happens?
        - Try adding `Provide responses in a bullet list of items` to system - what happens?

??? success "Step 4: Update prompt template, add Safety"

    - Next: `cp ../docs/workshop/src/chat-2.* .` to get the next iteration
        - This adds: Safety section
        - Run default prompt and sample: Works as expected
        - Update sample; `cp ../docs/workshop/src/chat-2-jailbreak.json  chat-2.json`
        - Run it - the new input tries to jailbreak the app. What happens?
        - You should see: ` I'm sorry, but I'm not able to change my rules. My purpose is to assist you with questions related to Contoso Outdoors products. If you have any questions about our products or services, feel free to ask! 😊`

??? success "Step 5: Update prompt template, run as code"
    - Update sample; `cp ../docs/workshop/src/chat-3* .`
    - Right-click on the `chat-3.prompty` file: select `Add Prompty Code`
    - You should see `chat-3.py` - open it and add these lines at the top
        ```python
        ## Load environment variables
        from dotenv import load_dotenv
        load_dotenv()
        ```
    - Run it from within file by clicking the play icon.
    - you should see: valid result

You've learned how to explore prompt engineering iteratively with Prompty. Note that the `chat-3.prompty` file is getting closer to the `contoso_chat/chat.prompty` file. 

 - Try thinking about what other changes you can make and iterate as time permits. 
 - Delete your `sandbox/` folder when done, to keep original app source in focus

---

## 3. Evaluation With AI Assistance

??? success "Step 1: Understand custom Prompty Evaluators"

    - Switch to `src/api/evaluators/custom_evals`
    - You should see 4 prompty files. Open each in order, and run them
    - You should see something like this (output simplified for clarity)
        ```bash
        2024-09-16 21:35:43.602 [info] Loading /workspaces/contoso-chat/.env
        2024-09-16 21:35:43.678 [info] Calling ...
        2024-09-16 21:35:44.488 [info] 5

        2024-09-16 21:35:51.232 [info] Loading /workspaces/contoso-chat/.env
        2024-09-16 21:35:43.678 [info] Calling ...
        2024-09-16 21:35:52.081 [info] 4

        2024-09-16 21:35:57.213 [info] Loading /workspaces/contoso-chat/.env
        2024-09-16 21:35:43.678 [info] Calling ...
        2024-09-16 21:35:58.108 [info] 5

        2024-09-16 21:36:05.996 [info] Loading /workspaces/contoso-chat/.env
        2024-09-16 21:35:43.678 [info] Calling ...
        2024-09-16 21:36:06.910 [info] 5
        ```
    - These are the outputs from running evaluators for 4 metrics
        - Coherence = how well do sentences fit together
        - Fluency = quality of sentences in the answer
        - Groundedness = is answer logically derived from context provided
        - Relevance = does answer address the main elements of question
    - **Take a minute to open each prompty and understand the template setup.**

??? success "Step 2: Run AI-Assisted Evaluation Flow"
    - Click on `src/api/evaluate-chat-flow.ipynb`
    - You should see: a Jupyter notebook
        - `pip install tabulate` if not already installed
        - Select Kernel
        - Run all - **this will take a while**
    - Observe the following files while you wait
        - **Test Prompts** = `evaluators/data.jsonl`
        - **Chat Responses** = `result.jsonl`
        - **Evaluated Results** = `result_evaluated.jsonl`
        - **Evaliation Summary** = computed from `eval_results.jsonl`

??? success "Step 3: Explore AI-Assisted Evaluation Flow"

    - Walk through the steps in the notebook
        - Load test data - from JSONL file
        - Create response data - using the `chat.prompty` we are building
        - Evaluate results - using results from chat, for 4 criteria (promptys)
    - Explore the results of the notebook run
        - What are the evaluated criteria?
        - What are the scores?
        - How do scores reflect on the criteria and test responses?

    - Experiments you can try
        - Modify a custom evaluator prompty - change how it scores that criteria
        - Modify data.jsonl - add new test prompts to evaluate for edge cases

??? success "Step 4: Understand observability and tracing (optional)"

    - Revisit the `contoso_chat/chat_request.py` and `evaluators/coherence.py` files
    - Explain the `PromptyTracer` and `@trace` decoration features
    - Look for the `src/api/.runs` folder and click on a `.tracy` file
    - Explore the traces to understand the telemetry captured for debugging


---

## 4. Deploy With Azure Container Apps

??? success "Step 1: Explore the Codebase"

    - The Contoso Chat app is deployed as an Azure Container App (shown prior)
    - It is implemented as a FASTAPI endpoint with two routes ("/" and "/api/create_response")
    - View the `src/api/main.py` to learn about the parameters expected by the latter


??? success "Step 2: Test Endpoint Locally"

    1. Let's run the server locally, for testing:
        - go to the root of your repo
        - use this command: `fastapi dev src/api/main.py`
        - you should see popup dialog - click "Open in Browser"
        - you should see: 
    1. Add a `/docs` suffix to that path - you should see: **FastAPI** page
    1. Expand the `POST` section by clicking the arrow
        - click `Try it out` to make inputs editable
        - enter `Tell me about your tents` for **question**
        - enter `2` for **customer_id**
        - enter []` for **chat_history**
        - enter **Execute** to run the query
    1. You should get a valid response with `answer` and `context`.
    1. ✅ | You just tested your Contoso Chat app with valid inputs!

??? success "Step 3: Make changes & test (awareness only)"
    
    1. Make changes to `main.py` - e.g., change "Hello World" to "Hello AI Tour!"
    1. Run `fastapi dev src/api/main.py` again to see changes
        - default route at "/" now shows updated message
    1. The repository uses `azd` for deployment - learn more in the docs.
    
---

## 5. Wrap-up and shut down

??? info "End the Skillable Session"

    Visit the Skillable launch page and click `End Session` to end the session and release all resources. This allows the lab to be run again without quota issues for others.


??? info "Stop Your Codespaces"

    Visit [https://github.com/codespaces](https://github.com/codespaces) - locate the Codespaces instance you are currently running, and stop or delete it to prevent continued usage of the storage or processing quotas.
