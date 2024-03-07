
metadata description = 'Creates an Azure AI Hub.'
param name string
param location string = resourceGroup().location
param tags object = {}
param aiHubId string
param cosmosId string
param cosmosDocEP string

resource mlProject 'Microsoft.MachineLearningServices/workspaces@2023-10-01' = {
  name: name
  location: location
  tags: tags
  sku: {
    name: 'Basic'
    tier: 'Basic'
  }
  kind: 'Project'
  identity: {
    type: 'SystemAssigned'
  }
  properties: {
    friendlyName: name
    hbiWorkspace: false
    v1LegacyMode: false
    publicNetworkAccess: 'Enabled'
    discoveryUrl: 'https://${location}.api.azureml.ms/discovery'
    // most properties are not allowed for a project workspace: "Project workspace shouldn't define ..."
    hubResourceId: aiHubId
  }
}


resource cosmosConnection 'Microsoft.MachineLearningServices/workspaces/connections@2023-10-01' = {
  parent: mlProject
  name: 'contoso-cosmos'
  properties: {
    category: 'CustomKeys'
    target: '_'
    authType: 'CustomKeys'
    credentials: {
      keys: {
        key: listKeys(cosmosId, '2023-11-15').primaryMasterKey
        }
    }
    metadata: {
      endpoint: cosmosDocEP
      databaseId: 'contoso-outdoor'
      containerId: 'customers'
      'azureml.flow.connection_type': 'Custom'
      'azureml.flow.module': 'promptflow.connections'

    }
  }
}

output mlProjectName string = mlProject.name
