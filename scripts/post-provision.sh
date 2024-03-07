 #!/bin/sh

echo "Loading azd .env file from current environment..."

while IFS='=' read -r key value; do
    value=$(echo "$value" | sed 's/^"//' | sed 's/"$//')
    export "$key=$value"
done <<EOF
$(azd env get-values)
EOF

if [ -z "$(az account show)" ]; then
    echo "You are not logged in. Please run 'az login' or 'az login --use-device-code' first."
    exit 1
fi

echo "Setting up environment variables in .env file..."
# Save output values to variables
openAiService=$openai_name
searchService=$search_name
cosmosService=$cosmos_name

# Get keys from services
searchKey=$(az search admin-key show --service-name $searchService --resource-group $resourceGroupName --query primaryKey --output tsv)
apiKey=$(az cognitiveservices account keys list --name $openAiService --resource-group $resourceGroupName --query key1 --output tsv)
cosmosKey=$(az cosmosdb keys list --name $cosmosService --resource-group $resourceGroupName --query primaryMasterKey --output tsv)

echo  > .env
echo "CONTOSO_SEARCH_ENDPOINT=$CONTOSO_SEARCH_ENDPOINT" >> .env
echo "CONTOSO_AI_SERVICES_ENDPOINT=$CONTOSO_AI_SERVICES_ENDPOINT" >> .env
echo "COSMOS_ENDPOINT=$COSMOS_ENDPOINT" >> .env
echo "CONTOSO_SEARCH_KEY=$searchKey" >> .env
echo "CONTOSO_AI_SERVICES_KEY=$apiKey" >> .env
echo "COSMOS_KEY=$cosmosKey" >> .env



echo "Writing config.json file for PromptFlow usage..."
subscriptionId=$(az account show --query id -o tsv)
echo "{\"subscription_id\": \"$subscriptionId\", \"resource_group\": \"$resourceGroupName\", \"workspace_name\": \"$mlProjectName\"}" > config.json
    
echo "Setting .env and config.json file complete!"