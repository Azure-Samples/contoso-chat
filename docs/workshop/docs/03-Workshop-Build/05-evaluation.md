# 5️⃣ | Evaluate with AI

To make sure our app is working as intended, we can **evaluate** its response (the ANSWER) given the customer's QUESTION and the CONTEXT provided. We will evaluate the responses according to the following criteria:

* **Coherence**: how well all the sentences in the ANSWER fit together and sound naturally as a whole
* **Fluency**: the quality of individual sentences in the ANSWER, and whether they are well-written and grammatically correct
* **Groundedness**: given CONTEXT, whether the ANSWER uses information provided by the CONTEXT
* **Relevance**: how well the ANSWER addresses the main aspects of the QUESTION, based on the CONTEXT

These evaluations _could_ be performed by a human, who could use their subjective judgement to rate an answer on a scale from one star to five stars. But in this section, we will **automate** the process using a powerful generative AI model (GPT-4) to evaluate responses.

# Step 1: Understand custom Prompty Evaluators

Prompty files to evaluate answers on the criteria above can be found in the repository at `src/api/evaluators/custom_evals`.

1. Open the `src/api/evaluators/custom_evals` folder in VS Code Explorer
1. Open the file `coherence.prompty` look at it. The default inputs in the `sample:` section are:
    - **question**: What feeds all the fixtures in low voltage tracks instead of each light having a line-to-low voltage transformer?
    - **context**: Track lighting, invented by Lightolier, was popular at one period of time because it was much easier to install than recessed lighting, and individual fixtures are decorative and can be easily aimed at a wall. It has regained some popularity recently in low-voltage tracks, which often look nothing like their predecessors because they do not have the safety issues that line-voltage systems have, and are therefore less bulky and more ornamental in themselves. A master transformer feeds all of the fixtures on the track or rod with 12 or 24 volts, instead of each light fixture having its own line-to-low voltage transformer. There are traditional spots and floods, as well as other small hanging fixtures. A modified version of this is cable lighting, where lights are hung from or clipped to bare metal cables under tension
    - **answer**: The main transformer is the object that feeds all the fixtures in low voltage tracks.
1. Run the prompty file. You will see output like this:
    ```bash
    2024-09-16 21:35:43.602 [info] Loading /workspaces/contoso-chat/.env
    2024-09-16 21:35:43.678 [info] Calling ...
    2024-09-16 21:35:44.488 [info] 5
    ```
    - The system has given this ANSWER a coherence score of 5 out of 5 stars. Do you agree with the assessment?    
1. Take another look at the prompty file. The meta-prompt provides guidance to the AI model on how to perform the assessment, and to provide its rating as a score from 1 to 5. 

    !!! info "Note the several examples given in the Prompty file of answers that represent each of the star ratings. This is an example of [few-shot learning](https://learn.microsoft.com/azure/ai-services/openai/concepts/advanced-prompt-engineering?pivots=programming-language-chat-completions#few-shot-learning), a common technique used to guide AI models."

1. Repeat the process for the other Prompty files:

    - `fluency.prompty`
    - `groundedness.prompty`
    - `relevance.prompty`

# Step 2: Execute AI-Assisted Evaluation

Now that you understand the process of evaluation, let's evaluate the perfomance of our Contoso Chat application on a suite of test questions.

1. Click on `src/api/evaluate-chat-flow.ipynb`
    - You will see: a Jupyter notebook
    - Click Select Kernel, choose "Python Environments" and then choose the recommended (starred) option: Python 3.11.x.
    - Click Run all. **This will take a while**, so while it's running let's take a look at the process in detail.

1. Open the file `src/api/evaluators/data.jsonl`
    - This file contains the suite of test questions, each associated with a specific customer.
       - Sample question: "what is the waterproof rating of the tent I bought?"

1. Take another look at  `src/api/evaluate-chat-flow.ipynb`
    - Look at Cell 3, beginning `def create_response_data(df):`
    - For each question in the file, the `get_response` function is used to call our deployed endpoint and generate the response and associated context
    - Each response is then evaluated for the four criteria, given the supplied question and returned context.

1. When the notebook completes, check out the results of the evaluations in these files created in the  `src/api/evaluators` folder:
    - **Chat Responses** = `result.jsonl`
    - **Evaluated Results** = `result_evaluated.jsonl` (The scores are at the end of each line.)
    - **Evaliation Summary** = computed from `eval_results.jsonl` (Complete data from the evaluation process.)

# Step 3: Understand Evaluation Workflow

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

!!! success "Congratulations! You just used custom evaluators in an AI-Assisted Evaluation flow!"

# Step 4: Understand Observability with Tracer (optional)

- Revisit the `contoso_chat/chat_request.py` and `evaluators/coherence.py` files
- Explain the `PromptyTracer` and `@trace` decoration features
- Look for the `src/api/.runs` folder and click on a `.tracy` file
- Explore the traces to understand the telemetry captured for debugging

# Step 5 (Optional) Homework

**Here are some other things to try when you run this workshop at home:** 

- Build a new evaluator that assesses a metric you made up 
- Define the scoring criteria, and give examples of usage
- Create the test dataset, then assess results against your evaluator. 
- Think about how this approach extends to _safety_ evaluations. 

---

_In this section, you saw how Prompty-based custom evaluators work with AI-Assisted evaluation, to assess the quality of your application using defined metrics like coherence, fluency, relevance, and groundedness. You got a sense for how these custom evaluators are crafted._



!!! example "Next → [Let's Talk About Deployment!](./06-operationalization.md) and related ideas for operationalization!"