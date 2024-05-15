using './main.bicep'

param environmentName = readEnvironmentVariable('AZURE_ENV_NAME', 'MY_ENV')

param location = readEnvironmentVariable('AZURE_LOCATION', 'eastus2')

param principalId = readEnvironmentVariable('AZURE_PRINCIPAL_ID', '')
param principalType = readEnvironmentVariable('AZURE_PRINCIPAL_TYPE', 'User')

param aiHubName = readEnvironmentVariable('AZUREAI_HUB_NAME', '')
param aiProjectName = readEnvironmentVariable('AZUREAI_PROJECT_NAME', '')
param endpointName = readEnvironmentVariable('AZURE_ENDPOINT_NAME', '')

param openAiName = readEnvironmentVariable('AZURE_OPENAI_NAME', '')
param searchServiceName = readEnvironmentVariable('AZURE_SEARCH_NAME', '')
