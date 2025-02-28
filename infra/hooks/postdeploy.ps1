#!/usr/bin/env pwsh

Write-Host "--- ☑️ 1. Starting postdeploy ---"

# -----------------------------------------------------------
# Setup to run notebooks
python -m pip install -r ./src/api/requirements.txt > $null
Write-Host "---- ✅ 3. Installed required dependencies ---"

# -----------------------------------------------------------
# Run notebooks to populate data
jupyter nbconvert --execute --to python --ExecutePreprocessor.timeout=-1 data/customer_info/create-cosmos-db.ipynb > $null
jupyter nbconvert --execute --to python --ExecutePreprocessor.timeout=-1 data/product_info/create-azure-search.ipynb > $null
Write-Host "---- ✅ 4. Completed populating data ---"

# -----------------------------------------------------------
Write-Host "--- ✅ Completed postdeploy ---"