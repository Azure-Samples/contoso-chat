@description('The AI Studio Hub Resource name')
param name string
@description('The display name of the AI Studio Hub Resource')
param displayName string = name
@description('The storage account ID to use for the AI Studio Hub Resource')
param storageAccountId string
@description('The key vault ID to use for the AI Studio Hub Resource')
param keyVaultId string
@description('The application insights ID to use for the AI Studio Hub Resource')
param appInsightsId string = ''
@description('The container registry ID to use for the AI Studio Hub Resource')
param containerRegistryId string = ''
@description('The OpenAI Cognitive Services account name to use for the AI Studio Hub Resource')
param openAiName string
@description('The Azure Cognitive Search service name to use for the AI Studio Hub Resource')
param aiSearchName string = ''

@description('The SKU name to use for the AI Studio Hub Resource')
param skuName string = 'Basic'
@description('The SKU tier to use for the AI Studio Hub Resource')
@allowed(['Basic', 'Free', 'Premium', 'Standard'])
param skuTier string = 'Basic'
@description('The public network access setting to use for the AI Studio Hub Resource')
@allowed(['Enabled','Disabled'])
param publicNetworkAccess string = 'Enabled'

param location string = resourceGroup().location
param tags object = {}

// NN:TODO resource hub 'Microsoft.MachineLearningServices/workspaces@2024-01-01-preview' = {
resource hub 'Microsoft.MachineLearningServices/workspaces@2024-04-01' = {
  name: name
  location: location
  tags: tags
  sku: {
    name: skuName
    tier: skuTier
  }
  kind: 'Hub'
  identity: {
    type: 'SystemAssigned'
  }
  properties: {
    friendlyName: displayName
    storageAccount: storageAccountId
    keyVault: keyVaultId
    applicationInsights: !empty(appInsightsId) ? appInsightsId : null
    containerRegistry: !empty(containerRegistryId) ? containerRegistryId : null
    hbiWorkspace: false
    managedNetwork: {
      isolationMode: 'Disabled'
    }
    v1LegacyMode: false
    publicNetworkAccess: publicNetworkAccess
    discoveryUrl: 'https://${location}.api.azureml.ms/discovery'
  }

/* NN:TODO
  resource contentSafetyDefaultEndpoint 'endpoints' = {
    name: 'Azure.ContentSafety'
    properties: {
      name: 'Azure.ContentSafety'
      endpointType: 'Azure.ContentSafety'
      associatedResourceId: openAi.id
    }
  }
*/

/*
  NN:TODO
  Connections are not in the GA Swagger - they are only in public preview of 2024-04-01-preview version
  That is what you specify with the workspace@ version for AML API version
  The ApiVersion specified in the metadata is for the Azure Cognitive Services version (that wraps the OpenAPI call)
 */

  resource openAiConnection 'connections@2024-04-01-preview' = { // NN:TODO Add @version to ensure resource is correctly versioned
    name: 'aoai-connection'
    properties: {
      category: 'AzureOpenAI'
      authType: 'ApiKey'
      isSharedToAll: true
      target: openAi.properties.endpoints['OpenAI Language Model Instance API']
      metadata: {
        //ApiVersion: '2023-07-01-preview'
        ApiVersion: '2024-02-01'
        ApiType: 'azure'
        ResourceId: openAi.id
      }
      credentials: {
        key: openAi.listKeys().key1
      }
    }
  }

  resource searchConnection 'connections' =
    if (!empty(aiSearchName)) {
      name: 'contoso-search'
      properties: {
        category: 'CognitiveSearch'
        authType: 'ApiKey'
        isSharedToAll: true
        target: 'https://${search.name}.search.windows.net/'
        credentials: {
          key: !empty(aiSearchName) ? search.listAdminKeys().primaryKey : ''
        }
      }
    }
}

resource openAi 'Microsoft.CognitiveServices/accounts@2023-05-01' existing = {
  name: openAiName
}

resource search 'Microsoft.Search/searchServices@2021-04-01-preview' existing =
  if (!empty(aiSearchName)) {
    name: aiSearchName
  }

output name string = hub.name
output id string = hub.id
output principalId string = hub.identity.principalId
