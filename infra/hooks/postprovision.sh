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
azd env set AZURE_SEARCH_KEY $searchKey
azd env set AZURE_OPENAI_KEY $apiKey
azd env set COSMOS_KEY $cosmosKey

# Output environment variables to .env file using azd env get-values
azd env get-values > .env

# NN: Re-added this to support local development notebooks & workshop
# Create config.json with the environment variable values
echo "{\"subscription_id\": \"$subscriptionId\", \"resource_group\": \"$resourceGroupName\", \"workspace_name\": \"$mlProjectName\"}" > config.json

echo "Script execution completed successfully."

echo 'Installing dependencies from "requirements.txt"'
python -m pip install -r requirements.txt

# Install ipythong and ipykernel
python -m pip install ipython ipykernel

# Configure the IPython kernel
ipython kernel install --name=python3 --user

# Verify kernelspec list isn't empty
jupyter kernelspec list

# Run juypter notebooks
jupyter nbconvert --execute --to python --ExecutePreprocessor.timeout=-1 evaluations/evaluate-chat-flow-sdk.ipynb

jupyter nbconvert --execute --to python --ExecutePreprocessor.timeout=-1 evaluations/evaluate-chat-flow-custom-no-sdk.ipynb

jupyter nbconvert --execute --to python --ExecutePreprocessor.timeout=-1 evaluations/evaluate-chat-flow-custom.ipynb
