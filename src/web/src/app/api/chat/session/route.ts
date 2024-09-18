import { type NextRequest } from "next/server";
const api_endpoint = process.env.CONTOSO_CHAT_API_ENDPOINT!;


export async function POST(req: NextRequest) {
    const headers = {
        "Content-Type": "application/json",
        "Access-Control-Allow-Origin": "localhost:8000"
    };

    const response = await fetch(`${api_endpoint}/api/clear_session`, {
        method: "POST",
        headers: headers,
    });

    if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
    }
    const data = await response.json();

    return Response.json(data);

}
