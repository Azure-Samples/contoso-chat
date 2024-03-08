targetScope = 'subscription'

@minLength(1)
@maxLength(64)
@description('Name of the the environment which is used to generate a short unique hash used in all resources.')
param environmentName string

@minLength(1)
@description('Primary location for all resources')
param location string

// Optional parameters to override the default azd resource naming conventions. Update the main.parameters.json file to provide values. e.g.,:
// "resourceGroupName": {
//      "value": "myGroupName"
// }

param applicationInsightsName string = ''
param azureOpenAiResourceName string = ''
param containerRegistryName string = ''
param cosmosAccountName string = ''
param keyVaultName string = ''
param resourceGroupName string = ''
param searchLocation string = ''
param searchServiceName string = ''
param storageServiceName string = ''

param accountsContosoChatSfAiServicesName string = 'contoso-chat-sf-ai-aiservices'
param workspacesApwsContosoChatSfAiName string = 'apws-contoso-chat-sf-ai'

@description('Id of the user or app to assign application roles')
param principalId string = ''

var openAiSubdomain  = '${accountsContosoChatSfAiServicesName}${resourceToken}'
var openAiEndpoint = 'https://${openAiSubdomain }.openai.azure.com/'
var resourceToken = toLower(uniqueString(subscription().id, environmentName, location))
var tags = { 'azd-env-name': environmentName }

// Organize resources in a resource group
resource rg 'Microsoft.Resources/resourceGroups@2021-04-01' = {
  name: !empty(resourceGroupName) ? resourceGroupName : 'rg-${environmentName}'
  location: location
  tags: tags
}

module containerRegistry 'core/host/container-registry.bicep' = {
  name: 'containerregistry'
  scope: rg
  params: {
    name: !empty(containerRegistryName) ? containerRegistryName : 'acrcontoso${resourceToken}'
    location: location
    tags: tags
    sku: {
      name: 'Standard'
    }
    scopeMaps: [
      {
        name: '_repositories_pull'
        properties: {
          description: 'Can pull any repository of the registry'
          actions: [
            'repositories/*/content/read'
          ]
        }
      }
      {
        name: '_repositories_pull_metadata_read'
        properties: {
          description: 'Can perform all read operations on the registry'
          actions: [
            'repositories/*/content/read'
            'repositories/*/metadata/read'
          ]
        }
      }
      {
        name: '_repositories_push'
        properties: {
          description: 'Can push to any repository of the registry'
          actions: [
            'repositories/*/content/read'
            'repositories/*/content/write'
          ]
        }
      }
      {
        name: '_repositories_push_metadata_write'
        properties: {
          description: 'Can perform all read and write operations on the registry'
          actions: [
            'repositories/*/metadata/read'
            'repositories/*/metadata/write'
            'repositories/*/content/read'
            'repositories/*/content/write'
          ]
        }
      }
      {
        name: '_repositories_admin'
        properties: {
          description: 'Can perform all read, write and delete operations on the registry'
          actions: [
            'repositories/*/metadata/read'
            'repositories/*/metadata/write'
            'repositories/*/content/read'
            'repositories/*/content/write'
            'repositories/*/content/delete'
          ]
        }
      }
    ]
  }
}

module cosmos 'core/database/cosmos/sql/cosmos-sql-db.bicep' = {
  name: 'cosmos'
  scope: rg
  params: {
    accountName: !empty(cosmosAccountName) ? cosmosAccountName : 'cosmos-contoso-${resourceToken}'
    databaseName: 'contoso-outdoor'
    location: location
    tags: union(tags, {
      defaultExperience: 'Core (SQL)'
      'hidden-cosmos-mmspecial': ''
    })
    keyVaultName: keyvault.outputs.name
    containers: [
      {
        name: 'customers'
        id: 'customers'
        partitionKey: '/id'
      }
    ]
  }
}

module keyvault 'core/security/keyvault.bicep' = {
  name: !empty(keyVaultName) ? keyVaultName : 'kvcontoso${resourceToken}'
  scope: rg
  params: {
    name: !empty(keyVaultName) ? keyVaultName : 'kvcontoso${resourceToken}'
    location: location
    tags: tags
    principalId: principalId
  }
}

module keyVaultAccess 'core/security/keyvalut-access.bicep' = {
  name: 'keyvault-access'
  scope: rg
  params: {
    keyVaultName: keyvault.name
    principalId: machineLearning.outputs.principalId
  }
}

module machineLearning 'app/ml.bicep' = {
  name: 'machinelearning'
  scope: rg
  params: {
    location: location
    storageAccountId: storage.outputs.id
    keyVaultId: keyvault.outputs.id
    applicationInsightsId: monitoring.outputs.applicationInsightsId
    containerRegistryId: containerRegistry.outputs.id
    openAiEndpoint: openAiEndpoint
    openAiName: openai.outputs.name
    searchName: search.outputs.name
  }
}

module monitoring 'core/monitor/monitoring.bicep' = {
  name: 'monitoring'
  scope: rg
  params: {
    logAnalyticsName: workspacesApwsContosoChatSfAiName
    applicationInsightsName: !empty(applicationInsightsName) ? applicationInsightsName : '${environmentName}-appi-contoso${resourceToken}'
    location: location
    tags: tags
  }
}


