# 17. PromptFlow: Run

> [!hint]
> In the previous section, you should have opened Visual Studio Code, navigated to the _contoso-chat_ folder, and opened the _flow.dag.yaml_ file in the Visual Editor view.

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


---

🥳 **Congratulations!** <br/> You ran your contoso-chat prompt flow successfully in the local runtime on GitHub Codespaces. Next, we want to _evaluate_ the performance of the flow.
