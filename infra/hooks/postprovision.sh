#!/bin/sh

# Check if running in GitHub Workspace
if [ -z "$GITHUB_WORKSPACE" ]; then
    # The GITHUB_WORKSPACE is not set, meaning this is not running in a GitHub Action
    DIR=$(dirname "$(realpath "$0")")
    "$DIR/login.sh"
fi

# Retrieve service names, resource group name, and other values from environment variables
resourceGroupName=$AZURE_RESOURCE_GROUP
searchService=$AZURE_SEARCH_NAME
openAiService=$AZURE_OPENAI_NAME
cosmosService=$AZURE_COSMOS_NAME
subscriptionId=$AZURE_SUBSCRIPTION_ID
mlProjectName=$AZUREAI_PROJECT_NAME

# Ensure all required environment variables are set
if [ -z "$resourceGroupName" ] || [ -z "$searchService" ] || [ -z "$openAiService" ] || [ -z "$cosmosService" ] || [ -z "$subscriptionId" ] || [ -z "$mlProjectName" ]; then
    echo "One or more required environment variables are not set."
    echo "Ensure that AZURE_RESOURCE_GROUP, AZURE_SEARCH_NAME, AZURE_OPENAI_NAME, AZURE_COSMOS_NAME, AZURE_SUBSCRIPTION_ID, and AZUREAI_PROJECT_NAME are set."
    exit 1
fi

# Retrieve the keys
searchKey=$(az search admin-key show --service-name $searchService --resource-group $resourceGroupName --query primaryKey --output tsv)
apiKey=$(az cognitiveservices account keys list --name $openAiService --resource-group $resourceGroupName --query key1 --output tsv)
cosmosKey=$(az cosmosdb keys list --name $cosmosService --resource-group $resourceGroupName --query primaryMasterKey --output tsv)

# Set the environment variables using azd env set
# TODO: Remove these once we have MI integration
azd env set AZURE_SEARCH_KEY $searchKey
azd env set AZURE_OPENAI_KEY $apiKey
azd env set COSMOS_KEY $cosmosKey

# Set additional environment variables expected by app 
# TODO: Standardize these and remove need for setting here
azd env set AZURE_OPENAI_API_VERSION 2023-03-15-preview
azd env set AZURE_OPENAI_CHAT_DEPLOYMENT gpt-35-turbo
azd env set CONTOSO_SEARCH_ENDPOINT $AZURE_SEARCH_ENDPOINT
azd env set CONTOSO_SEARCH_KEY $AZURE_SEARCH_KEY 

# Output environment variables to .env file using azd env get-values
azd env get-values > .env

# Create config.json with required Azure AI project config information
echo "{\"subscription_id\": \"$subscriptionId\", \"resource_group\": \"$resourceGroupName\", \"workspace_name\": \"$mlProjectName\"}" > config.json

echo "--- ✅ | 1. Post-provisioning - env configured ---"

# Setup to run notebooks
echo 'Installing dependencies from "requirements.txt"'
python -m pip install -r requirements.txt
python -m pip install ipython ipykernel      # Install ipython and ipykernel
ipython kernel install --name=python3 --user # Configure the IPython kernel
jupyter kernelspec list                      # Verify kernelspec list isn't empty
echo "--- ✅ | 2. Post-provisioning - ready execute notebooks ---"

echo "Populating data ...."
jupyter nbconvert --execute --to python --ExecutePreprocessor.timeout=-1 data/customer_info/create-cosmos-db.ipynb
jupyter nbconvert --execute --to python --ExecutePreprocessor.timeout=-1 data/product_info/create-azure-search.ipynb
echo "--- ✅ | 3. Post-provisioning - populated data ---"

echo "Running evaluations ...."
jupyter nbconvert --execute --to python --ExecutePreprocessor.timeout=-1 evaluations/evaluate-chat-flow-sdk.ipynb
jupyter nbconvert --execute --to python --ExecutePreprocessor.timeout=-1 evaluations/evaluate-chat-flow-custom-no-sdk.ipynb
jupyter nbconvert --execute --to python --ExecutePreprocessor.timeout=-1 evaluations/evaluate-chat-flow-custom.ipynb
echo "--- ✅ | 4. Post-provisioning - ran evaluations ---"
