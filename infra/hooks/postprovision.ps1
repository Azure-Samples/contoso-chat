#!/usr/bin/env pwsh

Write-Host "--- ☑️ 1. Starting postprovisioning ---"

# -----------------------------------------------------------
# Retrieve service names, resource group name, and other values from environment variables

# Retrieve service names, resource group name, and other values from environment variables
$resourceGroupName = $env:AZURE_RESOURCE_GROUP
Write-Host "resourceGroupName: $resourceGroupName"

$openAiService = $env:AZURE_OPENAI_NAME
Write-Host "openAiService: $openAiService"

$subscriptionId = $env:AZURE_SUBSCRIPTION_ID
Write-Host "subscriptionId: $subscriptionId"

$cosmosService = $env:AZURE_COSMOS_NAME
Write-Host "cosmosServiceName: $cosmosService"

$cosmosService = $env:COSMOS_ENDPOINT
Write-Host "cosmosServiceEndpoint: $cosmosService"

$azureSearchEndpoint = $env:AZURE_SEARCH_ENDPOINT
Write-Host "azureSearchEndpoint: $azureSearchEndpoint"

# Ensure all required environment variables are set
if ([string]::IsNullOrEmpty($resourceGroupName) -or [string]::IsNullOrEmpty($openAiService) -or [string]::IsNullOrEmpty($subscriptionId)) {
    Write-Host "🅇 One or more required environment variables are not set."
    Write-Host "Ensure that AZURE_RESOURCE_GROUP, AZURE_OPENAI_NAME, AZURE_SUBSCRIPTION_ID are set."
    exit 1
}

# Output environment variables to .env file using azd env get-values
azd env get-values > .env
#Write-Host "--- ✅ 2. Set environment variables ---"

# -----------------------------------------------------------
# Setup to run notebooks
#python -m pip install -r ./src/api/requirements.txt > $null
#Write-Host "---- ✅ 3. Installed required dependencies ---"

# -----------------------------------------------------------
# Run notebooks to populate data
#jupyter nbconvert --execute --to python --ExecutePreprocessor.timeout=-1 data/customer_info/create-cosmos-db.ipynb > $null
#jupyter nbconvert --execute --to python --ExecutePreprocessor.timeout=-1 data/product_info/create-azure-search.ipynb > $null
#Write-Host "---- ✅ 4. Completed populating data ---"

Write-Host "--- ✅ Completed postprovisioning ---"