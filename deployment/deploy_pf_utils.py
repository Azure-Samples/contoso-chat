# import required libraries
import os
from azure.ai.ml import MLClient
from azure.ai.ml.entities import WorkspaceConnection
# Import required libraries
from azure.identity import DefaultAzureCredential, InteractiveBrowserCredential

# Import required libraries
from azure.identity import DefaultAzureCredential, InteractiveBrowserCredential

def push_pf(flow_path, pf_name_suffix, type):

    try:
        credential = DefaultAzureCredential()
        # Check if given credential can get token successfully.
        credential.get_token("https://management.azure.com/.default")
    except Exception as ex:
        # Fall back to InteractiveBrowserCredential in case DefaultAzureCredential not work
        credential = InteractiveBrowserCredential()

    config_path = "../config.json"
    from promptflow.azure import PFClient
    pf_azure_client = PFClient.from_config(credential=credential, path=config_path)

    # Create unique name for pf name with date time
    import datetime
    now = datetime.datetime.now()
    pf_name = "{}-{}".format(pf_name_suffix, now.strftime("%Y-%m-%d-%H-%M-%S"))

    print("Creating prompt flow {} to {} ({})".format(flow_path, pf_name, type))

    # Runtime no longer needed (not in flow schema)
    flow = pf_azure_client.flows.create_or_update(
        flow=flow_path,
        display_name=pf_name,
        type=type)
    print("Created prompt flow", pf_name)
