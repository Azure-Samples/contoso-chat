param applicationInsightsId string
param containerRegistryId string
param contosoChatSfAiName string = 'contoso-chat-sf-ai'
param contosoChatSfAiProjectName string = 'contoso-chat-sf-aiproj'
param keyVaultId string
param location string
param openAiEndpoint string
param openAiName string
param searchName string
param storageAccountId string

// In ai.azure.com: Azure AI Resource
resource workspace 'Microsoft.MachineLearningServices/workspaces@2023-08-01-preview' = {
  name: contosoChatSfAiName
  location: location
  sku: {
    name: 'Basic'
    tier: 'Basic'
  }
  kind: 'Hub' 
  identity: {
    type: 'SystemAssigned'
  }
  properties: {
    friendlyName: contosoChatSfAiName
    storageAccount: storageAccountId
    keyVault: keyVaultId
    applicationInsights: applicationInsightsId
    hbiWorkspace: false
    managedNetwork: {
      isolationMode: 'Disabled'
    }
    v1LegacyMode: false
    containerRegistry: containerRegistryId
    publicNetworkAccess: 'Enabled'
    discoveryUrl: 'https://${location}.api.azureml.ms/discovery'
  }

  resource openAiDefaultEndpoint 'endpoints' = {
    name: 'Azure.OpenAI'
    properties: {
      name: 'Azure.OpenAI'
      endpointType: 'Azure.OpenAI'
      associatedResourceId: openai.id
    }
  }

  resource contentSafetyDefaultEndpoint 'endpoints' = {
    name: 'Azure.ContentSafety'
    properties: {
      name: 'Azure.ContentSafety'
      endpointType: 'Azure.ContentSafety'
      associatedResourceId: openai.id
    }
  }

  resource openAiConnection 'connections' = {
    name: 'aoai-connection'
    properties: {
      category: 'AzureOpenAI'
      target: openAiEndpoint
      authType: 'ApiKey'
      metadata: {
          ApiVersion: '2023-07-01-preview'
          ApiType: 'azure'
          ResourceId: openai.id
      }
      credentials: {
        key: openai.listKeys().key1
      }
    }
  }

  resource searchConnection 'connections' = {
    name: 'contoso-search'
    properties: {
      category: 'CognitiveSearch'
      target: 'https://${search.name}.search.windows.net/'
      authType: 'ApiKey'
      credentials: {
        key: search.listAdminKeys().primaryKey
      }
    }
  }
}

// In ai.azure.com: Azure AI Project
resource project 'Microsoft.MachineLearningServices/workspaces@2023-10-01' = {
  name: contosoChatSfAiProjectName 
  location: location
  sku: {
    name: 'Basic'
    tier: 'Basic'
  }
  kind: 'Project'
  identity: {
    type: 'SystemAssigned'
  }
  properties: {
    friendlyName: contosoChatSfAiProjectName 
    hbiWorkspace: false
    v1LegacyMode: false
    publicNetworkAccess: 'Enabled'
    discoveryUrl: 'https://${location}.api.azureml.ms/discovery'
    // most properties are not allowed for a project workspace: "Project workspace shouldn't define ..."
    hubResourceId: workspace.id
  }
}

resource openai 'Microsoft.CognitiveServices/accounts@2023-05-01' existing = {
  name: openAiName
}

resource search 'Microsoft.Search/searchServices@2021-04-01-preview' existing = {
  name: searchName
}

output workspaceName string = workspace.name
output projectName string = project.name
output principalId string = project.identity.principalId
