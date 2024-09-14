# MS Hackathon 2024


## Set up local environment

1. Clone the repository to your local machine and create a your new working branch with "alias/feature"
2. Open the project in VS Code and reopen the project in dev container. VS Code will ask for it 
3. Copy the .env file to the root of the project
4. Run in VS Code Terminal 'pip install -r requirements.txt' this will install additional dependencies required for the project
5. Az login in the terminal and select the subscription(ms-ignite-24)
6. Add your account to cosmos DB built in role <br>
    `az cosmosdb sql role assignment create --account-name cosmos-contoso-q5ezmhyg2mjqw --resource-group rg-contosochat --scope "/" --principal-id [USER_PRINCIPAL-ID] --role-definition-id 00000000-0000-0000-0000-000000000001 --subscription [SUBCRIPTION_ID]` 

    `az cosmosdb sql role assignment create --account-name cosmos-contoso-q5ezmhyg2mjqw --resource-group rg-contosochat --scope "/" --principal-id [USER_PRINCIPAL-ID] --role-definition-id 00000000-0000-0000-0000-000000000002 --subscription [SUBCRIPTION_ID]` 

7. Hit F5 to run the project in debug mode select `Python Debugger: FastAPI` as the configuration
8. Open [api-test.http](api-test.http) and click on `Send Request` to test the API
