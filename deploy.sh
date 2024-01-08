resourceGroupName="contchat-rg"

# az account set --subscription "ca-pamelafox-demo-test"
az group create --name $resourceGroupName --location "swedencentral"

az deployment group create \
    --resource-group $resourceGroupName \
    --name contchat \
    --template-file infra/main.bicep

openAiService=$(az deployment group show --name contchat --resource-group $resourceGroupName --query properties.outputs.openai_name.value -o tsv)
searchService=$(az deployment group show --name contchat --resource-group $resourceGroupName --query properties.outputs.search_name.value -o tsv)
cosmosService=$(az deployment group show --name contchat --resource-group $resourceGroupName --query properties.outputs.cosmos_name.value -o tsv)
openAiEndpoint=$(az deployment group show --name contchat --resource-group $resourceGroupName --query properties.outputs.openai_endpoint.value -o tsv)
cosmosEndpoint=$(az deployment group show --name contchat --resource-group $resourceGroupName --query properties.outputs.cosmos_endpoint.value -o tsv)

# Write to .env file
echo "CONTOSO_SEARCH_SERVICE=$searchService" >> .env
echo "CONTOSO_AI_SERVICES_ENDPOINT=$openAiEndpoint" >> .env
echo "COSMOS_ENDPOINT=$cosmosEndpoint" >> .env

# Get the current user's object ID
objectId=$(az ad signed-in-user show --query id -o tsv)
subscriptionId=$(az account show --query id -o tsv)

# Assign the role
az role assignment create --assignee-object-id $objectId --assignee-principal-type User --role "7ca78c08-252a-4471-8644-bb5ff32d4ba0" --scope /subscriptions/"$subscriptionId"/resourceGroups/"$resourceGroupName"

# get search key
searchKey=$(az search admin-key show --service-name $searchService --resource-group $resourceGroupName --query primaryKey --output tsv)
echo "CONTOSO_SEARCH_KEY=$searchKey" >> .env

apiKey=$(az cognitiveservices account keys list --name $openAiService --resource-group $resourceGroupName --query key1 --output tsv)
echo "CONTOSO_AI_SERVICES_KEY=$apiKey" >> .env

cosmosKey=$(az cosmosdb keys list --name $cosmosService --resource-group $resourceGroupName --query primaryMasterKey --output tsv)
echo "COSMOS_KEY=$cosmosKey" >> .env
