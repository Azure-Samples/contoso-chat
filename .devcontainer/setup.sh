#!/bin/bash

# Exit immediately if a command exits with a non-zero status
set -e

# Install requirements for the Contoso Chat API
echo "Installing requirements for the Contoso Chat API"
pip install -r ./src/api/requirements.txt

# Install NPM modules for Contoso Web UI
echo "Installing NPM modules for Contoso Web UI"
pushd ./src/web
npm install
popd