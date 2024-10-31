$ErrorActionPreference = "Stop"
# Start the Aspire Dashboard
docker run --rm -it -p 18888:18888 -p 4317:18889 -d --name aspire-dashboard mcr.microsoft.com/dotnet/aspire-dashboard:8.1.0
# Wait for the Aspire Dashboard to start
Start-Sleep -Seconds 7
# Get the last 15 lines of the Aspire Dashboard logs
docker logs --tail 15 aspire-dashboard
# Prompt the user to copy the token from the logs
Write-Host "Copy the token from the logs above."
# Wait for the user to confirm that they have copied the token
Read-Host -Prompt "Press Enter to continue and launch the Aspire Dashboard in the default browser"
# Open the Aspire Dashboard in the default browser
Start-Process "http://localhost:18888"