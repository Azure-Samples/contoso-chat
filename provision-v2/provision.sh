resourceGroupName="contchat-rg"
resourceGroupLocation="swedencentral"

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
    
echo "Provisioning complete!"