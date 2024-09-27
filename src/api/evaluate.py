# %%
import os
import json
import prompty
from evaluators.custom_evals.coherence import coherence_evaluation
from evaluators.custom_evals.relevance import relevance_evaluation
from evaluators.custom_evals.fluency import fluency_evaluation
from evaluators.custom_evals.groundedness import groundedness_evaluation
import jsonlines
import pandas as pd
from prompty.tracer import trace
from tracing import init_tracing
from contoso_chat.chat_request import get_response

# %% [markdown]
# ## Get output from data and save to results jsonl file

# %%
@trace
def load_data():
    data_path = "./evaluators/data.jsonl"

    df = pd.read_json(data_path, lines=True)
    df.head()
    return df

# %%
@trace
def create_response_data(df):
    results = []

    for index, row in df.iterrows():
        customerId = row['customerId']
        question = row['question']
        
        # Run contoso-chat/chat_request flow to get response
        response = get_response(customerId=customerId, question=question, chat_history=[])
        print(response)
        
        # Add results to list
        result = {
            'question': question,
            'context': response["context"],
            'answer': response["answer"]
        }
        results.append(result)

    # Save results to a JSONL file
    with open('result.jsonl', 'w') as file:
        for result in results:
            file.write(json.dumps(result) + '\n')
    return results

# %%
@trace
def evaluate():
    # Evaluate results from results file
    results_path = 'result.jsonl'
    results = []
    with open(results_path, 'r') as file:
        for line in file:
            print(line)
            results.append(json.loads(line))

    for result in results:
        question = result['question']
        context = result['context']
        answer = result['answer']
        
        groundedness_score = groundedness_evaluation(question=question, answer=answer, context=context)
        fluency_score = fluency_evaluation(question=question, answer=answer, context=context)
        coherence_score = coherence_evaluation(question=question, answer=answer, context=context)
        relevance_score = relevance_evaluation(question=question, answer=answer, context=context)
        
        result['groundedness'] = groundedness_score
        result['fluency'] = fluency_score
        result['coherence'] = coherence_score
        result['relevance'] = relevance_score

    # Save results to a JSONL file
    with open('result_evaluated.jsonl', 'w') as file:
        for result in results:
            file.write(json.dumps(result) + '\n')

    with jsonlines.open('eval_results.jsonl', 'w') as writer:
        writer.write(results)
    # Print results

    df = pd.read_json('result_evaluated.jsonl', lines=True)
    df.head()
    
    return df

# %%
@trace
def create_summary(df):
    print("Evaluation summary:\n")
    print(df)
    # drop question, context and answer
    mean_df = df.drop(["question", "context", "answer"], axis=1).mean()
    print("\nAverage scores:")
    print(mean_df)
    df.to_markdown('eval_results.md')
    with open('eval_results.md', 'a') as file:
        file.write("\n\nAverages scores:\n\n")
    mean_df.to_markdown('eval_results.md', 'a')

    print("Results saved to result_evaluated.jsonl")

# %%
# create main funciton for python script
if __name__ == "__main__":
   tracer = init_tracing(local_tracing=True)
   test_data_df = load_data()
   response_results = create_response_data(test_data_df)
   result_evaluated = evaluate()
   create_summary(result_evaluated)



