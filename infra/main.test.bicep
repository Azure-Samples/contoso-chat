// This file is for doing static analysis and contains sensible defaults
// for the bicep analyser to minimise false-positives and provide the best results.

// This file is not intended to be used as a runtime configuration file.

targetScope = 'subscription'

param environmentName string = 'testing'
param location string = 'westus2'

module main 'main.bicep' = {
  name: 'main'
  params: {
    environmentName: environmentName
    location: location
  }
}
