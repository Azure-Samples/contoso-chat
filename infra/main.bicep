targetScope = 'subscription'
@minLength(1)
@maxLength(64)
@description('Name of the the environment which is used to generate a short unique hash used in all resources.')
param environmentName string

@minLength(1)
@description('Primary location for all resources')
param location string = 'swedencentral'

@description('Id of the user or app to assign application roles')
param principalId string = ''

// Necessary for GPT-4
param searchLocation string = 'eastus'
param resourceGroupName string = ''
var tags = { 'azd-env-name': environmentName }

// Organize resources in a resource group
resource rg 'Microsoft.Resources/resourceGroups@2021-04-01' = {
  name: !empty(resourceGroupName) ? resourceGroupName : 'rg-${environmentName}'
  location: location
  tags: tags
}

module resources 'resources.bicep' = {
  name: 'resources'
  scope: rg
  params: {
    environmentName: environmentName
    location: location
    tags: tags
    searchLocation: searchLocation
    principalId: principalId
  }
}

// output the names of the resources
output openai_name string = resources.outputs.openai_name
output cosmos_name string = resources.outputs.cosmos_name
output search_name string = resources.outputs.search_name
output mlhub_name string = resources.outputs.mlhub_name
output mlproject_name string = resources.outputs.mlproject_name

output AZURE_RESOURCE_GROUP string = rg.name
output CONTOSO_AI_SERVICES_ENDPOINT string = resources.outputs.openai_endpoint
output COSMOS_ENDPOINT string = resources.outputs.cosmos_endpoint
output CONTOSO_SEARCH_ENDPOINT string = resources.outputs.search_endpoint
output AZURE_CONTAINER_REGISTRY_NAME string = resources.outputs.acr_name
