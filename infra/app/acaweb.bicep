param name string
param location string = resourceGroup().location
param tags object = {}

param identityName string
param containerAppsEnvironmentName string
param containerRegistryName string
param serviceName string = 'acaweb'
param contosochatapiendpoint string

module webapp '../core/host/container-app-upsert.bicep' = {
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
        name: 'CONTOSO_CHAT_API_ENDPOINT'
        value: contosochatapiendpoint
      }      
    ]
    targetPort: 3000
  }
}

output WEBAPP_ACA_NAME string = webapp.outputs.name
output WEBAPP_ACA_URI string = webapp.outputs.uri
output WEBAPP_ACA_IMAGE_NAME string = webapp.outputs.imageName
