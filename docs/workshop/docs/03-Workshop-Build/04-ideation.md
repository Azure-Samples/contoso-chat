# 4️⃣ | Ideate With Prompty

!!! success "Let's Review where we are right now"

    We still have these 5 tabs open.

    1. Github Repo - starting tab 1️⃣
    1. GitHub Codespaces 2️⃣
    1. Azure Portal 3️⃣
    1. Azure AI Studio 4️⃣
    1. Azure Container Apps 5️⃣

    We also have a fully-provisioned Azure infrastructure (backend), successfully deployed the first version of our application - and tested it manually, with a single input.


_Now it's time to understand how that application was developed - and specifically, understand how we can go from "prompt to prototype" in the **Ideation** phase of our developer workflow_.

??? danger "Step 1: Create a New Prompty"

    - create an empty folder in root of repo (e.g., `sandbox`)
    - switch to that directory in terminal: `cd sandbox`
    - right click to create `New Prompty` - you see: `basic.prompty`
    - run the prompty: you will be prompted to sign into Azure - complete auth flow.
    - Result: **You should get an Error** since model configuration is invalid
        - ❌ | ` Error: 404 The API deployment for this resource does not exist.`

??? info "Step 2: Update model configuration"

    - Copy the previous prompty to a new one: `cp basic.prompty chat-0.prompty`
    - Update this line as shown: `azure_deployment: ${env:AZURE_OPENAI_CHAT_DEPLOYMENT}`
    - Run the prompty - should run immediately.
    - Result: **You should get a valid response**
        - Example: "[info] Hello Seth! I'd be happy to tell you about our tents ..."
    - ✅ | Your prompty model configuration is working

??? info "Step 3: Update prompt template, add sample for testing"

    - Let's start refactoring the prompt in steps, till we get to the Contoso Chat version
    - First: `cp ../docs/workshop/src/chat-1.* .` to get the next iteration
        - `chat-1.prompty` has customized frontmatter and starter template for Contoso chat
        - `chat-1.json` has a sample test file we can use for validating it
    - Run `chat-1.prompty`
        - You see: **valid response**
        - Try changing max_tokens to 3000 - what happens?
        - Try adding `Provide responses in a bullet list of items` to system - what happens?
    - ✅ | Your prompty template is updated & uses sample test file

??? info "Step 4: Update prompt template, add Safety instructions"

    - Let's add a `Safety` guidance section
    - Run: `cp ../docs/workshop/src/chat-2.* .` to get version with Safety
        - Run default prompt and safe sample: Works as expected
        - Update to jailbreak sample; `cp ../docs/workshop/src/chat-2-jailbreak.json  chat-2.json`
        - Run it - the new input tries to jailbreak the app. 
        - What happens? You should see: 
            - ` I'm sorry, but I'm not able to change my rules. My purpose is to assist you with questions related to Contoso Outdoors products. If you have any questions about our products or services, feel free to ask! 😊`
    - ✅ | Your prompty now has Safety guidance built-in

??? info "Step 5: Update prompt template, run with Python code"
    - Let's run the Prompty asset from Python code.
    - Copy these files; `cp ../docs/workshop/src/chat-3* .`
    - Right-click on the `chat-3.prompty` file: select `Add Prompty Code`
    - It creates: `chat-3.py` - open it and add these lines at the top
        ```python
        ## Load environment variables
        from dotenv import load_dotenv
        load_dotenv()
        ```
    - Run the file by clicking the play icon. You should see a valid result.

!!! quote "Congratulations! You just learned prompt engineering with Prompty!"

    Let's recap what we tried:

    - First, create a base prompt → configure the model, parameters
    - Next, modify frontmatter → spersonalize usage, define inputs & test sample
    - Then, modify the body →  reflect system context, instructions and template structure
    - Finally, create executable code →  run Prompty from command-line or in automated workflows

    We saw how these simple tools can help us implement safety guidance for our prompts and iterate on our prompt template design quickly and flexibly, to get to our first prototype. The sample data file  provides a test input for rapid iteration, and it allows us understand the "shape" of data we will need, to implement this application in production.

---

_In this section, you saw how Prompty tooling supports rapid prototyping - starting with a basic prompty. Continue iterating on your own to get closer to the `contoso_chat/chat.prompty` target. You can now delete the `sandbox/` folder, to keep original app source in focus_.

!!! example "Next → [Let's Evaluate with AI!](./05-evaluation.md) and learn about custom evaluators!"
