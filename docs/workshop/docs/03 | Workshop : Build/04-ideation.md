# 4️⃣ | Ideate With Prompty

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

??? success "Congratulations 🎉 - You learned prompt engineering with Prompty!"

    - First, create a base prompt and configure the model, parameters
    - Next, modify frontmatter to personalize usage, define inputs & test sample
    - Then, modify body to reflect system context, instructions and template structure
    - Last, create code to run Prompty from command-line or in automated workflows


    Iterate and explore changes and their impact on prompt response quality & cost. With each iteration, you should get closer to the `contoso_chat/chat.prompty` final version. Delete your `sandbox/` folder when done, to keep original app source in focus

---