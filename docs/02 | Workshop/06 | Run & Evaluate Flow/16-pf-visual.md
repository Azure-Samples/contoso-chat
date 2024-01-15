# 16. PromptFlow: Visual Editor

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
