# 15. PromptFlow: Codebase

> [!NOTE]
> Our environment, resources and connections are configured. Now, let's learn about prompt flow and how it works. A **prompt flow is a DAG (directed acyclic graph)** made of up **nodes** connected together in a **flow**. Each node is a **function tool** (written in Python) that can be edited and customized to suit your needs.

* []  **01** | Let's explore the Prompt Flow extension
    - Click the "Prompt Flow" icon in the Visual Studio Code sidebar
    - You should see a slide-out menu with the following sections
        - **Quick Access** - Create new flows, install dependencies etc,
        - **Flows** - Lists flows in project (defined by _flow.dag.yaml_)
        - **Tools** - Lists available _function_ tools (used in flow nodes)
        - **Batch Run History** - flows run against data or other runs
        - **Connections** - Lists connections & helps create them
    - We'll revisit this later as needed, when executing prompt flows.

* []  **02** | Let's understand prompt flow folders & structure
    - Click the "Explorer" icon in the Visual Studio Code sidebar
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
