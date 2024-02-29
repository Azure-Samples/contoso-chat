var resourceToken = toLower(uniqueString(subscription().id, resourceGroup().name, location))

param workspaces_contoso_chat_sf_ai_name string = 'contoso-chat-sf-ai'
param accounts_contoso_chat_sf_ai_aiservices_name string = 'contoso-chat-sf-ai-aiservices'
param workspaces_contoso_chat_sf_aiproj_name string = 'contoso-chat-sf-aiproj'
param workspaces_apws_contosochatsfai362802272292_name string = 'apws-contosochatsfai362802272292'

// Necessary for GPT-4
param location string = 'swedencentral'
param searchLocation string = 'eastus'

var openaiSubdomain = '${accounts_contoso_chat_sf_ai_aiservices_name}${resourceToken}'
var openaiEndpoint = 'https://${openaiSubdomain}.openai.azure.com/'
resource openai 'Microsoft.CognitiveServices/accounts@2023-10-01-preview' = {
  name: 'oai-contoso${resourceToken}'
  location: location
  sku: {
    name: 'S0'
  }
  kind: 'AIServices'
  properties: {
    customSubDomainName: openaiSubdomain
    publicNetworkAccess: 'Enabled'
  }
}

var deployments = [
  {
    name: 'gpt-35-turbo'
    model: {
      format: 'OpenAI'
      name: 'gpt-35-turbo'
      version: '0613'
    }
    sku: {
      name: 'Standard'
      capacity: 120
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
      capacity: 120
    }
  }
]

@batchSize(1)
resource deployment 'Microsoft.CognitiveServices/accounts/deployments@2023-05-01' = [for deployment in deployments: {
  parent: openai
  name: deployment.name
  sku: deployment.sku
  properties: {
    model: deployment.model
  }
}]


resource containerRegistry 'Microsoft.ContainerRegistry/registries@2023-11-01-preview' = {
  name: 'acrcontoso${resourceToken}'
  location: location
  sku: {
    name: 'Standard'
  }
  properties: {
    adminUserEnabled: false
    policies: {
      quarantinePolicy: {
        status: 'disabled'
      }
      trustPolicy: {
        type: 'Notary'
        status: 'disabled'
      }
      retentionPolicy: {
        days: 7
        status: 'disabled'
      }
      exportPolicy: {
        status: 'enabled'
      }
      azureADAuthenticationAsArmPolicy: {
        status: 'enabled'
      }
      softDeletePolicy: {
        retentionDays: 7
        status: 'disabled'
      }
    }
    encryption: {
      status: 'disabled'
    }
    dataEndpointEnabled: false
    publicNetworkAccess: 'Enabled'
    networkRuleBypassOptions: 'AzureServices'
    zoneRedundancy: 'Disabled'
    anonymousPullEnabled: false
    metadataSearch: 'Disabled'
  }
}

resource registries_crcontosochatsfai868026252389_name_repositories_pull 'Microsoft.ContainerRegistry/registries/scopeMaps@2023-11-01-preview' = {
  parent: containerRegistry
  name: '_repositories_pull'
  properties: {
    description: 'Can pull any repository of the registry'
    actions: [
      'repositories/*/content/read'
    ]
  }
}

resource registries_crcontosochatsfai868026252389_name_repositories_pull_metadata_read 'Microsoft.ContainerRegistry/registries/scopeMaps@2023-11-01-preview' = {
  parent: containerRegistry
  name: '_repositories_pull_metadata_read'
  properties: {
    description: 'Can perform all read operations on the registry'
    actions: [
      'repositories/*/content/read'
      'repositories/*/metadata/read'
    ]
  }
}

resource registries_crcontosochatsfai868026252389_name_repositories_push 'Microsoft.ContainerRegistry/registries/scopeMaps@2023-11-01-preview' = {
  parent: containerRegistry
  name: '_repositories_push'
  properties: {
    description: 'Can push to any repository of the registry'
    actions: [
      'repositories/*/content/read'
      'repositories/*/content/write'
    ]
  }
}

