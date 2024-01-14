# 12. VSCode Populate Database

> [!NOTE]
_This assumes you setup the Azure CosmosDB resource earlier. In this section, we'll populate it with customer data._

* []  **01** | Return to the Visual Studio Code editor tab
    - Locate the "data/customer_info/" folder
    - Open the **create-cosmos-db.ipynb** Jupyter Notebook.

* []  **02** | Run the notebook to populate customer database
    - Click **Select Kernel**, set recommended Python environment 
    - Click **Clear All Outputs** then **Run All** & verify completion

* []  **03** | Verify the customer database was created
    - Open +++https://portal.azure.com+++ to Azure CosmosDB resource
    - Click the **Data Explorer** option in sidebar to view data
    - Verify that the **contoso-outdoor** container was created
    - Verify that it contains a **customers** database

---

🥳 **Congratulations!** <br/> Your Azure CosmosDB database is ready!
