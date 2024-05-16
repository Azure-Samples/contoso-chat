param name string
param location string = resourceGroup().location
param tags object = {}

var cognitiveServicesUserRoleDefinitionId = resourceId('Microsoft.Authorization/roleDefinitions', '5e0bd9bd-7b93-4f28-af87-19fc36ad61bd')

resource managedIdentity 'Microsoft.ManagedIdentity/userAssignedIdentities@2018-11-30' = {
  name: name
  location: location
  tags: union(tags, { 'azd-service-name': name })
}

// Assign the Cognitive Services User role to the user-defined managed identity used by workloads
resource cognitiveServicesUserRoleAssignment 'Microsoft.Authorization/roleAssignments@2022-04-01' = {
  name: guid(managedIdentity.id, cognitiveServicesUserRoleDefinitionId)
  scope: resourceGroup()
  properties: {
    roleDefinitionId: cognitiveServicesUserRoleDefinitionId
    principalId: managedIdentity.properties.principalId
    principalType: 'ServicePrincipal'
  }
}

output managedIdentityName string = managedIdentity.name
output managedIdentityClientId string = managedIdentity.properties.clientId
output managedIdentityPrincipalId string = managedIdentity.properties.principalId
