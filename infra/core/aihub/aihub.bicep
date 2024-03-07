metadata description = 'Creates an Azure AI Hub.'
param name string
param location string = resourceGroup().location
param tags object = {}
param storageId string
param keyvaultId string
param appinsightsId string
param containerRegistryId string
param openaiId string
param openaiEndpoint string
param aiSearchId string
param aiSearchName string


resource mlHub 'Microsoft.MachineLearningServices/workspaces@2023-08-01-preview' = {
  name: name
  location: location
  tags: tags
  sku: {
    name: 'Basic'
    tier: 'Basic'
  }
  kind: 'Hub' 
  identity: {
    type: 'SystemAssigned'
  }
  properties: {
    friendlyName: name
    storageAccount: storageId
    keyVault: keyvaultId
    applicationInsights: appinsightsId
    hbiWorkspace: false
    managedNetwork: {
      isolationMode: 'Disabled'
    }
    v1LegacyMode: false
    containerRegistry: containerRegistryId
    publicNetworkAccess: 'Enabled'
    discoveryUrl: 'https://${location}.api.azureml.ms/discovery'
  }

  resource openaiDefaultEndpoint 'endpoints' = {
    name: 'Azure.OpenAI'
    properties: {
      name: 'Azure.OpenAI'
      endpointType: 'Azure.OpenAI'
      associatedResourceId: openaiId
    }
  }

  // resource contentSafetyDefaultEndpoint 'endpoints' = {
  //   name: 'Azure.ContentSafety'
  //   properties: {
  //     name: 'Azure.ContentSafety'
  //     endpointType: 'Azure.ContentSafety'
  //     associatedResourceId: openaiId
  //   }
  // }

  resource openaiConnection 'connections' = {
    name: 'aoai-connection'
    properties: {
      category: 'AzureOpenAI'
      target: openaiEndpoint
      authType: 'ApiKey'
      metadata: {
          ApiVersion: '2023-07-01-preview'
          ApiType: 'azure'
          ResourceId: openaiId
      }
      credentials: {
        key: listKeys(openaiId, '2023-05-01').key1
      }
    }
  }

  resource searchConnection 'connections' = {
    name: 'contoso-search'
    properties: {
      category: 'CognitiveSearch'
      target: 'https://${aiSearchName}.search.windows.net/'
      authType: 'ApiKey'
      credentials: {
        key: listAdminKeys(aiSearchId, '2023-11-01').primaryKey
      }
    }
  }
}



output mlHubId string = mlHub.id
output mlHubName string = mlHub.name
