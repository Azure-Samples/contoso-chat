param cosmosAccounntName string
param aiResourceGroupName string
param aiHubName string

module cosmosConnection 'cosmos-connection.bicep' = {
  name: 'products-cosmos'
  scope: resourceGroup(aiResourceGroupName)
  params: {
    name: 'products-cosmos'
    hubName: aiHubName
    endpoint: cosmosAccount.properties.documentEndpoint
    database: 'products'
    container: 'customers'
    key: cosmosAccount.listKeys().primaryMasterKey
  }
}

resource cosmosAccount 'Microsoft.DocumentDB/databaseAccounts@2022-08-15' existing = {
  name: cosmosAccounntName
  scope: resourceGroup()
}