module openai 'core/ai/cognitiveservices.bicep' = {
  name: 'openai'
  scope: rg
  params: {
    name: !empty(azureOpenAiResourceName) ? azureOpenAiResourceName : '${environmentName}-openai-contoso-${resourceToken}'
    location: location
    tags: tags
    kind: 'AIServices'
    customSubDomainName: openAiSubdomain
    deployments: [
      {
        name: 'gpt-35-turbo'
        model: {
          format: 'OpenAI'
          name: 'gpt-35-turbo'
          version: '0613'
        }
        sku: {
          name: 'Standard'
          capacity: 20
        }
      }
      {
        name: 'gpt-4'
        model: {
          format: 'OpenAI'
          name: 'gpt-4'
          version: '0613'
        }
        sku: {
          name: 'Standard'
          capacity: 10
        }
      }
      {
        name: 'text-embedding-ada-002'
        model: {
          format: 'OpenAI'
          name: 'text-embedding-ada-002'
          version: '2'
        }
        sku: {
          name: 'Standard'
          capacity: 20
        }
      }
    ]
  }
}

module search 'core/search/search-services.bicep' = {
  name: 'search'
  scope: rg
  params: {
    name: !empty(searchServiceName) ? searchServiceName : '${environmentName}-search-contoso${resourceToken}'
    location: searchLocation
    semanticSearch: 'free'
  }
}

module storage 'core/storage/storage-account.bicep' = {
  name: 'storage'
  scope: rg
  params: {
    name: !empty(storageServiceName) ? storageServiceName : 'stcontoso${resourceToken}'
    location: location
    containers: [
      {
        name: 'default'
      }
    ]
    files: [
      {
        name: 'default'
      }
    ]
    queues: [
      {
        name: 'default'
      }
    ]
    tables: [
      {
        name: 'default'
      }
    ]
    corsRules: [
      {
        allowedOrigins: [
          'https://mlworkspace.azure.ai'
          'https://ml.azure.com'
          'https://*.ml.azure.com'
          'https://ai.azure.com'
          'https://*.ai.azure.com'
          'https://mlworkspacecanary.azure.ai'
          'https://mlworkspace.azureml-test.net'
        ]
        allowedMethods: [
          'GET'
          'HEAD'
          'POST'
          'PUT'
          'DELETE'
          'OPTIONS'
          'PATCH'
        ]
        maxAgeInSeconds: 1800
        exposedHeaders: [
          '*'
        ]
        allowedHeaders: [
          '*'
        ]
      }
    ]
    deleteRetentionPolicy: {
      allowPermanentDelete: false
      enabled: false
    }
    shareDeleteRetentionPolicy: {
      enabled: true
      days: 7
    }
  }
}

module userAcrRolePush 'core/security/role.bicep' = {
  name: 'user-acr-role-push'
  scope: rg
  params: {
    principalId: principalId
    roleDefinitionId: '8311e382-0749-4cb8-b61a-304f252e45ec'
    principalType: 'User'
  }
}

module userAcrRolePull 'core/security/role.bicep' = {
  name: 'user-acr-role-pull'
  scope: rg
  params: {
    principalId: principalId
    roleDefinitionId: '7f951dda-4ed3-4680-a7ca-43fe172d538d'
    principalType: 'User'
  }
}

module userRoleDataScientist 'core/security/role.bicep' = {
  name: 'user-role-data-scientist'
  scope: rg
  params: {
    principalId: principalId
    roleDefinitionId: 'f6c7c914-8db3-469d-8ca1-694a8f32e121'
    principalType: 'User'
  }
}

module userRoleSecretsReader 'core/security/role.bicep' = {
  name: 'user-role-secrets-reader'
  scope: rg
  params: {
    principalId: principalId
    roleDefinitionId: 'ea01e6af-a1c1-4350-9563-ad00f8c72ec5'
    principalType: 'User'
  }
}

module mlServiceRoleDataScientist 'core/security/role.bicep' = {
  name: 'ml-service-role-data-scientist'
  scope: rg
  params: {
    principalId: machineLearning.outputs.principalId
    roleDefinitionId: 'f6c7c914-8db3-469d-8ca1-694a8f32e121'
    principalType: 'ServicePrincipal'
  }
}

module mlServiceRoleSecretsReader 'core/security/role.bicep' = {
  name: 'ml-service-role-secrets-reader'
  scope: rg
  params: {
    principalId: machineLearning.outputs.principalId
    roleDefinitionId: 'ea01e6af-a1c1-4350-9563-ad00f8c72ec5'
    principalType: 'ServicePrincipal'
  }
}

// output the names of the resources
output AZURE_OPENAI_NAME string = openai.outputs.name
output AZURE_COSMOS_NAME string = cosmos.outputs.accountName
output AZURE_SEARCH_NAME string = search.outputs.name
output AZURE_WORKSPACE_NAME string = machineLearning.outputs.workspaceName
output AZURE_MLPROJECT_NAME string = machineLearning.outputs.projectName

output AZURE_RESOURCE_GROUP string = rg.name
output CONTOSO_AI_SERVICES_ENDPOINT string = openAiEndpoint
output COSMOS_ENDPOINT string = cosmos.outputs.endpoint
output CONTOSO_SEARCH_ENDPOINT string = search.outputs.endpoint
output AZURE_CONTAINER_REGISTRY_NAME string = containerRegistry.outputs.name
output AZURE_KEY_VAULT_NAME string = keyvault.outputs.name
