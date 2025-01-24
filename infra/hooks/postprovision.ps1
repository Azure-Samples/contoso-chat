#!/usr/bin/env pwsh

Write-Host "Starting postprovisioning..."

# Retrieve service names, resource group name, and other values from environment variables
$resourceGroupName = $env:AZURE_RESOURCE_GROUP
Write-Host "resourceGroupName: $resourceGroupName"

$openAiService = $env:AZURE_OPENAI_NAME
Write-Host "openAiService: $openAiService"

$subscriptionId = $env:AZURE_SUBSCRIPTION_ID
Write-Host "subscriptionId: $subscriptionId"

$cosmosService = $env:AZURE_COSMOS_NAME
Write-Host "cosmosServiceName: $cosmosService"

$cosmosServiceEndpoint = $env:COSMOS_ENDPOINT
Write-Host "cosmosServiceEndpoint: $cosmosServiceEndpoint"

$azureSearchEndpoint = $env:AZURE_SEARCH_ENDPOINT
Write-Host "azureSearchEndpoint: $azureSearchEndpoint"

# Ensure all required environment variables are set
if ([string]::IsNullOrEmpty($resourceGroupName) -or [string]::IsNullOrEmpty($openAiService) -or [string]::IsNullOrEmpty($subscriptionId)) {
    Write-Host "One or more required environment variables are not set."
    Write-Host "Ensure that AZURE_RESOURCE_GROUP, AZURE_OPENAI_NAME, AZURE_SUBSCRIPTION_ID are set."
    exit 1
}

# Ensure all required environment variables are set
if ([string]::IsNullOrEmpty($cosmosService) -or [string]::IsNullOrEmpty($cosmosServiceEndpoint) -or [string]::IsNullOrEmpty($azureSearchEndpoint)) {
    Write-Host "One or more required environment variables are not set."
    Write-Host "Ensure that AZURE_COSMOS_NAME, COSMOS_ENDPOINT, AZURE_SEARCH_ENDPOINT are set."
    exit 1
}

# Set additional environment variables expected by app 
# TODO: Standardize these and remove need for setting here
azd env set AZURE_OPENAI_API_VERSION 2024-08-01-preview
azd env set AZURE_OPENAI_CHAT_DEPLOYMENT gpt-4o-mini
azd env set AZURE_SEARCH_ENDPOINT $AZURE_SEARCH_ENDPOINT

# Output environment variables to .env file using azd env get-values
azd env get-values > .env
#Write-Host "Script execution completed successfully."
Write-Host  "--- ✳️ | 1. Post-provisioning - env configured ---"

Write-Host 'Installing dependencies from "requirements.txt"'
python -m pip install -r ./src/api/requirements.txt > $null
Write-Host  "--- ✳️ | 2. Post-provisioning - dependencies installed ---"

# populate data
Write-Host "Populating data ...."
jupyter nbconvert --execute --to python --ExecutePreprocessor.timeout=-1 data/customer_info/create-cosmos-db.ipynb > $null
jupyter nbconvert --execute --to python --ExecutePreprocessor.timeout=-1 data/product_info/create-azure-search.ipynb > $null
Write-Host  "--- ✳️ | 3. Post-provisioning - populated data ---"
