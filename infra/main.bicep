targetScope = 'subscription'

@minLength(1)
@maxLength(64)
@description('Name which is used to generate a short unique hash for each resource')
param environmentName string

@minLength(1)
@description('Primary location for all resources')
@metadata({
  azd: {
    type: 'location'
  }
})
param location string

@description('The name of the OpenAI resource')
param openAiResourceName string = ''

@description('The name of the resource group for the OpenAI resource')
param openAiResourceGroupName string = ''

@description('Location for the OpenAI resource')
@allowed([
  'canadaeast'
  'eastus'
  'eastus2'
  'francecentral'
  'switzerlandnorth'
  'uksouth'
  'japaneast'
  'northcentralus'
  'australiaeast'
  'swedencentral'
])
@metadata({
  azd: {
    type: 'location'
  }
})
param openAiResourceLocation string

@description('The SKU name of the OpenAI resource')
param openAiSkuName string = ''

@description('The API version of the OpenAI resource')
param openAiApiVersion string = ''

@description('The type of the OpenAI resource')
param openAiType string = 'azure'

@description('The name of the search service')
param searchServiceName string = ''

@description('The name of the Cosmos account')
param cosmosAccountName string = ''

@description('The name of the OpenAI embedding deployment')
param openAiEmbeddingDeploymentName string = ''

@description('The name of the AI search index')
param aiSearchIndexName string = 'contoso-products'

@description('The name of the Cosmos database')
param cosmosDatabaseName string = 'contoso-outdoor'

@description('The name of the Cosmos container')
param cosmosContainerName string = 'customers'

@description('The name of the OpenAI deployment')
param openAiDeploymentName string = ''

@description('Id of the user or app to assign application roles')
param principalId string = ''

@description('Whether the deployment is running on GitHub Actions')
param runningOnGh string = ''

@description('Whether the deployment is running on Azure DevOps Pipeline')
param runningOnAdo string = ''

var resourceToken = toLower(uniqueString(subscription().id, environmentName, location))
var tags = { 'azd-env-name': environmentName }

resource resourceGroup 'Microsoft.Resources/resourceGroups@2021-04-01' = {
  name: 'rg-${environmentName}'
  location: location
  tags: tags
}

resource openAiResourceGroup 'Microsoft.Resources/resourceGroups@2021-04-01' existing = if (!empty(openAiResourceGroupName)) {
  name: !empty(openAiResourceGroupName) ? openAiResourceGroupName : resourceGroup.name
}

var prefix = toLower('${environmentName}-${resourceToken}')

// USER ROLES
var principalType = empty(runningOnGh) && empty(runningOnAdo) ? 'User' : 'ServicePrincipal'
module managedIdentity 'core/security/managed-identity.bicep' = {
  name: 'managed-identity'
  scope: resourceGroup
  params: {
    name: 'id-${resourceToken}'
    location: location
    tags: tags
  }
}

module openAi 'core/ai/cognitiveservices.bicep' = {
  name: 'openai'
  scope: openAiResourceGroup
  params: {
    name: !empty(openAiResourceName) ? openAiResourceName : '${resourceToken}-cog'
    location: !empty(openAiResourceLocation) ? openAiResourceLocation : location
    tags: tags
    sku: {
      name: !empty(openAiSkuName) ? openAiSkuName : 'S0'
    }
    deployments: [
      {
        name: openAiDeploymentName
        model: {
          format: 'OpenAI'
          name: 'gpt-35-turbo'
          version: '0613'
        }
        sku: {
          name: 'Standard'
          capacity: 30
        }
      }
      {
        name: openAiEmbeddingDeploymentName
        model: {
          format: 'OpenAI'
          name: 'text-embedding-ada-002'
          version: '2'
        }
        sku: {
          name: 'Standard'
          capacity: 20
        }
      }
    ]
  }
}

