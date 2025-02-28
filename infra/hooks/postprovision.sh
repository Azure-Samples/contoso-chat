#!/bin/bash

echo "--- ☑️ Starting postprovisioning ---"

# -----------------------------------------------------------
# Retrieve service names, resource group name, and other values from environment variables
resourceGroupName=$AZURE_RESOURCE_GROUP
searchService=$AZURE_SEARCH_NAME
openAiService=$AZURE_OPENAI_NAME
cosmosService=$AZURE_COSMOS_NAME
subscriptionId=$AZURE_SUBSCRIPTION_ID

# Ensure all required environment variables are set
if [ -z "$resourceGroupName" ] || [ -z "$searchService" ] || [ -z "$openAiService" ] || [ -z "$cosmosService" ] || [ -z "$subscriptionId" ]; then
    echo "One or more required environment variables are not set."
    echo "Ensure that AZURE_RESOURCE_GROUP, AZURE_SEARCH_NAME, AZURE_OPENAI_NAME, AZURE_COSMOS_NAME, AZURE_SUBSCRIPTION_ID are set."
    exit 1
fi

# Output environment variables to .env file using azd env get-values
azd env get-values >.env
echo "--- ✅ 2. Set environment variables ---"



echo "--- ✅ Completed postprovisioning ---"
# -----------------------------------------------------------