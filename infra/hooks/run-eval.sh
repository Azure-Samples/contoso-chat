echo "Running evaluation notebooks after post-provisioning"

echo 'Installing dependencies from "requirements.txt"'
python -m pip install -r requirements.txt

# Install ipythong and ipykernel
python -m pip install ipython ipykernel

# Configure the IPython kernel
ipython kernel install --name=python3 --user

# Verify kernelspec list isn't empty
jupyter kernelspec list

# Run juypter notebooks
jupyter nbconvert --execute --to python --ExecutePreprocessor.timeout=-1 evaluations/evaluate-chat-flow-sdk.ipynb

jupyter nbconvert --execute --to python --ExecutePreprocessor.timeout=-1 evaluations/evaluate-chat-flow-custom-no-sdk.ipynb

jupyter nbconvert --execute --to python --ExecutePreprocessor.timeout=-1 evaluations/evaluate-chat-flow-custom.ipynb
