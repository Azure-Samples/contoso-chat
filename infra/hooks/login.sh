#!/bin/bash

# Check if the script is running in a Codespace Browser and ask user to open in VS Code Desktop if it is
# Initialize IS_BROWSER variable to false
IS_BROWSER=false

# Check if 'code' command exists
if command -v code &> /dev/null
then
    # Run 'code -s' and capture the output
    output=$(code -s 2>&1)
    
    # Check if the output indicates it's running in a browser
    if [[ "$output" == *"The --status argument is not yet supported in browsers."* ]]; then
        IS_BROWSER=true
    fi
fi

# Check if IS_BROWSER is true and CODESPACE_NAME is set
if [ "$IS_BROWSER" = true ] && [ -n "$CODESPACE_NAME" ]; then
    # Construct the URL with CODESPACE_NAME
    url="https://github.com/codespaces/$CODESPACE_NAME?editor=vscode"
    
    # Display the security policy explanation message and the URL
    echo "Due to security policies that prevent authenticating with Azure and Microsoft accounts directly from the browser, you are required to open this project in Visual Studio Code Desktop. This restriction is in place to ensure the security of your account details and to comply with best practices for authentication workflows. Please use the following link to proceed with opening your Codespace in Visual Studio Code Desktop:"
    echo "$url"
    exit
fi

# AZD LOGIN

echo "Checking Azure Developer CLI (azd) login status..."

# Check if the user is logged in to Azure
login_status=$(azd auth login --check-status)

# Check if the user is not logged in
if [[ "$login_status" == *"Not logged in"* ]]; then
  echo "Not logged in to the Azure Developer CLI, initiating login process..."
  # Command to log in to Azure
  azd auth login
else
  echo "Already logged in to Azure Developer CLI."
fi

echo "Checking Azure (az) CLI login status..."

# AZ LOGIN
EXPIRED_TOKEN=$(az ad signed-in-user show --query 'id' -o tsv 2>/dev/null || true)

if [[ -z "$EXPIRED_TOKEN" ]]; then
    echo "Not logged in to Azure, initiating login process..."
    az login --scope https://graph.microsoft.com/.default -o none
else
    echo "Already logged in to the Azure (az) CLI."
fi

if [[ -z "${AZURE_SUBSCRIPTION_ID:-}" ]]; then
    ACCOUNT=$(az account show --query '[id,name]')
    echo "No Azure subscription ID set."
    echo "You can set the \`AZURE_SUBSCRIPTION_ID\` environment variable with \`azd env set AZURE_SUBSCRIPTION_ID\`."
    echo "Current subscription:"
    echo $ACCOUNT
    
    read -r -p "Do you want to use the above subscription? (Y/n) " response
    response=${response:-Y}
    case "$response" in
        [yY][eE][sS]|[yY]) 
            echo "Using the selected subscription."
            ;;
        *)
            echo "Listing available subscriptions..."
            SUBSCRIPTIONS=$(az account list --query 'sort_by([], &name)' --output json)
            echo "Available subscriptions:"
            echo "$SUBSCRIPTIONS" | jq -r '.[] | [.name, .id] | @tsv' | column -t -s $'\t'
            read -r -p "Enter the name or ID of the subscription you want to use: " subscription_input
            AZURE_SUBSCRIPTION_ID=$(echo "$SUBSCRIPTIONS" | jq -r --arg input "$subscription_input" '.[] | select(.name==$input or .id==$input) | .id')
            if [[ -n "$AZURE_SUBSCRIPTION_ID" ]]; then
                echo "Setting active subscription to: $AZURE_SUBSCRIPTION_ID"
                az account set -s $AZURE_SUBSCRIPTION_ID
            else
                echo "Subscription not found. Please enter a valid subscription name or ID."
                exit 1
            fi
            ;;
        *)
            echo "Use the \`az account set\` command to set the subscription you'd like to use and re-run this script."
            exit 0
            ;;
    esac
else
    echo "Azure subscription ID is already set."
    az account set -s $AZURE_SUBSCRIPTION_ID
fi