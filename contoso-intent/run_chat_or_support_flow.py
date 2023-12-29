from promptflow import tool
from promptflow.connections import AzureOpenAIConnection
import os, openai
from jinja2 import Template
import urllib.request
import json
import ssl



def get_intent(question: str, azure_open_ai_connection: AzureOpenAIConnection, open_ai_deployment: str) -> str:
    """
    get intent of question
    """
    aoai_client = openai.AzureOpenAI(
    api_key = azure_open_ai_connection.api_key,  
    api_version = azure_open_ai_connection.api_version,
    azure_endpoint = azure_open_ai_connection.api_base 
    )
    jinja_template = os.path.join(os.path.dirname(__file__), "intent.jinja2")
    with open(jinja_template, encoding="utf-8") as f:
        template = Template(f.read())
    prompt = template.render(question=question)
    messages = [
        {
            "role": "system",
            "content": prompt,
        }
    ]
    chat_intent_completion = aoai_client.chat.completions.create(
        model=open_ai_deployment,
        messages=messages,
        temperature=0,
        max_tokens=1024,
        n=1,
    )
    user_intent = chat_intent_completion.choices[0].message.content
    # if string contains chat, return chat
    if "chat" in user_intent:
        return "chat"
    # if string contains support, return support
    elif "support" in user_intent:
        return "support"
    # else return chat
    else:
        return "chat"

def run_chat_flow(question: str, customer_id: str, chat_history: []) -> str:
    """
    run chat flow based on the question and customer id
    """
    # call chat endpoint and return response (input is question and customer id in json format)
    # TODO: Update these to secrets
    url = ''
    key = ''
    input_data = {"question": question, "customer_id": customer_id, "chat_history": chat_history}
    response = call_endpoint(url, key, input_data)
    return response

def run_support_flow(question: str, customer_id: str, chat_history: []) -> str:
    """
    run support flow based on the question and customer id
    """
    # call support endpoint and return response (input is question and customer id in json format)
    # TODO: Update these to secrets
    url = ''
    key = ''
    input_data = {"question": question, "customer_id": customer_id, "chat_history": chat_history}
    response = call_endpoint(url, key, input_data)
    return response
  

def allowSelfSignedHttps(allowed):
# bypass the server certificate verification on client side
    if allowed and not os.environ.get('PYTHONHTTPSVERIFY', '') and getattr(ssl, '_create_unverified_context', None):
        ssl._create_default_https_context = ssl._create_unverified_context
def call_endpoint(url, key, input_data):
    # Allow self-signed certificate
    allowSelfSignedHttps(True) # this line is needed if you use self-signed certificate in your scoring service.
    # Request data goes here
    # The example below assumes JSON formatting which may be updated
    # depending on the format your endpoint expects.
    # More information can be found here:
    # https://docs.microsoft.com/azure/machine-learning/how-to-deploy-advanced-entry-script
    data = input_data
    body = str.encode(json.dumps(data))
    url = url
    # Replace this with the primary/secondary key or AMLToken for the endpoint
    api_key = key
    if not api_key:
        raise Exception("A key should be provided to invoke the endpoint")
    # The azureml-model-deployment header will force the request to go to a specific deployment.
    # Remove this header to have the request observe the endpoint traffic rules
    headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_key), 'azureml-model-deployment': 'contoso-support' }
    req = urllib.request.Request(url, body, headers)
    try:
        response = urllib.request.urlopen(req)
        result = response.read()
        print(result)
        return result.decode("utf8", 'ignore')
    except urllib.error.HTTPError as error:
        print("The request failed with status code: " + str(error.code))
        # Print the headers - they include the requert ID and the timestamp, which are useful for debugging the failure
        print(error.info())
        print(error.read().decode("utf8", 'ignore'))
            # call support endpoint and return response (input is question and customer id in json format)
        return error.read().decode("utf8", 'ignore')
    # Get Intent of question

@tool
def run_chat_or_support_flow(
    question: str,
    chat_history: list[str],
    customer_id: str,
    azure_open_ai_connection: AzureOpenAIConnection,
    open_ai_deployment: str
) -> str:
    """
    run chat or support flow based on the intent
    """
    user_intent = get_intent(question, azure_open_ai_connection, open_ai_deployment)

    if user_intent == "chat":
        # call chat endpoint and return response (input is question and customer id in json format)
        return run_chat_flow(question, customer_id, chat_history)

    elif user_intent == "support":
        # call support endpoint and return response (input is question and customer id in json format)
        return run_support_flow(question, customer_id, chat_history)