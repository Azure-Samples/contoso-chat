from promptflow import PFClient
from promptflow.azure import PFClient as PFClientAzure
import datetime

def run_local_flow(flow: str, inputs: dict, pf_client: PFClient)->dict:
    print("running local flow")
    print({"flow": flow, "inputs": inputs})
    output = pf_client.test(
        flow=flow, # Path to the flow directory
        inputs=inputs,
    )
    return output

def run_azure_flow(runtime: str, flow: str, run_name: str, data: str, column_mapping: dict, pf_client_azure: PFClientAzure)->dict:
    # # AI Studio Azure batch run on an evaluation json dataset  
    
    now = datetime.datetime.now()
    timestamp = now.strftime("%m_%d_%H%M")
    run_name = str(run_name + "_" + timestamp)
    # create base run in Azure Ai Studio
    base_run = pf_client_azure.run(
        flow=flow,
        data=data,
        column_mapping=column_mapping,
        runtime=runtime,
        display_name=run_name,
        name=run_name,
    )
    return base_run



def run_azure_eval_flow(runtime: str, eval_flow: str, run_name: str, data: str, column_mapping: dict, base_run, pf_client_azure: PFClientAzure)->dict:
    # # AI Studio Azure batch run on an evaluation json dataset  
    
    now = datetime.datetime.now()
    timestamp = now.strftime("%m_%d_%H%M")
    run_name = str(run_name + "_" + timestamp)
    # create base run in Azure Ai Studio
    eval_run_variant = pf_client_azure.run(
        flow=eval_flow,
        data=data,  # path to the data file
        run=base_run,  # use run as the variant
        column_mapping=column_mapping,
        runtime=runtime,
        display_name=run_name,
        name=run_name
    )

    return eval_run_variant
