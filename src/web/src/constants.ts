// get hostname from env file variable name is WEBAPP_ACA_URI
//create a function to get the endpoint and set the port or return localhost
const endpoint = (): string => {
    //TODO: Fix this    
    const apihostname = process.env.API_SERVICE_ACA_URI!;
    console.log(process.env.API_SERVICE_ACA_URI);
    return apihostname;
};

export { endpoint };