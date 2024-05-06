@minLength(1)
@description('Primary location for all resources')
param location string

@description('The AI Hub resource name.')
param hubName string
@description('The AI Project resource name.')
param projectName string
@description('The Key Vault resource name.')
param keyVaultName string
@description('The Storage Account resource name.')
param storageAccountName string
@description('The Open AI resource name.')
param openAiName string
@description('The Open AI model deployments.')
param openAiModelDeployments array = []
@description('The Log Analytics resource name.')
param logAnalyticsName string = ''
@description('The Application Insights resource name.')
param appInsightsName string = ''
@description('The Container Registry resource name.')
param containerRegistryName string = ''
@description('The Azure Search resource name.')
param searchName string = ''
param tags object = {}

module hubDependencies '../ai/hub-dependencies.bicep' = {
  name: 'hubDependencies'
  params: {
    location: location
    tags: tags
    keyVaultName: keyVaultName
    storageAccountName: storageAccountName
    containerRegistryName: containerRegistryName
    appInsightsName: appInsightsName
    logAnalyticsName: logAnalyticsName
    openAiName: openAiName
    openAiModelDeployments: openAiModelDeployments
    searchName: searchName
  }
}

module hub '../ai/hub.bicep' = {
  name: 'hub'
  params: {
    location: location
    tags: tags
    name: hubName
    displayName: hubName
    keyVaultId: hubDependencies.outputs.keyVaultId
    storageAccountId: hubDependencies.outputs.storageAccountId
    containerRegistryId: hubDependencies.outputs.containerRegistryId
    appInsightsId: hubDependencies.outputs.appInsightsId
    openAiName: hubDependencies.outputs.openAiName
    aiSearchName: hubDependencies.outputs.searchName
  }
}

module project '../ai/project.bicep' = {
  name: 'project'
  params: {
    location: location
    tags: tags
    name: projectName
    displayName: projectName
    hubName: hub.outputs.name
    keyVaultName: hubDependencies.outputs.keyVaultName
  }
}

// Outputs
// Resource Group
output resourceGroupName string = resourceGroup().name

// Hub
output hubName string = hub.outputs.name
output hubPrincipalId string = hub.outputs.principalId

// Project
output projectName string = project.outputs.name
output projectPrincipalId string = project.outputs.principalId

// Key Vault
output keyVaultName string = hubDependencies.outputs.keyVaultName
output keyVaultEndpoint string = hubDependencies.outputs.keyVaultEndpoint

// Application Insights
output appInsightsName string = hubDependencies.outputs.appInsightsName
output logAnalyticsWorkspaceName string = hubDependencies.outputs.logAnalyticsWorkspaceName

// Container Registry
output containerRegistryName string = hubDependencies.outputs.containerRegistryName
output containerRegistryEndpoint string = hubDependencies.outputs.containerRegistryEndpoint

// Storage Account
output storageAccountName string = hubDependencies.outputs.storageAccountName

// Open AI
output openAiName string = hubDependencies.outputs.openAiName
output openAiEndpoint string = hubDependencies.outputs.openAiEndpoint

// Search
output searchName string = hubDependencies.outputs.searchName
output searchEndpoint string = hubDependencies.outputs.searchEndpoint
