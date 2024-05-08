resourceGroupName="contoso-chat-rg"
resourceGroupLocation="swedencentral"
name="contoso-chat"     #TODO: Replace with Deployment name

echo "Setting up environment variables in .env file..."
# Save output values to variables
openAiService=$(az deployment group show --name $name --resource-group $resourceGroupName --query properties.outputs.openai_name.value -o tsv)
searchService=$(az deployment group show --name $name --resource-group $resourceGroupName --query properties.outputs.search_name.value -o tsv)
cosmosService=$(az deployment group show --name $name --resource-group $resourceGroupName --query properties.outputs.cosmos_name.value -o tsv)
searchEndpoint=$(az deployment group show --name $name --resource-group $resourceGroupName --query properties.outputs.search_endpoint.value -o tsv)
openAiEndpoint=$(az deployment group show --name $name --resource-group $resourceGroupName --query properties.outputs.openai_endpoint.value -o tsv)
cosmosEndpoint=$(az deployment group show --name $name --resource-group $resourceGroupName --query properties.outputs.cosmos_endpoint.value -o tsv)
mlProjectName=$(az deployment group show --name $name --resource-group $resourceGroupName --query properties.outputs.mlproject_name.value -o tsv)

# Get keys from services
searchKey=$(az search admin-key show --service-name $searchService --resource-group $resourceGroupName --query primaryKey --output tsv)
apiKey=$(az cognitiveservices account keys list --name $openAiService --resource-group $resourceGroupName --query key1 --output tsv)
cosmosKey=$(az cosmosdb keys list --name $cosmosService --resource-group $resourceGroupName --query primaryMasterKey --output tsv)

echo "CONTOSO_SEARCH_ENDPOINT=$searchEndpoint" >> ../.env
echo "CONTOSO_AI_SERVICES_ENDPOINT=$openAiEndpoint" >> ../.env
echo "COSMOS_ENDPOINT=$cosmosEndpoint" >> ../.env
echo "CONTOSO_SEARCH_KEY=$searchKey" >> ../.env
echo "CONTOSO_AI_SERVICES_KEY=$apiKey" >> ../.env
echo "COSMOS_KEY=$cosmosKey" >> ../.env

echo "Writing config.json file for PromptFlow usage..."
subscriptionId=$(az account show --query id -o tsv)
echo "{\"subscription_id\": \"$subscriptionId\", \"resource_group\": \"$resourceGroupName\", \"workspace_name\": \"$mlProjectName\"}" > ../config.json
    
echo "Provisioning complete!"