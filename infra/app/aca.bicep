param name string
param location string = resourceGroup().location
param tags object = {}

param identityName string
param identityId string
param containerAppsEnvironmentName string
param containerRegistryName string
param serviceName string = 'aca'
param openAiDeploymentName string
param openAiEndpoint string
param openAiApiVersion string
param openAiEmbeddingDeploymentName string
param openAiType string
param cosmosEndpoint string
param cosmosDatabaseName string
param cosmosContainerName string
param aiSearchEndpoint string
param aiSearchIndexName string
param appinsights_Connectionstring string


module app '../core/host/container-app-upsert.bicep' = {
  name: '${serviceName}-container-app-module'
  params: {
    name: name
    location: location
    tags: union(tags, { 'azd-service-name': serviceName })
    identityName: identityName
    identityType: 'UserAssigned'
    containerAppsEnvironmentName: containerAppsEnvironmentName
    containerRegistryName: containerRegistryName
    env: [
      {
        name: 'AZURE_CLIENT_ID'
        value: identityId
      }
      {
        name: 'COSMOS_ENDPOINT'
        value: cosmosEndpoint
      }
      {
        name: 'AZURE_COSMOS_NAME'
        value: cosmosDatabaseName
      }
      {
        name: 'COSMOS_CONTAINER'
        value: cosmosContainerName
      }
      {
        name: 'AZURE_SEARCH_ENDPOINT'
        value: aiSearchEndpoint
      }
      {
        name: 'AZUREAISEARCH__INDEX_NAME'
        value: aiSearchIndexName
      }
      {
        name: 'OPENAI_TYPE'
        value: openAiType
      }
      {
        name: 'AZURE_OPENAI_API_VERSION'
        value: openAiApiVersion
      }
      {
        name: 'AZURE_OPENAI_ENDPOINT'
        value: openAiEndpoint
      }
      {
        name: 'AZURE_OPENAI_CHAT_DEPLOYMENT'
        value: openAiDeploymentName
      }
      {
        name: 'AZURE_EMBEDDING_NAME'
        value: openAiEmbeddingDeploymentName
      }
      {
        name: 'APPINSIGHTS_CONNECTIONSTRING'
        value: appinsights_Connectionstring
      }

    ]
    targetPort: 80
  }
}

output SERVICE_ACA_NAME string = app.outputs.name
output SERVICE_ACA_URI string = app.outputs.uri
output SERVICE_ACA_IMAGE_NAME string = app.outputs.imageName
