# AI-Assisted Evaluation

!!! success "Let's Review where we are right now"

    ![Dev Workflow](./../img/workshop-developer-flow.png)

    In the previous step, we learned to prototype our application iteratively using Prompty assets and tooling. And we tested each iteration manually, _with a single sample input_. In this stage, we assess the prototype for production readiness by testing it with a **larger dataset of test inputs**. 
    
    And we use _AI-Assisted Evaluation_ to make this scalable, using a second AI (generative AI model) to grade the responses from our application (on a scale of `1-5`) using custom criteria, for quality and safety.

In this section, we'll learn to assess the **quality** of our application responses using AI-Assisted evaluation, with this 3-step workflow:

1. We define a representative set of test inputs in a JSON file (see `evaluators/data.jsonl`)
1. Our application processes these inputs, storing the results (in `evaluators/results.jsonl`)
1. Our evaluators grade results for 4 quality metrics (in `evaluators/eval_results.jsonl`)

---

!!! info "Connect The Dots: How does AI-Assisted Evaluation Work? 💡 "

**During the ideation phase, we use a single test input (sample) to evaluate our chat AI.** We do this by _manually_ checking the copilot response to that test input, then iterating our prompt asset till the response is satisfactory. But this approach does not scale to the diverse set of possible test inputs that may happen in the real world.

**In the evaluation phase, we use a second AI to evaluate the first one.** We do this by _instructing_ a second generative AI model (the evaluator AI) to "grade" the chat AI (copilot) using a set of custom scoring criteria that we provide. The evaluator AI takes `{question, response}` pairs as inputs and grades them to return a `score` in the 1-5 range, **for the specific metric** being evaluated.

**We can build prompt-based custom evaluators** forquality assessments with Prompty. Let's see this in action.
