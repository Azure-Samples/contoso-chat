# 11. VSCode Populate Search

> [!NOTE]
_This assumes you setup the Azure AI Search resource earlier. In this section, we'll populate it with product data and create the index._

* []  **01** | Return to the Visual Studio Code editor tab
    - Locate the "data/product_info/" folder
    - Open the **create-azure-search.ipynb** Jupyter Notebook.

* []  **02** | Run the notebook to populate search index
    - Click **Select Kernel** (top right)
    - Pick "Python Environments" and select recommended option
    - Click **Clear All Outputs** then **Run All**
    - Verify that all code cells executed correctly.

* []  **03** | Verify the search index was created
    - Open +++https://portal.azure.com+++ to Azure AI Search resource
    - Click the **Indexes** option in sidebar to view indexes
    - Verify that the **contoso-products** search index was created.

---

🥳 **Congratulations!** <br/> Your Azure AI Search index is ready!
