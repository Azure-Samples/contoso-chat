# 5️⃣ | Evaluate with AI

!!! success "Let's Review where we are right now"

    ![Dev Workflow](./../img/workshop-developer-flow.png)

    In the previous step, we learned to iteratively build our application prototype using Prompty assets and tooling, manually testing each iteration with a single test input.  In this `EVALUATE` stage, we now make test the application with a **larger set of test inputs**, using **AI Assisted Evaluation** to grade the responses (on a scale of `1-5`) for quality and safety based on pre-defined criteria.

## AI-Assisted Evaluation

Evaluation helps us make sure our application meets desired quality and safety criteria in the responses it generates. In this section, we'll learn how to assess the _quality_ of responses from our application using a 3-step workflow:

1. We define a representative set of test inputs in a JSON file (see `evaluators/data.jsonl`)
1. Our application processes these inputs, storing the results (in `evaluators/results.jsonl`)
1. Our evaluators grade results for 4 quality metrics (in `evaluators/eval_results.jsonl`)

While this workflow can be done manually, with a human grader providing the scores, it will not scale to the diverse test inputs and frequent design iterations required for generative AI applications. Instead, we use **AI Assisted Evaluation** effectively getting a second AI application (evaluator) to grade the first AI application (chat) - based on a scoring task that we define using a custom evaluator (Prompty). Let's see how this works.

## Step 1: Understand Metrics

The chat application generates its response (ANSWER) given a customer input (QUESTION) and support knowledge (CONTEXT) that can include the customer_id and chat_history. We then assess the _quality_ of the ANSWER using 4 metrics, each scored on a scale of 1-5.

| Metric | What it assesses |
|:--|:--|
| **Coherence** | How well do all sentences in the ANSWER fit together? <br/> Do they sound natural when taken as a whole? |
| **Fluency** | What is the quality of individual sentences in the ANSWER? <br/> Are they well-written and grammatically correct? |
| **Groundedness**| Given support knowledge, does the ANSWER use the information provided by the CONTEXT? |
| **Relevance**| How well does the ANSWER address the main aspects of the QUESTION, based on the CONTEXT? |

## Step 2: Understand Evaluators

The "scoring" task could be performed by a human, but this does not scale. Instead, we use AI-assisted evaluation by using one AI application ("evaluator") to grade the other ("chat"). And just like we used a `chat.prompty` to define our chat application, we can design `evaluator.prompty` instances that define the grading application - with a **custom evaluator** for each assessed metric.

### 2.1 View/Run all evaluators.

1. Navigate to the `src/api/evaluators/custom_evals` folder in VS Code.
1. Open each of the 4 `.prompty` files located there, in the VS Code editor.
    - `fluency.prompty`
    - `coherence.prompty`
    - `groundedness.prompty`
    - `relevance.prompty`
1. Run each file and observe the output seen frm Prompty execution.
1. **Check:** You see prompty for Coherence, Fluency, Relevance and Groundedness.
1. **Check:** Running the prompty assets gives scores between `1` and `5`

Let's understand how this works, taking one of these custom evaluators as an example.


### 2.2 View Coherence Prompty

1. Open the file `coherence.prompty` and look at its structure

    1. You should see: **system** task is

        > You are an AI assistant. You will be given the definition of an evaluation metric for assessing the quality of an answer in a question-answering task. Your job is to compute an accurate evaluation score using the provided evaluation metric. You should return a single integer value between 1 to 5 representing the evaluation metric. You will include no other text or information.

    1. You should see: **inputs** expected are

        - `question` = user input to the chat model
        - `answer` = response provided by the chat model
        - `context` = support knowledge that the chat model was given

    1. You should see: **meta-prompt** guidance for the task:

        > Coherence of an answer is measured by how well all the sentences fit together and sound naturally as a whole. Consider the overall quality of the answer when evaluating coherence. Given the question and answer, score the coherence of answer between one to five stars using the following rating scale:
        >
        > - One star: the answer completely lacks coherence
        > - Two stars: the answer mostly lacks coherence
        > - Three stars: the answer is partially coherent
        > - Four stars: the answer is mostly coherent
        > - Five stars: the answer has perfect coherency

    1. You should see: **examples** that provide guidance for the scoring.

        > This rating value should always be an integer between 1 and 5. So the rating produced should be 1 or 2 or 3 or 4 or 5.
        > (See examples for question-answer-context inputs that reflect 1,2,3,4 and 5 scores)