resource registries_crcontosochatsfai868026252389_name_repositories_push_metadata_write 'Microsoft.ContainerRegistry/registries/scopeMaps@2023-11-01-preview' = {
  parent: containerRegistry
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

resource registries_crcontosochatsfai868026252389_name_repositories_admin 'Microsoft.ContainerRegistry/registries/scopeMaps@2023-11-01-preview' = {
  parent: containerRegistry
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

resource cosmos 'Microsoft.DocumentDB/databaseAccounts@2023-09-15' = {
  name: 'cosmos-contoso${resourceToken}'
  location: location
  tags: {
    defaultExperience: 'Core (SQL)'
    'hidden-cosmos-mmspecial': ''
  }
  kind: 'GlobalDocumentDB'
  identity: {
    type: 'None'
  }
  properties: {
    publicNetworkAccess: 'Enabled'
    enableAutomaticFailover: false
    enableMultipleWriteLocations: false
    isVirtualNetworkFilterEnabled: false
    virtualNetworkRules: []
    disableKeyBasedMetadataWriteAccess: false
    enableFreeTier: false
    enableAnalyticalStorage: false
    analyticalStorageConfiguration: {
      schemaType: 'WellDefined'
    }
    databaseAccountOfferType: 'Standard'
    defaultIdentity: 'FirstPartyIdentity'
    networkAclBypass: 'None'
    disableLocalAuth: false
    enablePartitionMerge: false
    enableBurstCapacity: false
    minimalTlsVersion: 'Tls12'
    consistencyPolicy: {
      defaultConsistencyLevel: 'Session'
      maxIntervalInSeconds: 5
      maxStalenessPrefix: 100
    }
    locations: [
      {
        locationName: location
        failoverPriority: 0
        isZoneRedundant: false
      }
    ]
    cors: []
    capabilities: []
    ipRules: []
    backupPolicy: {
      type: 'Periodic'
      periodicModeProperties: {
        backupIntervalInMinutes: 240
        backupRetentionIntervalInHours: 8
        backupStorageRedundancy: 'Geo'
      }
    }
    networkAclBypassResourceIds: []
  }
}


resource databaseAccounts_contoso_chat_sf_cosmos_name_contoso_outdoor 'Microsoft.DocumentDB/databaseAccounts/sqlDatabases@2023-09-15' = {
  parent: cosmos
  name: 'contoso-outdoor'
  properties: {
    resource: {
      id: 'contoso-outdoor'
    }
  }
}

resource databaseAccounts_contoso_chat_sf_cosmos_name_00000000_0000_0000_0000_000000000001 'Microsoft.DocumentDB/databaseAccounts/sqlRoleDefinitions@2023-09-15' = {
  parent: cosmos
  name: '00000000-0000-0000-0000-000000000001'
  properties: {
    roleName: 'Cosmos DB Built-in Data Reader'
    type: 'BuiltInRole'
    assignableScopes: [
      cosmos.id
    ]
    permissions: [
      {
        dataActions: [
          'Microsoft.DocumentDB/databaseAccounts/readMetadata'
          'Microsoft.DocumentDB/databaseAccounts/sqlDatabases/containers/executeQuery'
          'Microsoft.DocumentDB/databaseAccounts/sqlDatabases/containers/readChangeFeed'
          'Microsoft.DocumentDB/databaseAccounts/sqlDatabases/containers/items/read'
        ]
        notDataActions: []
      }
    ]
  }
}

resource databaseAccounts_contoso_chat_sf_cosmos_name_00000000_0000_0000_0000_000000000002 'Microsoft.DocumentDB/databaseAccounts/sqlRoleDefinitions@2023-09-15' = {
  parent: cosmos
  name: '00000000-0000-0000-0000-000000000002'
  properties: {
    roleName: 'Cosmos DB Built-in Data Contributor'
    type: 'BuiltInRole'
    assignableScopes: [
      cosmos.id
    ]
    permissions: [
      {
        dataActions: [
          'Microsoft.DocumentDB/databaseAccounts/readMetadata'
          'Microsoft.DocumentDB/databaseAccounts/sqlDatabases/containers/*'
          'Microsoft.DocumentDB/databaseAccounts/sqlDatabases/containers/items/*'
        ]
        notDataActions: []
      }
    ]
  }
}

resource keyvault 'Microsoft.KeyVault/vaults@2023-07-01' = {
  name: 'kv-contoso${resourceToken}'
  location: location
  properties: {
    sku: {
      family: 'A'
      name: 'standard'
    }
    tenantId: subscription().tenantId
    enabledForDeployment: false
    enableSoftDelete: true
    publicNetworkAccess: 'Enabled'
    accessPolicies: []
  }
}

resource analytics 'Microsoft.OperationalInsights/workspaces@2021-12-01-preview' = {
  name: workspaces_apws_contosochatsfai362802272292_name
  location: location
  properties: {
    sku: {
      name: 'PerGB2018'
    }
    retentionInDays: 30
    features: {
      enableLogAccessUsingOnlyResourcePermissions: true
    }
    workspaceCapping: {
      dailyQuotaGb: -1
    }
    publicNetworkAccessForIngestion: 'Enabled'
    publicNetworkAccessForQuery: 'Enabled'
  }
}

resource search 'Microsoft.Search/searchServices@2023-11-01' = {
  name: 'search-contoso${resourceToken}'
  location: searchLocation
  sku: {
    name: 'standard'
  }
  properties: {
    replicaCount: 1
    partitionCount: 1
    hostingMode: 'default'
    publicNetworkAccess: 'enabled'
    networkRuleSet: {
      ipRules: []
    }
    encryptionWithCmk: {
      enforcement: 'Unspecified'
    }
    disableLocalAuth: false
    authOptions: {
      apiKeyOnly: {}
    }
    semanticSearch: 'free'
  }
}

resource storage 'Microsoft.Storage/storageAccounts@2023-01-01' = {
  name: 'stcontoso${resourceToken}'
  location: location
  sku: {
    name: 'Standard_LRS'
  }
  kind: 'StorageV2'
  properties: {
    allowCrossTenantReplication: false
    minimumTlsVersion: 'TLS1_2'
    allowBlobPublicAccess: false
    networkAcls: {
      bypass: 'AzureServices'
      virtualNetworkRules: []
      ipRules: []
      defaultAction: 'Allow'
    }
    supportsHttpsTrafficOnly: true
    encryption: {
      services: {
        file: {
          keyType: 'Account'
          enabled: true
        }
        blob: {
          keyType: 'Account'
          enabled: true
        }
      }
      keySource: 'Microsoft.Storage'
    }
    accessTier: 'Hot'
  }
}


resource appinsights 'microsoft.insights/components@2020-02-02' = {
  name: 'appi-contoso${resourceToken}'
  location: location
  kind: 'web'
  properties: {
    Application_Type: 'web'
    RetentionInDays: 90
    WorkspaceResourceId: analytics.id
    IngestionMode: 'LogAnalytics'
    publicNetworkAccessForIngestion: 'Enabled'
    publicNetworkAccessForQuery: 'Enabled'
  }
}

resource cosmosConnection 'Microsoft.MachineLearningServices/workspaces/connections@2023-10-01' = {
  parent: mlProject
  name: 'contoso-cosmos'
  properties: {
    category: 'CustomKeys'
    target: '_'
    authType: 'CustomKeys'
    credentials: {
      keys: {
        key: cosmos.listKeys().primaryMasterKey
        }
    }
    metadata: {
      endpoint: cosmos.properties.documentEndpoint
      databaseId: 'contoso-outdoor'
      containerId: 'customers'
      'azureml.flow.connection_type': 'Custom'
      'azureml.flow.module': 'promptflow.connections'

    }
  }
}

resource storageAccounts_stcontosocha735868071044_name_default 'Microsoft.Storage/storageAccounts/blobServices@2023-01-01' = {
  parent: storage
  name: 'default'
  properties: {
    cors: {
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
    }
    deleteRetentionPolicy: {
      allowPermanentDelete: false
      enabled: false
    }
  }
}

resource Microsoft_Storage_storageAccounts_fileServices_storageAccounts_stcontosocha735868071044_name_default 'Microsoft.Storage/storageAccounts/fileServices@2023-01-01' = {
  parent: storage
  name: 'default'
  properties: {
    protocolSettings: {
      smb: {}
    }
    cors: {
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
    }
    shareDeleteRetentionPolicy: {
      enabled: true
      days: 7
    }
  }
}

resource Microsoft_Storage_storageAccounts_queueServices_storageAccounts_stcontosocha735868071044_name_default 'Microsoft.Storage/storageAccounts/queueServices@2023-01-01' = {
  parent: storage
  name: 'default'
  properties: {
    cors: {
      corsRules: []
    }
  }
}

resource Microsoft_Storage_storageAccounts_tableServices_storageAccounts_stcontosocha735868071044_name_default 'Microsoft.Storage/storageAccounts/tableServices@2023-01-01' = {
  parent: storage
  name: 'default'
  properties: {
    cors: {
      corsRules: []
    }
  }
}

resource databaseAccounts_contoso_chat_sf_cosmos_name_contoso_outdoor_customers 'Microsoft.DocumentDB/databaseAccounts/sqlDatabases/containers@2023-09-15' = {
  parent: databaseAccounts_contoso_chat_sf_cosmos_name_contoso_outdoor
  name: 'customers'
  properties: {
    resource: {
      id: 'customers'
      indexingPolicy: {
        indexingMode: 'consistent'
        automatic: true
        includedPaths: [
          {
            path: '/*'
          }
        ]
        excludedPaths: [
          {
            path: '/"_etag"/?'
          }
        ]
      }
      partitionKey: {
        paths: [
          '/id'
        ]
        kind: 'Hash'
        version: 2
      }
      conflictResolutionPolicy: {
        mode: 'LastWriterWins'
        conflictResolutionPath: '/_ts'
      }
    }
  }
}

// In ai.azure.com: Azure AI Resource
resource mlHub 'Microsoft.MachineLearningServices/workspaces@2023-08-01-preview' = {
  name: workspaces_contoso_chat_sf_ai_name
  location: location
  sku: {
    name: 'Basic'
    tier: 'Basic'
  }
  kind: 'Hub' 
  identity: {
    type: 'SystemAssigned'
  }
  properties: {
    friendlyName: workspaces_contoso_chat_sf_ai_name
    storageAccount: storage.id
    keyVault: keyvault.id
    applicationInsights: appinsights.id
    hbiWorkspace: false
    managedNetwork: {
      isolationMode: 'Disabled'
    }
    v1LegacyMode: false
    containerRegistry: containerRegistry.id
    publicNetworkAccess: 'Enabled'
    discoveryUrl: 'https://${location}.api.azureml.ms/discovery'
  }

  resource openaiDefaultEndpoint 'endpoints' = {
    name: 'Azure.OpenAI'
    properties: {
      name: 'Azure.OpenAI'
      endpointType: 'Azure.OpenAI'
      associatedResourceId: openai.id
    }
  }

  resource contentSafetyDefaultEndpoint 'endpoints' = {
    name: 'Azure.ContentSafety'
    properties: {
      name: 'Azure.ContentSafety'
      endpointType: 'Azure.ContentSafety'
      associatedResourceId: openai.id
    }
  }

  resource openaiConnection 'connections' = {
    name: 'aoai-connection'
    properties: {
      category: 'AzureOpenAI'
      target: openaiEndpoint
      authType: 'ApiKey'
      metadata: {
          ApiVersion: '2023-07-01-preview'
          ApiType: 'azure'
          ResourceId: openai.id
      }
      credentials: {
        key: openai.listKeys().key1
      }
    }
  }

  resource searchConnection 'connections' = {
    name: 'contoso-search'
    properties: {
      category: 'CognitiveSearch'
      target: 'https://${search.name}.search.windows.net/'
      authType: 'ApiKey'
      credentials: {
        key: search.listAdminKeys().primaryKey
      }
    }
  }
}

// In ai.azure.com: Azure AI Project
resource mlProject 'Microsoft.MachineLearningServices/workspaces@2023-10-01' = {
  name: workspaces_contoso_chat_sf_aiproj_name
  location: location
  sku: {
    name: 'Basic'
    tier: 'Basic'
  }
  kind: 'Project'
  identity: {
    type: 'SystemAssigned'
  }
  properties: {
    friendlyName: workspaces_contoso_chat_sf_aiproj_name
    hbiWorkspace: false
    v1LegacyMode: false
    publicNetworkAccess: 'Enabled'
    discoveryUrl: 'https://${location}.api.azureml.ms/discovery'
    // most properties are not allowed for a project workspace: "Project workspace shouldn't define ..."
    hubResourceId: mlHub.id
  }
}

// output the names of the resources
output openai_name string = openai.name
output cosmos_name string = cosmos.name
output search_name string = search.name
output mlhub_name string = mlHub.name
output mlproject_name string = mlProject.name

output openai_endpoint string = openaiEndpoint
output cosmos_endpoint string = cosmos.properties.documentEndpoint
output search_endpoint string = 'https://${search.name}.search.windows.net/'
