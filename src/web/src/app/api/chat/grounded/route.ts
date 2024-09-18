import { ChatTurn, Citation, Product } from "@/lib/types";
import { OpenAIStream, StreamingTextResponse } from "ai";
import { OpenAIClient, AzureKeyCredential } from "@azure/openai";
import { type NextRequest } from "next/server";
import { ChatMessage } from "@azure/openai/rest";
import { promises as fs } from "fs";

const searchendpoint = process.env.CONTOSO_SEARCH_ENDPOINT!;
const searchkey = process.env.CONTOSO_SEARCH_KEY!;
const aiservicesendpoint = process.env.CONTOSO_AISERVICES_ENDPOINT!;
const aiserviceskey = process.env.CONTOSO_AISERVICES_KEY!;

async function getData(): Promise<Product[]> {
  const file = await fs.readFile(
    process.cwd() + "/public/products.json",
    "utf8"
  );
  const data: Product[] = JSON.parse(file);
  return data;
}

export async function POST(request: NextRequest) {
  const messages: ChatMessage[] = await request.json();
  const deployment_id = "gpt-35-turbo";
  const grounded_uri = `${aiservicesendpoint}openai/deployments/${deployment_id}/extensions/chat/completions?api-version=2023-08-01-preview`;

  const headers = {
    "Content-Type": "application/json",
    "api-key": aiserviceskey,
  };

  const message_body = {
    dataSources: [
      {
        type: "AzureCognitiveSearch",
        parameters: {
          endpoint: searchendpoint,
          key: searchkey,
          indexName: "contoso-manuals-index",
          queryType: "vectorSimpleHybrid",
          fieldsMapping: {
            contentFieldsSeparator: "\n",
            contentFields: ["content"],
            filepathField: "filepath",
            titleField: "title",
            urlField: "url",
            vectorFields: ["contentVector"],
          },
          inScope: true,
          roleInformation:
            "You are an AI assistant for the Contoso Outdoors product information that helps people find information in the shortest amount of text possible. Be brief and concise in your response and include emojis.",
          embeddingDeploymentName: "text-embedding-ada-002",
          strictness: 3,
          topNDocuments: 5,
        },
      },
    ],
    messages: messages,
    deployment: deployment_id,
    temperature: 0,
    top_p: 1,
    max_tokens: 800,
    stream: false,
  };

  const response = await fetch(grounded_uri, {
    method: "POST",
    headers: headers,
    body: JSON.stringify(message_body),
  });

  const products = await getData();

  const data = await response.json();

  const returnMessage = data.choices[0].message;
  const context = JSON.parse(returnMessage.context.messages[0].content);

  const citationReplacement = (val: any, index: number): Citation => {
    const productId = parseInt(
      val.filepath.replace(".md", "").replace("product_info_", "")
    );
    const product = products.find((p) => p.id === productId)!;
    return {
      index: index + 1,
      productId: productId,
      slug: `/products/${product.slug}`,
      chunk: val.content,
      manual: product.manual,
      replace: `[doc${index + 1}]`,
    };
  };

  const citations: Citation[] = context.citations.map(citationReplacement);

  // links [doc0] => [0](/product/[slug])
  const message = citations.reduce((acc: string, val: Citation) => {
    const link = `[${val.index}](${val.slug})`;
    return acc.replaceAll(val.replace, link);
  }, returnMessage.content);

  return Response.json({
    message: message,
    citations: citations,
  });
}
