# get config.json
echo "Writing config.json file for PromptFlow usage..."
subscriptionId=$(az account show --query id -o tsv)
resourceGroupName=$(az group show --name $resourceGroupName --query name -o tsv)
mlProjectName=$(az deployment group show --name contchat --resource-group $resourceGroupName --query properties.outputs.mlproject_name.value -o tsv)

# create a random hash for the endpoint name all lowercase letters
endpointName="contoso-chat-$RANDOM"
# create a random hash for the deployment name
deploymentName="contoso-chat-$RANDOM"

echo "{\"subscription_id\": \"$subscriptionId\", \"resource_group\": \"$resourceGroupName\", \"workspace_name\": \"$mlProjectName\"}" > config.json
$(cat principal.txt) --secret-permissions get list

# register promptflow as model
echo "Registering PromptFlow as a model in Azure ML..."
az extension add -n ml -y
az ml model create --file deployment/chat-model.yaml  -g $resourceGroupName -w $mlProjectName

# Deploy prompt flow
echo "Deploying PromptFlow to Azure ML..."
az ml online-endpoint create --file deployment/chat-endpoint.yaml -n $endpointName -g $resourceGroupName -w $mlProjectName

# Setup deployment
echo "Setting up deployment..."
az ml online-deployment create --file deployment/chat-deployment.yaml --name $deploymentName --endpoint-name $endpointName --all-traffic -g $resourceGroupName -w $mlProjectName
az ml online-endpoint show -n $endpointName -g $resourceGroupName -w $mlProjectName
az ml online-deployment get-logs --name $deploymentName --endpoint-name $endpointName -g $resourceGroupName -w $mlProjectName

# Read endpoint principal
echo "Reading endpoint principal..."
az ml online-endpoint show -n $endpointName -g $resourceGroupName -w $mlProjectName > endpoint.json
jq -r '.identity.principal_id' endpoint.json > principal.txt
echo "Principal is: $(cat principal.txt)"

#Assign Permission to Endpoint Principal
echo "Assigning permissions to Principal..."
az role assignment create --assignee $(cat principal.txt) --role "AzureML Data Scientist" --scope "/subscriptions/$subscription_id/resourcegroups/$resourceGroupName/providers/Microsoft.MachineLearningServices/workspaces/$mlProjectName"
az role assignment create --assignee $(cat principal.txt) --role "Azure Machine Learning Workspace Connection Secrets Reader" --scope "/subscriptions/$subscription_id/resourcegroups/$resourceGroupName/providers/Microsoft.MachineLearningServices/workspaces/$mlProjectName/onlineEndpoints/$endpointName"
# Get keyValueName from Azure ML
keyValueName=$(az ml online-endpoint show -n $endpointName -g $resourceGroupName -w $mlProjectName --query "identity.principal_id" -o tsv)          
echo "assigning permissions to Principal to Key vault.."
az keyvault set-policy --name $keyValueName --resource-group $resourceGroupName --object-id 