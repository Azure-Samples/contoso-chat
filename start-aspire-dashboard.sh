#!/bin/bash

# Exit immediately if a command exits with a non-zero status
set -e

# Start the Aspire Dashboard.
docker run --rm -it -p 18888:18888 -p 4317:18889 -d --name aspire-dashboard mcr.microsoft.com/dotnet/aspire-dashboard:8.1.0

# Wait for the Aspire Dashboard to start.
sleep 7 

# Get the last 15 lines of the Aspire Dashboard logs.
docker logs --tail 15 aspire-dashboard

# Prompt the user to copy the token from the logs.
echo "Copy the token from the logs above."

# Wait for the user to confirm that they have copied the token
read -p "Press enter to continue and launch the Aspire Dashboard in the default browser."

# Open the Aspire Dashboard in the default browser.
xdg-open http://localhost:18888