module search 'core/search/search-services.bicep' = {
  name: 'search'
  scope: resourceGroup
  params: {
    name: !empty(searchServiceName) ? searchServiceName : '${prefix}-search-contoso'
    location: location
    semanticSearch: 'standard'
    disableLocalAuth: true
  }
}

module cosmos 'core/database/cosmos/sql/cosmos-sql-db.bicep' = {
  name: 'cosmos'
  scope: resourceGroup
  params: {
    accountName: !empty(cosmosAccountName) ? cosmosAccountName : 'cosmos-contoso-${resourceToken}'
    databaseName: 'contoso-outdoor'
    location: location
    tags: union(tags, {
      defaultExperience: 'Core (SQL)'
      'hidden-cosmos-mmspecial': ''
    })
    containers: [
      {
        name: 'customers'
        id: 'customers'
        partitionKey: '/id'
      }
    ]
  }
}

module logAnalyticsWorkspace 'core/monitor/loganalytics.bicep' = {
  name: 'loganalytics'
  scope: resourceGroup
  params: {
    name: '${prefix}-loganalytics'
    location: location
    tags: tags
  }
}

module monitoring 'core/monitor/monitoring.bicep' = {
  name: 'monitoring'
  scope: resourceGroup
  params: {
    location: location
    tags: tags
    logAnalyticsName: logAnalyticsWorkspace.name
    applicationInsightsName: '${prefix}-appinsights'
    applicationInsightsDashboardName: '${prefix}-dashboard'
  }
}

// Container apps host (including container registry)
module containerApps 'core/host/container-apps.bicep' = {
  name: 'container-apps'
  scope: resourceGroup
  params: {
    name: 'app'
    location: location
    tags: tags
    containerAppsEnvironmentName: '${prefix}-containerapps-env'
    containerRegistryName: '${replace(prefix, '-', '')}registry'
    logAnalyticsWorkspaceName: logAnalyticsWorkspace.outputs.name
  }
}

module aca 'app/aca.bicep' = {
  name: 'aca'
  scope: resourceGroup
  params: {
    name: replace('${take(prefix, 19)}-ca', '--', '-')
    location: location
    tags: tags
    identityName: managedIdentity.outputs.managedIdentityName
    identityId: managedIdentity.outputs.managedIdentityClientId
    containerAppsEnvironmentName: containerApps.outputs.environmentName
    containerRegistryName: containerApps.outputs.registryName
    openAiDeploymentName: !empty(openAiDeploymentName) ? openAiDeploymentName : 'gpt-35-turbo'
    openAiEmbeddingDeploymentName: openAiEmbeddingDeploymentName
    openAiEndpoint: openAi.outputs.endpoint
    openAiType: openAiType
    openAiApiVersion: openAiApiVersion
    aiSearchEndpoint: search.outputs.endpoint
    aiSearchIndexName: aiSearchIndexName
    cosmosEndpoint: cosmos.outputs.endpoint
    cosmosDatabaseName: cosmosDatabaseName
    cosmosContainerName: cosmosContainerName
    appinsights_Connectionstring: monitoring.outputs.applicationInsightsConnectionString
  }
}

module aiSearchRole 'core/security/role.bicep' = {
  scope: resourceGroup
  name: 'ai-search-index-data-contributor'
  params: {
    principalId: managedIdentity.outputs.managedIdentityPrincipalId
    roleDefinitionId: '8ebe5a00-799e-43f5-93ac-243d3dce84a7' //Search Index Data Contributor
    principalType: 'ServicePrincipal'
  }
}

module cosmosRoleContributor 'core/security/role.bicep' = {
  scope: resourceGroup
  name: 'ai-search-service-contributor'
  params: {
    principalId: managedIdentity.outputs.managedIdentityPrincipalId
    roleDefinitionId: '7ca78c08-252a-4471-8644-bb5ff32d4ba0' //Search Service Contributor
    principalType: 'ServicePrincipal'
  }
}

