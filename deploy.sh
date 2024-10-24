#!/bin/bash
de
set -a
source .env
set +a

# Build environment variables string for az containerapp update
ENV_VARS=""
while IFS= read -r line; do
  if [[ ! "$line" =~ ^# && "$line" =~ = ]]; then
    varname=$(echo "$line" | cut -d '=' -f 1)
    ENV_VARS+="$varname=${!varname},"
  fi
done < .env

# Remove trailing comma
ENV_VARS=${ENV_VARS%,}

# print the environment variables

echo "Environment variables: $ENV_VARS"


az containerapp update --subscription ${AZURE_SUBSCRIPTION_ID} --name ${SERVICE_ACA_NAME} --resource-group ${AZURE_RESOURCE_GROUP} --set-env-vars $ENV_VARS

