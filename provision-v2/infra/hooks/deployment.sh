#!/bin/sh

echo "Loading azd .env file from current environment..."

while IFS='=' read -r key value; do
    value=$(echo "$value" | sed 's/^"//' | sed 's/"$//')
    export "$key=$value"
done <<EOF
$(azd env get-values)
EOF

# create a random hash for the endpoint name all lowercase letters
endpointName="contoso-chat-$RANDOM"
# create a random hash for the deployment name
deploymentName="contoso-chat-$RANDOM"

az extension add -n ml -y

# Execute the command and parse versions directly, storing the highest version number
max_version=0
for version in $(az ml environment list --name $acrRepository --resource-group $AZURE_RESOURCE_GROUP --workspace-name $AZURE_MLPROJECT_NAME | jq -r '.[].version'); do
    if [ "$version" -gt "$max_version" ]; then
        max_version=$version
    fi
done

# Increment the highest version number
next_version=$((max_version + 1))

# Store the next version number in a variable
new_version=$next_version
echo "The next version number is: $new_version"


az acr login --name $AZURE_CONTAINER_REGISTRY_NAME
az ml environment create --file deployment/docker/environment.yml --resource-group $AZURE_RESOURCE_GROUP --workspace-name $AZURE_MLPROJECT_NAME --version $new_version

# Pause for 600 seconds to allow the environment to be created
echo "Waiting for environment to be created..."
sleep 600

#get registry first repository name as variable
acrRepository=$(az acr repository list --name $AZURE_CONTAINER_REGISTRY_NAME --output tsv --query "[0]")
# get repository name
# get envirnment image name from acr
image_tag=$(az acr repository show-tags --name $AZURE_CONTAINER_REGISTRY_NAME --repository $acrRepository --query "[0]" -o tsv)
#concatenate the image name
image_name=$AZURE_CONTAINER_REGISTRY_NAME.azurecr.io/$acrRepository:$image_tag

# register promptflow as model
echo "Registering PromptFlow as a model in Azure ML..."
az ml model create --file deployment/chat-model.yaml  -g $AZURE_RESOURCE_GROUP -w $AZURE_MLPROJECT_NAME

# Deploy prompt flow
echo "Deploying PromptFlow to Azure ML..."
az ml online-endpoint create --file deployment/chat-endpoint.yaml -n $endpointName -g $AZURE_RESOURCE_GROUP -w $AZURE_MLPROJECT_NAME

PRT_CONFIG_OVERRIDE=deployment.subscription_id=$AZURE_SUBSCRIPTION_ID,deployment.resource_group=$AZURE_RESOURCE_GROUP,deployment.workspace_name=$AZURE_MLPROJECT_NAME,deployment.endpoint_name=$endpointName,deployment.deployment_name=$deploymentName
sed -i "s/PRT_CONFIG_OVERRIDE:.*/PRT_CONFIG_OVERRIDE: $PRT_CONFIG_OVERRIDE/g" deployment/chat-deployment.yaml

# Setup deployment
echo "Setting up deployment..."
az ml online-deployment create --file deployment/chat-deployment.yaml --name $deploymentName --endpoint-name $endpointName --all-traffic -g $AZURE_RESOURCE_GROUP -w $AZURE_MLPROJECT_NAME --set environment.image=$image_name
az ml online-endpoint show -n $endpointName -g $AZURE_RESOURCE_GROUP -w $AZURE_MLPROJECT_NAME
az ml online-deployment get-logs --name $deploymentName --endpoint-name $endpointName -g $AZURE_RESOURCE_GROUP -w $AZURE_MLPROJECT_NAME

# Read endpoint principal

echo "Reading endpoint principal..."
principal_id=$(az ml online-endpoint show -n $endpointName -g $AZURE_RESOURCE_GROUP -w $AZURE_MLPROJECT_NAME --query "identity.principal_id" -o tsv)
echo "Principal is: $principal_id"
 
# Assign Permission to Endpoint Principal

echo "Assigning Data Scientist permissions to Principal..."
az role assignment create --assignee $principal_id --role "AzureML Data Scientist" --scope "subscriptions/$AZURE_SUBSCRIPTION_ID/resourcegroups/$AZURE_RESOURCE_GROUP/providers/Microsoft.MachineLearningServices/workspaces/$AZURE_MLPROJECT_NAME"
echo "Assigning permissions to Principal to Endpoint..."
az role assignment create --assignee $principal_id --role "Azure Machine Learning Workspace Connection Secrets Reader" --scope "subscriptions/$AZURE_SUBSCRIPTION_ID/resourcegroups/$AZURE_RESOURCE_GROUP/providers/Microsoft.MachineLearningServices/workspaces/$AZURE_MLPROJECT_NAME/onlineEndpoints/$endpointName"
 
# Get Key Vault name

echo "Getting keyValueName from Azure ML..."
keyValueName=$(az keyvault list --resource-group $AZURE_RESOURCE_GROUP --query "[0].name" -o tsv)
echo "Key Vault Name is: $keyValueName"
echo "Assigning permissions to Principal to Key Vault..."
az keyvault set-policy --name $keyValueName --resource-group $AZURE_RESOURCE_GROUP --object-id $principal_id --key-permissions get list --secret-permissions get list