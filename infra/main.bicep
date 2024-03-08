targetScope = 'subscription'


@minLength(1)
@maxLength(64)
@description('Name of the the environment which is used to generate a short unique hash used in all resources.')
param environmentName string

param resourceGroupName string = 'contoso-chats-${environmentName}-rg'

var resourceToken = toLower(uniqueString(subscription().id, environmentName, location))

param aiHubName string = 'contoso-chat-ai'
param aiServicesName string = 'aiservices-contoso-chat'
param aiProjectName string = 'aiproj-contoso-chat'
param appInsightName string = 'apws-contoso-chat'
param cosmosDBName string = 'cosmos-contoso-chat'
param keyVaultName string = 'kvcontosochat'
param aiSearchName string = 'search-contoso-chat'

// Necessary for GPT-4
@minLength(1)
@description('Primary location for all resources')
param location string

@description('Location for the OpenAI resource group')
@allowed(['canadaeast', 'eastus', 'eastus2', 'francecentral', 'switzerlandnorth', 'uksouth', 'japaneast', 'northcentralus', 'australiaeast', 'swedencentral'])
@metadata({
  azd: {
    type: 'location'
  }
})
param openAiResourceLocation string
param openAiSkuName string = 'S0'

param searchServiceLocation string

var openaiSubdomain = '${aiServicesName}${resourceToken}'
var openaiEndpoint = 'https://${openaiSubdomain}.openai.azure.com/'

var tags = { 'azd-env-name': environmentName }
// Organize resources in a resource group
resource resourceGroup 'Microsoft.Resources/resourceGroups@2021-04-01' = {
  name: !empty(resourceGroupName) ? resourceGroupName : '${environmentName}-rg'
  location: location
  tags: tags
}

var deployments = [
  {
    name: 'gpt-35-turbo'
    model: {
      format: 'OpenAI'
      name: 'gpt-35-turbo'
      version: '0613'
    }
    sku: {
      name: 'Standard'
      capacity: 120
    }
  }
  {
    name: 'gpt-4'
    model: {
      format: 'OpenAI'
      name: 'gpt-4'
      version: '0613'
    }
    sku: {
      name: 'Standard'
      capacity: 10
    }
  }
  {
    name: 'text-embedding-ada-002'
    model: {
      format: 'OpenAI'
      name: 'text-embedding-ada-002'
      version: '2'
    }
    sku: {
      name: 'Standard'
      capacity: 120
    }
  }
]

module openAi 'core/ai/cognitiveservices.bicep' =  {
  name: 'openai'
  scope: resourceGroup
  params: {
    name: 'oai-contoso${resourceToken}'
    location: openAiResourceLocation
    customSubDomainName: openaiSubdomain
    tags: tags
    sku: {
      name: openAiSkuName
    }
    deployments: deployments
  }
}

module acr './core/acr/acr.bicep' = {
  name: 'acr'
  scope: resourceGroup
  params: {
    location: location
    name: 'acrcontoso${resourceToken}'
    tags: tags
  }
}

module cosmosDb './core/cosmos/cosmos.bicep' = {
  scope: resourceGroup
  name: 'CosmosDB'
  params: {
    name: '${cosmosDBName}${resourceToken}'
    location: location
    tags: tags
  }
}

module kv 'core/kv/kv.bicep' = {
  scope: resourceGroup
  name: 'Keyvault'
  params: {
    name: substring('${keyVaultName}${resourceToken}',0,24)
    location: location
    tags: tags
  }
}


module law 'core/law/law.bicep' = {
  scope: resourceGroup
  name: 'logAnalyticsWorkspace'
  params: {
    name: 'law-${resourceToken}'
    location: location
    tags: tags
  }
}

module appInsight 'core/appinsight/appinsight.bicep' = {
  scope: resourceGroup
  name: 'appInsight'
  params: {
    logAnalyticsWsId: law.outputs.lawId
    name: '${appInsightName}${resourceToken}'
    location: location
    tags: tags
  }
}


module aiSearch 'core/aisearch/aisearch.bicep' = {
  scope: resourceGroup
  name: 'aisearch'
  params: {
    name: '${aiSearchName}${resourceToken}'
    location: searchServiceLocation
    tags : tags
  }
}


module storageAccount 'core/storage/storage.bicep' = {
  scope: resourceGroup
  name: 'StorageAccount'
  params: {
    name: 'stcontoso${resourceToken}'
    location: location
    tags: tags
  }
}





// In ai.azure.com: Azure AI Resource

module aiHub 'core/aihub/aihub.bicep' = {
  scope: resourceGroup
  name: 'aiHub'
  params: {
    name: aiHubName
    location: location
    aiSearchId: aiSearch.outputs.searchId
    appinsightsId: appInsight.outputs.appinsightsId
    containerRegistryId: acr.outputs.acrId
    keyvaultId: kv.outputs.keyvaultId
    openaiEndpoint: openaiEndpoint
    openaiId: openAi.outputs.id
    storageId: storageAccount.outputs.storageId 
    tags: tags
    aiSearchName: aiSearch.outputs.searchName
  }
}

// In ai.azure.com: Azure AI Project

module aiProject 'core/aiproject/aiproject.bicep' = {
  scope: resourceGroup
  name: 'aiProject'
  params: {
    name: aiProjectName
    location: location
    aiHubId: aiHub.outputs.mlHubId
    cosmosDocEP: cosmosDb.outputs.cosmosDocEP
    cosmosId: cosmosDb.outputs.cosmosId
    tags: tags
  }
}

// output the names of the resources
output resourceGroupName string = resourceGroup.name
output openai_name string = openAi.outputs.name
output cosmos_name string = cosmosDb.outputs.name
output search_name string = aiSearch.outputs.searchName
output mlhub_name string = aiHub.outputs.mlHubName
output mlproject_name string = aiProject.outputs.mlProjectName

output CONTOSO_AI_SERVICES_ENDPOINT string = openaiEndpoint
output COSMOS_ENDPOINT string = cosmosDb.outputs.cosmosDocEP
output CONTOSO_SEARCH_ENDPOINT string = 'https://${aiSearch.name}.search.windows.net/'

