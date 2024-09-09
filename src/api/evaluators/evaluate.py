# %%
import os
import json
import prompty
from custom_evals.coherence import coherence_evaluation
from custom_evals.relevance import relevance_evaluation
from custom_evals.fluency import fluency_evaluation
from custom_evals.groundedness import groundedness_evaluation
import jsonlines

# %% [markdown]
# ## Get output from data and save to results jsonl file

# %%
import pandas as pd

data_path = "data.jsonl"

df = pd.read_json(data_path, lines=True)
df.head()

# %%
# import python file from /workspaces/contoso-chat/src/api/contoso_chat/chat_request.py
import sys
sys.path.append('/workspaces/contoso-chat/src/api/contoso_chat')
from chat_request import get_response

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

# %%
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

# Print results

df = pd.read_json('result_evaluated.jsonl', lines=True)
df.head()

# %%
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
with jsonlines.open('eval_results.jsonl', 'w') as writer:
    writer.write(results)

print("Results saved to result_evaluated.jsonl")

# %%