### 2.3 Run Coherence Prompty

1. You see: **sample input** for testing

    | question | What feeds all the fixtures in low voltage tracks instead of each light having a line-to-low voltage transformer? |
    |:---|:---|
    | answer| The main transformer is the object that feeds all the fixtures in low voltage tracks. |
    | context| Track lighting, invented by Lightolier, was popular at one period of time because it was much easier to install than recessed lighting, and individual fixtures are decorative and can be easily aimed at a wall. It has regained some popularity recently in low-voltage tracks, which often look nothing like their predecessors because they do not have the safety issues that line-voltage systems have, and are therefore less bulky and more ornamental in themselves. A master transformer feeds all of the fixtures on the track or rod with 12 or 24 volts, instead of each light fixture having its own line-to-low voltage transformer. There are traditional spots and floods, as well as other small hanging fixtures. A modified version of this is cable lighting, where lights are hung from or clipped to bare metal cables under tension |

1. Run the prompty file. You see output like this. This means the evaluator "assessed" this ANSWER as being very coherent (score=5). 

    ```bash
    2024-09-16 21:35:43.602 [info] Loading /workspaces/contoso-chat/.env
    2024-09-16 21:35:43.678 [info] Calling ...
    2024-09-16 21:35:44.488 [info] 5
    ```

1. **Observe:** Recall that coherence is about how well the sentences fit together. 
    - Given the sample input, do you agree with the assessment?   

1. **Change Answer**
    - replace sample answer with: `Lorem ipsum orci dictumst aliquam diam` 
    - run the prompty again. _How did the score change?_
    - undo the change. Return the prompty to original state for the next step.

Repeat this exercise for the other evaluators on your own. Use this to build your intuition for each metric and how it defines and assesses response quality.

!!! info "Note the several examples given in the Prompty file of answers that represent each of the star ratings. This is an example of [few-shot learning](https://learn.microsoft.com/azure/ai-services/openai/concepts/advanced-prompt-engineering?pivots=programming-language-chat-completions#few-shot-learning), a common technique used to guide AI models."

---

## Step 3: Run Batch Evaluation

In the previous section, we assessed a single answer for a single metric, running one Prompty at a time. In reality, we will need to run assessments automatically across a large set of test inputs, with all custom evaluators, before we can judge if the application is ready for production use. In this exercise, we'll run a batch evaluation on our Contoso Chat application, using a Jupyter notebook.

### 3.1 Run Evaluation Notebook

Navigate to the `src/api` folder in Visual Studio Code.

- Click: `evaluate-chat-flow.ipynb` - see: A Jupyter notebook
- Click: Select Kernel - choose "Python Environments" - pick recommended `Python 3.11.x`
- Click: `Run all` - this kickstarts the multi-step evaluation flow.

!!! warning "Troubleshooting: Evaluation gives an error message in the Notebook"

    On occasion, the evaluation notebook may throw an error after a few iterations. This is typically a transient error. To fix it, `Clear outputs` in the Jupyter Notebook, then `Restart` the kernel. `Run All` should complete the run this time.


### 3.2 Watch Evaluation Runs

One of the benefits of using Prompty is the built-in `Tracer` feature that captures execution traces for the entire workflow. These trace _runs_ are stored in  `.tracy` files in the `api/.runs/` folder as shown in the figure below.

- Keep this explorer sidebar open while the evaluation notebook runs/
- You see: `get_response` traces when our chat application is running
- You see: `groundedness` traces when its groundeness is evaluated
- You see: similar `fluency`, `coherence` and `relevance` traces

![Eval](./../img/Evaluation%20Runs.png)

### 3.3 Explore: Evaluation Trace

Click on any of these `.tracy` files to launch the _Trace Viewer_ window seen at right. 

- Note that this may take a while to appear. 
- You may need to click several runs before seeing a full trace.

Once the trace file is displayed, explore the panel to get an intuition for usage

- See: sequence of steps in orchestrated flow (left)
- See: prompt files with `load-prepare-run` sub-traces
- See: Azure OpenAIExecutor traces on model use
- Click: any trace to see its timing and details in pane (right)

!!! info "Want to learn more about Prompty Tracing? [Explore the documentation](https://github.com/microsoft/prompty/tree/main/runtime/prompty#using-tracing-in-prompty) to learn how to configure your application for traces, and how to view and publish traces for debugging and observability."


## Step 4: Understand Eval Workflow

