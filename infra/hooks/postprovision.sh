#!/bin/bash

echo  "Building contosochatapi:latest..."
az acr build --subscription ${AZURE_SUBSCRIPTION_ID} --registry ${AZURE_CONTAINER_REGISTRY_NAME} --image contosochatapi:latest ./src/api/
image_name="${AZURE_CONTAINER_REGISTRY_NAME}.azurecr.io/contosochatapi:latest"
az containerapp update --subscription ${AZURE_SUBSCRIPTION_ID} --name ${SERVICE_ACA_NAME} --resource-group ${AZURE_RESOURCE_GROUP} --image ${image_name}
az containerapp ingress update --subscription ${AZURE_SUBSCRIPTION_ID} --name ${SERVICE_ACA_NAME} --resource-group ${AZURE_RESOURCE_GROUP} --target-port 80


# Retrieve service names, resource group name, and other values from environment variables
resourceGroupName=$AZURE_RESOURCE_GROUP
searchService=$AZURE_SEARCH_NAME
openAiService=$AZURE_OPENAI_NAME
cosmosService=$AZURE_COSMOS_NAME
subscriptionId=$AZURE_SUBSCRIPTION_ID

# Ensure all required environment variables are set
if [ -z "$resourceGroupName" ] || [ -z "$searchService" ] || [ -z "$openAiService" ] || [ -z "$cosmosService" ] || [ -z "$subscriptionId" ]; then
    echo "One or more required environment variables are not set."
    echo "Ensure that AZURE_RESOURCE_GROUP, AZURE_SEARCH_NAME, AZURE_OPENAI_NAME, AZURE_COSMOS_NAME, AZURE_SUBSCRIPTION_ID are set."
    exit 1
fi

# Set additional environment variables expected by app
# TODO: Standardize these and remove need for setting here
azd env set AZURE_OPENAI_API_VERSION 2023-03-15-preview
azd env set AZURE_OPENAI_CHAT_DEPLOYMENT gpt-35-turbo
azd env set AZURE_SEARCH_ENDPOINT $AZURE_SEARCH_ENDPOINT
azd env set AZURE_TRACING_GEN_AI_CONTENT_RECORDING_ENABLED false
azd env set OTEL_EXPORTER_OTLP_ENDPOINT http://localhost:4317

# Output environment variables to .env file using azd env get-values
azd env get-values >.env

echo "--- ✅ | 1. Post-provisioning - env configured ---"

# Setup to run notebooks
echo 'Installing dependencies from "requirements.txt"'
python -m pip install -r ./src/api/requirements.txt > /dev/null
python -m pip install ipython ipykernel > /dev/null      # Install ipython and ipykernel
ipython kernel install --name=python3 --user > /dev/null # Configure the IPython kernel
jupyter kernelspec list > /dev/null                      # Verify kernelspec list isn't empty
echo "--- ✅ | 2. Post-provisioning - ready execute notebooks ---"

echo "Populating data ...."
jupyter nbconvert --execute --to python --ExecutePreprocessor.timeout=-1 data/customer_info/create-cosmos-db.ipynb > /dev/null
jupyter nbconvert --execute --to python --ExecutePreprocessor.timeout=-1 data/product_info/create-azure-search.ipynb > /dev/null
echo "--- ✅ | 3. Post-provisioning - populated data ---"

#echo "Running evaluations ...."
#jupyter nbconvert --execute --to python --ExecutePreprocessor.timeout=-1 evaluations/evaluate-chat-flow-sdk.ipynb
#jupyter nbconvert --execute --to python --ExecutePreprocessor.timeout=-1 evaluations/evaluate-chat-flow-custom-no-sdk.ipynb
#jupyter nbconvert --execute --to python --ExecutePreprocessor.timeout=-1 evaluations/evaluate-chat-flow-custom.ipynb
#echo "--- ✅ | 4. Post-provisioning - ran evaluations ---"


echo  "Building contosochatweb:latest..."
echo -e "\e[31mWarning: Building Frotend Image take a while, please be patient\e[0m"
echo -e "\e[33Alternatively you can skip this step and build it manually\e[0m"

az acr build --subscription ${AZURE_SUBSCRIPTION_ID} --registry ${AZURE_CONTAINER_REGISTRY_NAME} --image contosochatweb:latest ./src/web/
web_image_name="${AZURE_CONTAINER_REGISTRY_NAME}.azurecr.io/contosochatweb:latest"
az containerapp update --subscription ${AZURE_SUBSCRIPTION_ID} --name ${WEBAPP_ACA_NAME} --resource-group ${AZURE_RESOURCE_GROUP} --image ${web_image_name}
az containerapp ingress update --subscription ${AZURE_SUBSCRIPTION_ID} --name ${WEBAPP_ACA_NAME} --resource-group ${AZURE_RESOURCE_GROUP} --target-port 3000

