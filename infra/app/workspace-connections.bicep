param cosmosAccounntName string
param aiResourceGroupName string
param aiHubName string

// NN: Update connection names to reflect v1
//     TODO: refactor to use environment variables for flexibility
module cosmosConnection 'cosmos-connection.bicep' = {
  name: 'contoso-cosmos'
  scope: resourceGroup(aiResourceGroupName)
  params: {
    name: 'contoso-cosmos'
    hubName: aiHubName
    endpoint: cosmosAccount.properties.documentEndpoint
    database: 'contoso-outdoor'
    container: 'customers'
    key: cosmosAccount.listKeys().primaryMasterKey
  }
}

resource cosmosAccount 'Microsoft.DocumentDB/databaseAccounts@2022-08-15' existing = {
  name: cosmosAccounntName
  scope: resourceGroup()
}
