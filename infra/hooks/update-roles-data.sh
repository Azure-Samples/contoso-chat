#!/bin/bash

echo "--- ✅ | 3. Post-provisioning - Updating access roles---"
set -e

# Output environment variables to .env file using azd env get-values
azd env get-values > .env

# Load variables from .env file
if [ -f .env ]; then
    source .env
else
    echo ".env file not found!"
    exit 1
fi

PRINCIPAL_ID=$(az ad signed-in-user show --query id -o tsv)

az role assignment create \
        --role "8ebe5a00-799e-43f5-93ac-243d3dce84a7" \
        --assignee-object-id "${PRINCIPAL_ID}" \
        --scope /subscriptions/"${AZURE_SUBSCRIPTION_ID}"/resourceGroups/"${AZURE_OPENAI_RESOURCE_GROUP}" \
        --assignee-principal-type 'User'

az role assignment create \
        --role "1407120a-92aa-4202-b7e9-c0e197c71c8f" \
        --assignee-object-id "${PRINCIPAL_ID}" \
        --scope /subscriptions/"${AZURE_SUBSCRIPTION_ID}"/resourceGroups/"${AZURE_OPENAI_RESOURCE_GROUP}" \
        --assignee-principal-type 'User'

az role assignment create \
        --role "8ebe5a00-799e-43f5-93ac-243d3dce84a7" \
        --assignee-object-id "${PRINCIPAL_ID}" \
        --scope /subscriptions/"${AZURE_SUBSCRIPTION_ID}"/resourceGroups/"${AZURE_OPENAI_RESOURCE_GROUP}" \
        --assignee-principal-type 'User'

az role assignment create \
        --role "5e0bd9bd-7b93-4f28-af87-19fc36ad61bd" \
        --assignee-object-id "${PRINCIPAL_ID}" \
        --scope /subscriptions/"${AZURE_SUBSCRIPTION_ID}"/resourceGroups/"${AZURE_OPENAI_RESOURCE_GROUP}" \
        --assignee-principal-type 'User'


# Already setup to run notebooks
echo "--- ✅ | 4. Post-provisioning - populating data---"
jupyter nbconvert --execute --to python --ExecutePreprocessor.timeout=-1 data/customer_info/create-cosmos-db.ipynb > /dev/null
jupyter nbconvert --execute --to python --ExecutePreprocessor.timeout=-1 data/product_info/create-azure-search.ipynb > /dev/null
echo "--- ✅ | PROVISIONING HOOKS COMPLETED ---"
