metadata description = 'Creates an Application Insights instance based on an existing Log Analytics workspace.'
param name string
param dashboardName string = ''
param location string = resourceGroup().location
param tags object = {}
param logAnalyticsWorkspaceId string

var workbookJson = string(loadJsonContent('gen-ai-insights.json'))

resource applicationInsights 'Microsoft.Insights/components@2020-02-02' = {
  name: name
  location: location
  tags: tags
  kind: 'web'
  properties: {
    Application_Type: 'web'
    WorkspaceResourceId: logAnalyticsWorkspaceId
  }
}

module applicationInsightsDashboard 'applicationinsights-dashboard.bicep' = if (!empty(dashboardName)) {
  name: 'application-insights-dashboard'
  params: {
    name: dashboardName
    location: location
    applicationInsightsName: applicationInsights.name
  }
}

//Deploy application insights workbook resource
resource genAiInsightsWorkbook 'Microsoft.Insights/workbooks@2023-06-01' = {
  name:  guid(resourceGroup().id, 'Microsoft.Insights/workbooks', 'Gen-AI-Insights')
  location: location
  tags: tags
  kind: 'shared' 
  properties: {
    sourceId: 'Azure Monitor'
    category: 'workbook'
    description: 'Gen-AI-Insights-Workbook'
    displayName: 'Gen-AI-Insights'
    serializedData: workbookJson
    version: 'Notebook/1.0'
  }
}

output connectionString string = applicationInsights.properties.ConnectionString
output id string = applicationInsights.id
output instrumentationKey string = applicationInsights.properties.InstrumentationKey
output name string = applicationInsights.name
output workbookId string = genAiInsightsWorkbook.id
