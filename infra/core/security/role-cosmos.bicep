metadata description = 'Creates a role assignment for a service principal.'
param principalId string
param databaseAccountId string
param databaseAccountName string

var roleDefinitionReader = '00000000-0000-0000-0000-000000000001' // Cosmos DB Built-in Data Reader
var roleDefinitionContributor = '00000000-0000-0000-0000-000000000002' // Cosmos DB Built-in Data Contributor

var roleDefinitionId = guid('sql-role-definition-', principalId, databaseAccountId)
var roleAssignmentId = guid(roleDefinitionId, principalId, databaseAccountId)
///subscriptions/070de2d1-125e-447f-8caf-511f7a99f764/resourceGroups/chatcontoso-rg/providers/Microsoft.DocumentDB/databaseAccounts/cosmos-contoso-qceliatc7cgpq/sqlRoleDefinitions/00000000-0000-0000-0000-000000000002

resource sqlRoleAssignment 'Microsoft.DocumentDB/databaseAccounts/sqlRoleAssignments@2023-04-15' = {
  name: '${databaseAccountName}/${roleAssignmentId}'
  //parent: databaseAccount
  properties:{
    principalId: principalId
    //roleDefinitionId: '/${subscription().id}/resourceGroups/<databaseAccountResourceGroup>/providers/Microsoft.DocumentDB/databaseAccounts/<myCosmosAccount>/sqlRoleDefinitions/<roleDefinitionId>'
    roleDefinitionId: '/${subscription().id}/resourceGroups/${resourceGroup().name}/providers/Microsoft.DocumentDB/databaseAccounts/${databaseAccountName}/sqlRoleDefinitions/${roleDefinitionContributor}'
    scope: databaseAccountId
  }
}
