import { type NextRequest } from "next/server";
import { cookies } from 'next/headers'
import { v4 } from "uuid";


export async function DELETE(req: NextRequest) {
    cookies().delete('sessionid')
    const data = {message: "success"}
    return Response.json(data);
}

export async function POST(req: NextRequest) {
    cookies().set("sessionid", v4())
    const data = {message: "success"}
    return Response.json(data);
}