!!! note "The evaluation flow takes 7-9 minutes to complete. Let's use the time to explore the code and understand the underlying workflow in more detail"

### 4.1 Explore: Create Response

1. Open the file `src/api/evaluators/data.jsonl`
    - This file contains the suite of test questions, each associated with a specific customer.
       - Sample question: _"what is the waterproof rating of the tent I bought?"_

1. Take another look at  `src/api/evaluate-chat-flow.ipynb`
    - Look at Cell 3, beginning `def create_response_data(df):`
    - For each question in the file, the `get_response` function (from our chat application) is invoked to generate the response and associated context
    - The {question, context, response} triples are then written to the `results.jsonl` file.

### 4.2 Explore: Evaluate Response

1. Take another look at  `src/api/evaluate-chat-flow.ipynb`
    - Look a cell 4, beginning `def evaluate():`
    - **Observe**: It loads the results file from the previous step
    - **Observe**: For each result in file, it extracts the "triple"
    - **Observe**: For each triple, it executes the 4 evaluator Promptys
    - **Observe**: It writes the scores to an `evaluated_results.jsonl` file

### 4.3 Explore: Create Summary

1. When notebook execution completes, look in the `src/api/evaluators` folder:
    - You see: **Chat Responses** in `result.jsonl`
    - You see: **Evaluated Results** in `result_evaluated.jsonl` (scores at end of each line)
    - You see: **Evaluation Summary** computed from `eval_results.jsonl` (complete data.)

1. Scroll to the bottom of the notebook to view the results cell:
    - Click the `View as scrollable element` link to redisplay output
    - Scroll to the bottom of redisplayed cell to view scores table
    - You should see something like the table below - we reformatted it manually for clarity.

![Eval](./../img/tabular-eval.png)

### 4.4 Understand: Eval Results

The figure shows you what that tabulated data looks like in the notebook results. Ignore the formatting for now, and let's look at what this tells us:

1. You see 12 rows of data - corresponding to 12 test inputs (in `data.jsonl`)
1. You see 4 metrics from custom evaluators - `groundedness`,`fluency`,`coherence`,`relevance`
1. Each metric records a score - between `1` and `5`

Let's try to put the scores in context of the responses we see. Try these exercises:

1. Pick a row above that has a `groundedness` of 5.
    - View the related row in the `result_evaluation.jsonl` file
    - Observe related answer and context in file - _was the answer grounded in the context?_
1. Pick a row that has a `groundedness` of 1.
    - View the related row in the `result_evaluation.jsonl` file
    - Observe related answer and context in file - _was THIS answer grounded in the context?_

As one example, we can see that the first response in the visualized results (`row 0`) had a groundedness of 5, while the third row from the bottom (`row 9`) had a groundedness of 1. You might find that in the first case the answers provided matched the data context. While in the second case, the answers may quote specific context but did not actually reflect correct usage.

!!! note "Explore the data in more detail on your own. Try to build your intuition for how scores are computed, and how that assessment reflects in the quality of your application."

## Step 5 (Optional) Homework

!!! success "Congratulations! You just used custom evaluators in an AI-Assisted Evaluation flow!"


We covered a lot in this section!! But there's a lot more left to learn. Here are two areas for you to explore on your own, when you revisit this workshop at home.

### 5.1 Explore: Observability 

- Revisit the `contoso_chat/chat_request.py` and `evaluators/coherence.py` files
    - **Observe:** the `PromptyTracer` and `@trace` decoration features
- Look for the `src/api/.runs` folder and click on a `.tracy` file
    - **Observe:** the traces to understand the telemetry captured for debugging
- What happens when we remove a `@trace` annotation from a method?
- What happens when we remove: `Tracer.add("PromptyTracer", json_tracer.tracer)`

### 5.2 Explore: Custom Evaluators

- Copy the `Coherence.prompty` to a new `Politeness.prompty` file
- Modify the **system** segment to define a "Politeness" metric
- Modify the **user** segment to define your scoring guidance
- Define a sample input & refine Prompty to return valid score
- Create the test dataset, then assess results against your evaluator. 
- Think about how this approach extends to _safety_ evaluations. 


---

_In this section, you saw how Prompty-based custom evaluators work with AI-Assisted evaluation, to assess the quality of your application using defined metrics like coherence, fluency, relevance, and groundedness. You got a sense for how these custom evaluators are crafted._



!!! example "Next → [Let's Talk About Deployment!](./06-operationalization.md) and related ideas for operationalization!"