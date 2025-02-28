#!/bin/bash

echo "--- ☑️ Starting postpdeploy ---"

# -----------------------------------------------------------
# Setup to run notebooks
python -m pip install -r ./src/api/requirements.txt > /dev/null
python -m pip install ipython ipykernel > /dev/null      # Install ipython and ipykernel
ipython kernel install --name=python3 --user > /dev/null # Configure the IPython kernel
jupyter kernelspec list > /dev/null                      # Verify kernelspec list isn't empty
echo "---- ✅ 3. Installed required dependencies ---"

# -----------------------------------------------------------
# Run notebooks to populate data
echo "Populating data ...."
jupyter nbconvert --execute --to python --ExecutePreprocessor.timeout=-1 data/customer_info/create-cosmos-db.ipynb > /dev/null
jupyter nbconvert --execute --to python --ExecutePreprocessor.timeout=-1 data/product_info/create-azure-search.ipynb > /dev/null
echo "---- ✅ 4. Completed populating data ---"

echo "--- ✅ Completed postdeploy ---"