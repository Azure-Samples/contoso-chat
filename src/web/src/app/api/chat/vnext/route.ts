
import { log } from "console";
import { type NextRequest } from "next/server";
const api_endpoint = process.env.CONTOSO_CHAT_API_ENDPOINT!;

// TODO: Give this a better name than 'vnext'.


export async function POST(req: NextRequest) {
    const request_body = await req.json();

    // TODO: What is the authentication mechanism?
    const headers = {
        "Content-Type": "application/json"
        //,
        // Authorization: "Bearer " + api_key,
    };

    log("Request body: ", request_body);
    log("Request body jsonify: ", JSON.stringify(request_body));

    const response = await fetch(`${api_endpoint}/api/create_response`, {
        method: "POST",
        headers: headers,
        body: JSON.stringify(request_body),
    });

    if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
    }
    const data = await response.json();

    data.responseId = response.headers.get('gen_ai.response.id');
    
    return Response.json(data);

}
