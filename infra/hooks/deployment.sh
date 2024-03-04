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

acrRepository="promptflow-contoso-chat"

# Execute the command and parse versions directly, storing the highest version number
max_version=0
for version in $(az ml environment list -n $acrRepository --resource-group $AZURE_RESOURCE_GROUP -w $mlproject_name | jq -r '.[].version'); do
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
az ml environment create --file deployment/docker/environment.yml --resource-group $AZURE_RESOURCE_GROUP --workspace-name $mlproject_name --registry-name $AZURE_CONTAINER_REGISTRY_NAME --version $new_version

#get registry name
#acrName=$(az acr list --resource-group $AZURE_RESOURCE_GROUP --query "[0].name" -o tsv)
# get repository name
# get envirnment image name from acr
image_tag=$(az acr repository show-tags --name $AZURE_CONTAINER_REGISTRY_NAME --repository $acrRepository --query "[0]" -o tsv)
#concatenate the image name
image_name=$AZURE_CONTAINER_REGISTRY_NAME.azurecr.io/$acrRepository:$image_tag

# register promptflow as model
echo "Registering PromptFlow as a model in Azure ML..."
az ml model create --file deployment/chat-model.yaml  -g $AZURE_RESOURCE_GROUP -w $mlproject_name

# Deploy prompt flow
echo "Deploying PromptFlow to Azure ML..."
az ml online-endpoint create --file deployment/chat-endpoint.yaml -n $endpointName -g $AZURE_RESOURCE_GROUP -w $mlproject_name

# Setup deployment
echo "Setting up deployment..."
az ml online-deployment create --file deployment/chat-deployment.yaml --name $deploymentName --endpoint-name $endpointName --all-traffic -g $AZURE_RESOURCE_GROUP -w $mlproject_name --set environment.image=$image_name
az ml online-endpoint show -n $endpointName -g $AZURE_RESOURCE_GROUP -w $mlproject_name
az ml online-deployment get-logs --name $deploymentName --endpoint-name $endpointName -g $AZURE_RESOURCE_GROUP -w $mlproject_name

# Read endpoint principal
#echo "Reading endpoint principal..."
#az ml online-endpoint show -n $endpointName -g $AZURE_RESOURCE_GROUP -w $mlproject_name > endpoint.json
#jq -r '.identity.principal_id' endpoint.json > principal.txt
#echo "Principal is: $(cat principal.txt)"

#Assign Permission to Endpoint Principal
#echo "Assigning permissions to Principal..."
#az role assignment create --assignee $(cat principal.txt) --role "AzureML Data Scientist" --scope "/subscriptions/$subscription_id/resourcegroups/$AZURE_RESOURCE_GROUP/providers/Microsoft.MachineLearningServices/workspaces/$mlproject_name"
#az role assignment create --assignee $(cat principal.txt) --role "Azure Machine Learning Workspace Connection Secrets Reader" --scope "/subscriptions/$subscription_id/resourcegroups/$AZURE_RESOURCE_GROUP/providers/Microsoft.MachineLearningServices/workspaces/$mlproject_name/onlineEndpoints/$endpointName"
# Get keyValueName from Azure ML
#keyValueName=$(az ml online-endpoint show -n $endpointName -g $AZURE_RESOURCE_GROUP -w $mlproject_name --query "identity.principal_id" -o tsv)          
#echo "assigning permissions to Principal to Key vault.."
#az keyvault set-policy --name $keyValueName --resource-group $AZURE_RESOURCE_GROUP --object-id 