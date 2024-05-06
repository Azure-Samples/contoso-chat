import os
import sys


script_dir = os.path.dirname(os.path.realpath(__file__))


contoso_chat_dir = os.path.join(script_dir, '../contoso_chat')


sys.path.append(contoso_chat_dir)


from chat_request import get_response


import json

import pandas as pd

from promptflow.core import AzureOpenAIModelConfiguration

from promptflow.evals.evaluators import RelevanceEvaluator, GroundednessEvaluator, FluencyEvaluator, CoherenceEvaluator

from promptflow.evals.evaluate import evaluate

# Initialize Azure OpenAI Connection
model_config = AzureOpenAIModelConfiguration(
        azure_deployment="gpt-4",
        api_key=os.environ["AZURE_OPENAI_API_KEY"],
        api_version=os.environ["AZURE_OPENAI_API_VERSION"],
        azure_endpoint=os.environ["AZURE_OPENAI_ENDPOINT"]
    )

data_path = "jldeen/data.jsonl"

# Check if the file exists and is not empty
if os.path.isfile(data_path) and os.path.getsize(data_path) > 0:
    df = pd.read_json(data_path, lines=True)
    df.head()
else:
    print(f"No data found at {data_path}")

relevance_evaluator = RelevanceEvaluator(model_config)
groundedness_evaluator = GroundednessEvaluator(model_config)
fluency_evaluator = FluencyEvaluator(model_config)
coherence_evaluator = CoherenceEvaluator(model_config)

result_eval = evaluate(
    data="jldeen/data.jsonl",
    target=get_response,
    evaluators={
        #"violence": violence_eval,
        "relevance": relevance_evaluator,
        "fluency": fluency_evaluator,
        "coherence": coherence_evaluator,
        "groundedness": groundedness_evaluator,
    },
    # column mapping    return {"question": question, "answer": result, "context": context}
    evaluator_config={
        "defaultS": {
            "question": "${data.question}",
            "answer": "${target.question}",
            "context": "${target.chat_history}",
        },
    },
)

eval_result = pd.DataFrame(result_eval["rows"])

eval_result.head()

eval_result.to_json('eval_result.jsonl', orient='records', lines=True)
