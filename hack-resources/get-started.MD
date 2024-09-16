# MS Hackathon 2024


## Set up local environment

1. Clone the repository to your local machine and create a your new working branch with "alias/feature".
1. Open the project in VS Code and reopen the project in dev container. VS Code will ask for it.
1. Rename the file `.env.sample` to `.env` and update the values for the environment variables.
1. Run in VS Code Terminal 'pip install -r requirements.txt' this will install additional dependencies required for the project.
1. In the terminal, use the Azure CLI `az login` command to log into Azure.  Select the **ms-ignite-24** subscription.
1. Run the `setup-cosmos-rbac.sh` script from the **hack-resources** folder to set up the needed permissions for Cosmos DB.
1. Hit F5 to run the project in debug mode select `Python Debugger: FastAPI` as the configuration.
1. Open [api-test.http](api-test.http) and click on `Send Request` to test the API.
