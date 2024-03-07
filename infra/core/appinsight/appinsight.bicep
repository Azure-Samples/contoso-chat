
metadata description = 'Creates an Azure App Insight Instance.'
param name string
param location string = resourceGroup().location
param tags object = {}
param logAnalyticsWsId string


resource appinsights 'microsoft.insights/components@2020-02-02' = {
  name: name
  location: location
  kind: 'web'
  tags: tags
  properties: {
    Application_Type: 'web'
    RetentionInDays: 90
    WorkspaceResourceId: logAnalyticsWsId
    IngestionMode: 'LogAnalytics'
    publicNetworkAccessForIngestion: 'Enabled'
    publicNetworkAccessForQuery: 'Enabled'
  }
}

output appinsightsId string = appinsights.id
