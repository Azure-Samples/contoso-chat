
import { type NextRequest } from "next/server";
const api_endpoint = process.env.VISUAL_ENDPOINT!;
const api_key = process.env.VISUAL_KEY!;

export async function POST(req: NextRequest) {
  const request_body = await req.json();

  const headers = {
    "Content-Type": "application/json",
    Authorization: "Bearer " + api_key,
  };

  const response = await fetch(api_endpoint, {
    method: "POST",
    headers: headers,
    body: JSON.stringify(request_body),
  });

  const data = await response.json();

  return Response.json(data);
}
