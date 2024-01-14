# 18. PromptFlow: Evaluate

> [!NOTE]
> You've built and run the _contoso-chat_ prompt flow locally using the Visual Studio Code Prompt Flow extension and SDK. Now it's time to **evaluate** the quality of your LLM app response to see if it's performing up to expectations. Let's dive in.

* []  **01** | First, run **evaluate-chat-prompt-flow.ipynb**
    - Locate the "eval/" folder
    - Open **evaluate-chat-prompt0flow.ipynb**.
    - Click **Select Kernel**, use default Python env
    - Click **Clear All Outputs**, then **Run All** 
    - Execution **takes some time**. Until then ....

* []  **02** | Let's explore what the notebook does
    - Keep Jupyter notebook open "Editor" pane
    - Open VS Code "Explorer" pane, select **Outline**
    - You should see these code sections:
        - Local Evaluation - **Groundedness**
        - Local Evaluation - **Multiple Metrics**
        - AI Studio Azure - **Batch run, json dataset**
        - Cloud Evaluation - **Multi-flow, json dataset**
    - Let's understand what each does.

* []  **03** | Local Evalution : Explore **Groundedness**
    - Evaluates **contoso-chat** for _groundedness_ 
    - This [**measures**](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in#ai-assisted-groundedness-1) how well the model's generated answers align with information from the source data (user-defined context).
    - **Example**: We test if the answer to the question _"Can you tell me about your jackets"_ is grounded in the product data we indexed previously. 

* []  **04** | Local Evaluation : Explore **Multiple Metrics**
    - Evaluates **contoso-chat** using [4 key metrics](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in#metrics-for-multi-turn-or-single-turn-chat-with-retrieval-augmentation-rag):
    - **Groundedness** = How well does model's generated answers align with information from the source (product) data?
    - **Relevance** = Extent to which the model's generated responses are pertinent and directly related to the given questions.
    - **Coherence** = Ability to generate text that reads naturally, flows smoothly, and resembles human-like language in responses.
    - **Fluency** = Measures the grammatical proficiency of a generative AI's predicted answer.

> [!NOTE]
> The above evaluation tests ran against a single test question. For more comprehensive testing, we can use Azure AI Studio to run **batch tests** using the same evaluation prompt, with the **data/salestestdata.jsonl** dataset. Let's understand how that works.

* []  **05** | Base Run : **With evaluation JSON dataset**
    - Use Azure AI Studio with automatic runtime
    - Use "data/salestestdata.jsonl" as _batch test data_
    - Do a _base-run_ using contoso-chat prompt flow
    - View results in notebook - visualized as table

* []  **06** | Eval Run : **With evaluation JSON dataset**
    - Use Azure AI Studio with automatic runtime
    - Use "data/salestestdata.jsonl" as _batch test data_
    - Do multi-flow eval with _base run as variant_
    - View results in notebook - visualized as table
    - Results should now show the 4 eval metrics
    - Optionally, click **Web View** link in final output
        - See **Visualize outputs** (Azure AI Studio)
        - Learn more on [viewing eval results](https://learn.microsoft.com/azure/ai-studio/how-to/flow-bulk-test-evaluation#view-the-evaluation-result-and-metrics)

* []  **07** | Review Evaluation Output
    - Check the Jupyter Notebook outputs
    - Verify execution run completed successfully
    - Review evaluation metrics to gain insight  

---

🥳 **Congratulations!** <br/> You've evaluated your contoso-chat flow for single-data and batch data runs, using single-metric and multi-metric eval flows. _Now you're ready to deploy the flow so apps can use it_. 