module cosmosAccountRole 'core/security/role-cosmos.bicep' = {
  scope: resourceGroup
  name: 'cosmos-account-role'
  params: {
    principalId: managedIdentity.outputs.managedIdentityPrincipalId
    databaseAccountId: cosmos.outputs.accountId
    databaseAccountName: cosmos.outputs.accountName
  }
}

module appinsightsAccountRole 'core/security/role.bicep' = {
  scope: resourceGroup
  name: 'appinsights-account-role'
  params: {
    principalId: managedIdentity.outputs.managedIdentityPrincipalId
    roleDefinitionId: '3913510d-42f4-4e42-8a64-420c390055eb' // Monitoring Metrics Publisher
    principalType: 'ServicePrincipal'
  }
}

module userAiSearchRole 'core/security/role.bicep' = if (!empty(principalId)) {
  scope: resourceGroup
  name: 'user-ai-search-index-data-contributor'
  params: {
    principalId: principalId
    roleDefinitionId: '8ebe5a00-799e-43f5-93ac-243d3dce84a7' //Search Index Data Contributor
    principalType: principalType
  }
}

module userCosmosRoleContributor 'core/security/role.bicep' = if (!empty(principalId)) {
  scope: resourceGroup
  name: 'user-ai-search-service-contributor'
  params: {
    principalId: principalId
    roleDefinitionId: '7ca78c08-252a-4471-8644-bb5ff32d4ba0' //Search Service Contributor
    principalType: principalType
  }
}

module openaiRoleUser 'core/security/role.bicep' = if (!empty(principalId)) {
  scope: resourceGroup
  name: 'user-openai-user'
  params: {
    principalId: principalId
    roleDefinitionId: '5e0bd9bd-7b93-4f28-af87-19fc36ad61bd' //Cognitive Services OpenAI User
    principalType: principalType
  }
}

module userCosmosAccountRole 'core/security/role-cosmos.bicep' = if (!empty(principalId)) {
  scope: resourceGroup
  name: 'user-cosmos-account-role'
  params: {
    principalId: principalId
    databaseAccountId: cosmos.outputs.accountId
    databaseAccountName: cosmos.outputs.accountName
  }
}

output AZURE_LOCATION string = location
output AZURE_RESOURCE_GROUP string = resourceGroup.name

output AZURE_OPENAI_CHATGPT_DEPLOYMENT string = openAiDeploymentName
output AZURE_OPENAI_API_VERSION string = openAiApiVersion
output AZURE_OPENAI_ENDPOINT string = openAi.outputs.endpoint
output AZURE_OPENAI_NAME string = openAi.outputs.name
output AZURE_OPENAI_RESOURCE_GROUP string = openAiResourceGroup.name
output AZURE_OPENAI_SKU_NAME string = openAi.outputs.skuName
output AZURE_OPENAI_RESOURCE_GROUP_LOCATION string = openAiResourceGroup.location

output SERVICE_ACA_NAME string = aca.outputs.SERVICE_ACA_NAME
output SERVICE_ACA_URI string = aca.outputs.SERVICE_ACA_URI
output SERVICE_ACA_IMAGE_NAME string = aca.outputs.SERVICE_ACA_IMAGE_NAME

output AZURE_CONTAINER_ENVIRONMENT_NAME string = containerApps.outputs.environmentName
output AZURE_CONTAINER_REGISTRY_ENDPOINT string = containerApps.outputs.registryLoginServer
output AZURE_CONTAINER_REGISTRY_NAME string = containerApps.outputs.registryName

output APPINSIGHTS_CONNECTIONSTRING string = monitoring.outputs.applicationInsightsConnectionString

output OPENAI_TYPE string = 'azure'
output AZURE_EMBEDDING_NAME string = openAiEmbeddingDeploymentName

output COSMOS_ENDPOINT string = cosmos.outputs.endpoint
output AZURE_COSMOS_NAME string = cosmosDatabaseName
output COSMOS_CONTAINER string = cosmosContainerName
output AZURE_SEARCH_ENDPOINT string = search.outputs.endpoint
output AZURE_SEARCH_NAME string = search.outputs.name
