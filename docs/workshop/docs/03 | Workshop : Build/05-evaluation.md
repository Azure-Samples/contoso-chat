# 5️⃣ | Evaluate with AI

??? info "Step 1: Understand custom Prompty Evaluators"

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

??? info "Step 2: Execute AI-Assisted Evaluation"
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

??? info "Step 3: Understand Evaluation Workflow"

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

??? info "Step 4: Understand Observability with Tracer (optional)"

    - Revisit the `contoso_chat/chat_request.py` and `evaluators/coherence.py` files
    - Explain the `PromptyTracer` and `@trace` decoration features
    - Look for the `src/api/.runs` folder and click on a `.tracy` file
    - Explore the traces to understand the telemetry captured for debugging

??? success "Congratulations 🎉 - You used AI-Assisted Evaluation with custom evaluators!"

---
