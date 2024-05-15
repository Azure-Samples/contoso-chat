
import requests
import json
DEPLOYMENT_NAME="os-aml-mixtral-deployment-1"
ENDPOINT_URL="https://nim-aml-endpoint-1.westeurope.inference.ml.azure.com"
TOKEN="mVHiH89aX9KtWvartgwXG5V1fmCAjYEy"
MODEL="/var/azureml-app/azureml-models/mistralai-Mixtral-8x7B-Instruct-v01/5/mlflow_model_folder/data/model"
CHAT_COMPLETIONS_URL_EXTN = "/v1/chat/completions"
url = ENDPOINT_URL + CHAT_COMPLETIONS_URL_EXTN
headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ TOKEN), 'azureml-model-deployment': DEPLOYMENT_NAME }
from promptflow import tool


# The inputs section will change based on the arguments of the tool function, after you save the code
# Adding type to arguments and return value will help the system show the types properly
# Please update the function name/signature per need
@tool
def my_python_tool(question: str,prompt_text: str) -> str:
    body = { 
	"model": MODEL,
    	"messages" : [
		{
			"role": "user",
			"content": question
		},
        {
            "role": "assistant", 
            "content": prompt_text
        }
    	],
    	"max_tokens": 200,
    	"stream": False
	}
    response = requests.post(url=url, json=body, headers=headers)
    #print(prompt_text)
    return response.json()['choices'][0]['message']['content']

