param name string
param hubName string
param endpoint string
param database string
param container string

@secure()
param key string

resource cosmosConnection 'Microsoft.MachineLearningServices/workspaces/connections@2024-01-01-preview' = {
  parent: hub
  name: name
  properties: {
    authType: 'CustomKeys'
    category: 'CustomKeys'
    isSharedToAll: true
    credentials: {
      keys: {
        key: key
      }
    }
    metadata: {
      endpoint: endpoint
      databaseId: database
      containerId: container
      'azureml.flow.connection_type': 'Custom'
      'azureml.flow.module': 'promptflow.connections'
    }
  }
}

resource hub 'Microsoft.MachineLearningServices/workspaces@2024-01-01-preview' existing = {
  name: hubName
}
