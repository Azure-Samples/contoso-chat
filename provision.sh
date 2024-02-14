resourceGroupName="contchat-rg"
resourceGroupLocation="swedencentral"
endpointName="contoso-chat-store"
deploymentName="contoso-chat-ai"

if [ -z "$(az account show)" ]; then
    echo "You are not logged in. Please run 'az login' or 'az login --use-device-code' first."
    exit 1
fi

echo "Running provisioning using this subscription:"
az account show --query "{subscriptionId:id, name:name}"
echo "If that is not the correct subscription, please run 'az account set --subscription \"<SUBSCRIPTION-NAME>\"'"

echo "Creating resource group $resourceGroupName in $resourceGroupLocation..."
az group create --name $resourceGroupName --location $resourceGroupLocation > /dev/null
if [ $? -ne 0 ]; then
    echo "ERROR: Failed to create resource group, perhaps you need to set the subscription? See command above."
    exit 1
fi

echo "Provisioning resources in resource group $resourceGroupName..."
az deployment group create --resource-group $resourceGroupName --name contchat --only-show-errors --template-file infra/main.bicep > /dev/null
if [ $? -ne 0 ]; then
    echo "ERROR: Failed to provision resources. Please check the error message above."
    exit 1
fi

echo "Setting up environment variables in .env file..."
# Save output values to variables
openAiService=$(az deployment group show --name contchat --resource-group $resourceGroupName --query properties.outputs.openai_name.value -o tsv)
searchService=$(az deployment group show --name contchat --resource-group $resourceGroupName --query properties.outputs.search_name.value -o tsv)
cosmosService=$(az deployment group show --name contchat --resource-group $resourceGroupName --query properties.outputs.cosmos_name.value -o tsv)
searchEndpoint=$(az deployment group show --name contchat --resource-group $resourceGroupName --query properties.outputs.search_endpoint.value -o tsv)
openAiEndpoint=$(az deployment group show --name contchat --resource-group $resourceGroupName --query properties.outputs.openai_endpoint.value -o tsv)
cosmosEndpoint=$(az deployment group show --name contchat --resource-group $resourceGroupName --query properties.outputs.cosmos_endpoint.value -o tsv)
mlProjectName=$(az deployment group show --name contchat --resource-group $resourceGroupName --query properties.outputs.mlproject_name.value -o tsv)

# Get keys from services
searchKey=$(az search admin-key show --service-name $searchService --resource-group $resourceGroupName --query primaryKey --output tsv)
apiKey=$(az cognitiveservices account keys list --name $openAiService --resource-group $resourceGroupName --query key1 --output tsv)
cosmosKey=$(az cosmosdb keys list --name $cosmosService --resource-group $resourceGroupName --query primaryMasterKey --output tsv)

echo "CONTOSO_SEARCH_ENDPOINT=$searchEndpoint" >> .env
echo "CONTOSO_AI_SERVICES_ENDPOINT=$openAiEndpoint" >> .env
echo "COSMOS_ENDPOINT=$cosmosEndpoint" >> .env
echo "CONTOSO_SEARCH_KEY=$searchKey" >> .env
echo "CONTOSO_AI_SERVICES_KEY=$apiKey" >> .env
echo "COSMOS_KEY=$cosmosKey" >> .env

echo "Writing config.json file for PromptFlow usage..."
subscriptionId=$(az account show --query id -o tsv)
echo "{\"subscription_id\": \"$subscriptionId\", \"resource_group\": \"$resourceGroupName\", \"workspace_name\": \"$mlProjectName\"}" > config.json

# register promptflow as model
echo "Registering PromptFlow as a model in Azure ML..."
az ml model create --file deployment/chat-model.yaml  -g $resourceGroupName -w $mlProjectName

# Deploy prompt flow
echo "Deploying PromptFlow to Azure ML..."
az extension add -n ml -y
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
az keyvault set-policy --name $keyValueName --resource-group $resourceGroupName --object-id $(cat principal.txt) --secret-permissions get list
    

echo "Provisioning complete!"