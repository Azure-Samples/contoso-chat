import os
import sys
import json
import pandas as pd
from promptflow.core import AzureOpenAIModelConfiguration
from promptflow.evals.evaluators import RelevanceEvaluator, GroundednessEvaluator, FluencyEvaluator, CoherenceEvaluator
from promptflow.evals.evaluate import evaluate

sys.path.append('../contoso_chat')
from chat_request import get_response

if __name__ == '__main__':
    # Initialize Azure OpenAI Connection
    model_config = AzureOpenAIModelConfiguration(
            azure_deployment="gpt-4",
            api_version=os.environ["AZURE_OPENAI_API_VERSION"],
            azure_endpoint=os.environ["AZURE_OPENAI_ENDPOINT"]
        )
    
    # set the path to the data file to use for evaluations
    data_path = "../data/data.jsonl"

    # Check if the file exists and is not empty
    if os.path.isfile(data_path) and os.path.getsize(data_path) > 0:
        # Read the JSON lines file into a pandas DataFrame
        df = pd.read_json(data_path, lines=True)
        df.head()
    else:
        print(f"No data found at {data_path}")

    # Create evaluators for different evaluation metrics
    relevance_evaluator = RelevanceEvaluator(model_config)
    groundedness_evaluator = GroundednessEvaluator(model_config)
    fluency_evaluator = FluencyEvaluator(model_config)
    coherence_evaluator = CoherenceEvaluator(model_config)

    # Perform evaluation using the evaluate function
    result_eval = evaluate(
        data="../data/data.jsonl",
        target=get_response,
        evaluators={
            "relevance": relevance_evaluator,
            "fluency": fluency_evaluator,
            "coherence": coherence_evaluator,
            "groundedness": groundedness_evaluator,
        },
        evaluator_config={
            "defaultS": {
                "question": "${data.question}",
                "answer": "${target.question}",
                "context": "${target.chat_history}",
            },
        },
    )
    
    # # Print result_eval to json file
    # with open('result_eval.json', 'w') as f:
    #     json.dump(result_eval, f)

    # Convert the evaluation results to a pandas DataFrame
    eval_result = pd.DataFrame(result_eval["rows"])
    
    # parse result_eval to capture the studio_url
    studio_url = result_eval["studio_url"]

    # write the studio_url to a file
    with open('studio_url.txt', 'w') as f:
        f.write(studio_url)
    
    # Format data for markdown, drop unneeded columns from dataframe
    fmtresult = eval_result.drop(['outputs.context', 'outputs.answer', 'inputs.customerId', 'inputs.chat_history', 'inputs.intent', 'line_number'], axis=1)

    # Save the evaluation results as JSON lines and Markdown files
    eval_result.to_json('eval_result.jsonl', orient='records', lines=True)
    
    # Create headers for our markdown table
    headers = ["ID", "Question", "Relevance", "Fluency", "Coherence", "Groundedness"]
    
    # Print the formatted evaluation results
    fmtresult.to_markdown('eval_result.md', headers=headers)
