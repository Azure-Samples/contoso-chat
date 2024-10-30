

// get hostname
const hostname = window.location.hostname;
const apiPort = 8000

function githubDevSubsPort(hostname: string, port: number): string {
    const regex = /-[0-9]{4,6}/gm;
    const subst = `-${port}`;
    let result = hostname.replace(regex, subst);
    if (!result.startsWith("https://")) {
        result = "https://"+ result;
    }
    return result;    
}

const endpoint = 
    // @ts-expect-error
    window['endpoint'] ? window['endpoint']
    : (hostname === 'localhost' || hostname === '127.0.0.1')
    ? `http://localhost:${apiPort}`
    : hostname.endsWith('github.dev') 
    ? `${githubDevSubsPort(hostname, apiPort)}/`
    : "api/article";

export { endpoint };