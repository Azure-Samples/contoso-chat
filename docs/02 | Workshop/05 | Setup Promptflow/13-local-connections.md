# 13. VSCode Config Connections

> [!NOTE]
_This assumes you completed all Azure resource setup and VS Code configuration for those resources. Now let's setup **local Connections** so we can run the prompt flow in VS Code later._

* []  **01** | Return to the Visual Studio Code editor tab

* []  **02** | Setup a local third-party backend to store keys
    - Open the Visual Studio Code terminal 
    - Type +++pip install keyrings-alt+++ and hit Enter
    - Installation should complete quickly

* []  **03** | Run the notebook to set local prompt flow connections
    - Locate the "connections/" folder
    - Open the **create-connections.ipynb** Jupyter Notebook.
    - Click **Select Kernel**, set recommended Python environment 
    - Click **Clear All Outputs** then **Run All** & verify completion

* []  **04** | Validate connections were created
    - Return to Visual Studio Code terminal
    - Type +++pf connection list+++ and hit Enter
    - Verify 3 connections were created *with these names* <br/> **"contoso-search", "contoso-cosmos", "aoai-connection"**

---

🥳 **Congratulations!** <br/> Your *local connections* to the Azure AI project are ready!
