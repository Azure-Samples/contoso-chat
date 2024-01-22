from promptflow import tool
from promptflow.connections import CustomConnection
import os
import urllib.request
import json
import ssl


def allowSelfSignedHttps(allowed):
# bypass the server certificate verification on client side
    if allowed and not os.environ.get('PYTHONHTTPSVERIFY', '') and getattr(ssl, '_create_unverified_context', None):
        ssl._create_default_https_context = ssl._create_unverified_context
def call_endpoint(url, api_key, input_data, model_deployment_name):
    # Allow self-signed certificate
    allowSelfSignedHttps(True) # this line is needed if you use self-signed certificate in your scoring service.
    # Request data goes here
    # The example below assumes JSON formatting which may be updated
    # depending on the format your endpoint expects.
    # More information can be found here:
    # https://docs.microsoft.com/azure/machine-learning/how-to-deploy-advanced-entry-script
    body = str.encode(json.dumps(input_data))
    # Replace this with the primary/secondary key or AMLToken for the endpoint
    if not api_key:
        raise Exception("A key should be provided to invoke the endpoint")
    # The azureml-model-deployment header will force the request to go to a specific deployment.
    # Remove this header to have the request observe the endpoint traffic rules
    headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_key), 'azureml-model-deployment': model_deployment_name }
    req = urllib.request.Request(url, body, headers)
    try:
        response = urllib.request.urlopen(req)
        result = response.read()
        # convert result to string
        result = result.decode("utf-8", 'ignore')
        # convert result to json
        resultjson = json.loads(result)
        print(resultjson)

        answer = resultjson['answer']
        context = resultjson['context']

        if(model_deployment_name ==  'contoso-support'):
            citations = resultjson['citations']
            customer_data = resultjson['customer_data']
            query_rewrite = resultjson['query_rewrite']
            return {'answer': answer, 'context': context, 'citations': citations, 'customer_data': customer_data, 'query_rewrite': query_rewrite}
        else:
            return {'answer': answer, 'context': context}
    except urllib.error.HTTPError as error:
        print("The request failed with status code: " + str(error.code))
        # Print the headers - they include the requert ID and the timestamp, which are useful for debugging the failure
        print(error.info())
        print(error.read().decode("utf8", 'ignore'))
            # call support endpoint and return response (input is question and customer id in json format)
        return error.read().decode("utf8", 'ignore')

@tool
def run_chat_or_support_flow(
    question: str,
    chat_history: list[str],
    customerId: str,
    user_intent: str,
    support_endpoint: CustomConnection,
    chat_endpoint: CustomConnection,
):
    """
    run chat or support flow based on the intent
    """

    if "support" in user_intent:
        # call chat endpoint and return response (input is question and customer id in json format)
        print("running support flow")
        url = support_endpoint['api_base']
        key = support_endpoint['api_key']

        input_data = {"question": question, "customerId": customerId, "chat_history": chat_history}
        return call_endpoint(url, key, input_data, "contoso-support-9f8e7b")
    else:
        # call support endpoint and return response (input is question and customer id in json format)
        print("running chat flow")
        url = chat_endpoint['api_base']
        key = chat_endpoint['api_key']

        input_data = {"question": question, "customerId": customerId, "chat_history": chat_history}
        return call_endpoint(url, key, input_data, "contoso-chat-b7a357")