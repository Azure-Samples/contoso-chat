#!/bin/sh

# Check if the Azure CLI is authenticated
EXPIRED_TOKEN=$(az ad signed-in-user show --query 'id' -o tsv 2>/dev/null || true)

if [ -z "$EXPIRED_TOKEN" ]; then
    echo "No Azure user signed in. Please login."
    az login -o none
fi

# Check if Azure Subscription ID is set
if [ -z "${AZURE_SUBSCRIPTION_ID:-}" ]; then
    ACCOUNT=$(az account show --query '[id,name]')
    echo "You can set the \`AZURE_SUBSCRIPTION_ID\` environment variable with \`azd env set AZURE_SUBSCRIPTION_ID\`."
    echo "$ACCOUNT"
    
    echo "Do you want to use the above subscription? (Y/n) "
    read response
    response=${response:-Y}
    case "$response" in
        [yY][eE][sS]|[yY])
            ;;
        *)
            echo "Listing available subscriptions..."
            SUBSCRIPTIONS=$(az account list --query 'sort_by([], &name)' --output json)
            echo "Available subscriptions:"
            echo "$SUBSCRIPTIONS" | jq -r '.[] | [.name, .id] | @tsv' | column -t -s $'\t'
            echo "Enter the name or ID of the subscription you want to use: "
            read subscription_input
            AZURE_SUBSCRIPTION_ID=$(echo "$SUBSCRIPTIONS" | jq -r --arg input "$subscription_input" '.[] | select(.name==$input or .id==$input) | .id')
            if [ -n "$AZURE_SUBSCRIPTION_ID" ]; then
                echo "Setting active subscription to: $AZURE_SUBSCRIPTION_ID"
                az account set -s $AZURE_SUBSCRIPTION_ID
            else
                echo "Subscription not found. Please enter a valid subscription name or ID."
                exit 1
            fi
            ;;
    esac
else
    az account set -s $AZURE_SUBSCRIPTION_ID
fi

# Retrieve service names, resource group name, and other values from environment variables
resourceGroupName=$AZURE_RESOURCE_GROUP
searchService=$search_name
openAiService=$openai_name
cosmosService=$cosmos_name
subscriptionId=$AZURE_SUBSCRIPTION_ID
mlProjectName=$mlproject_name

# Ensure all required environment variables are set
if [ -z "$resourceGroupName" ] || [ -z "$searchService" ] || [ -z "$openAiService" ] || [ -z "$cosmosService" ] || [ -z "$subscriptionId" ] || [ -z "$mlProjectName" ]; then
    echo "One or more required environment variables are not set."
    echo "Ensure that AZURE_RESOURCE_GROUP, search_name, openai_name, cosmos_name, AZURE_SUBSCRIPTION_ID, and mlproject_name are set."
    exit 1
fi

# Retrieve the keys
searchKey=$(az search admin-key show --service-name $searchService --resource-group $resourceGroupName --query primaryKey --output tsv)
apiKey=$(az cognitiveservices account keys list --name $openAiService --resource-group $resourceGroupName --query key1 --output tsv)
cosmosKey=$(az cosmosdb keys list --name $cosmosService --resource-group $resourceGroupName --query primaryMasterKey --output tsv)

# Set the environment variables using azd env set
azd env set CONTOSO_SEARCH_KEY $searchKey
azd env set CONTOSO_AI_SERVICES_KEY $apiKey
azd env set COSMOS_KEY $cosmosKey

# Create config.json with the environment variable values
echo "{\"subscription_id\": \"$subscriptionId\", \"resource_group\": \"$resourceGroupName\", \"workspace_name\": \"$mlProjectName\"}" > config.json

# Output environment variables to .env file using azd env get-values
azd env get-values > .env

echo "Script execution completed successfully."
