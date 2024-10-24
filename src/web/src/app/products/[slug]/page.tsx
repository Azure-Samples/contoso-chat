import Block from "@/components/block";
import clsx from "clsx";
import Image from "next/image";
import { Product } from "@/lib/types";
import { promises as fs } from "fs";
import { marked } from "marked";
import Header from "@/components/header";

// This function gets called at build time
export async function generateStaticParams() {
  const file = await fs.readFile(
    process.cwd() + "/public/products.json",
    "utf8"
  );

  // Parsing JSON data
  const products = JSON.parse(file) as Product[];
  // Generating paths from data
  const paths = products.map((product) => ({ slug: product.slug }));
  return paths;
}

async function getData(slug: string): Promise<Product> {
  const file = await fs.readFile(
    process.cwd() + "/public/products.json",
    "utf8"
  );
  const data: Product[] = JSON.parse(file);
  const product = data.findIndex((p) => p.slug === slug);
  return data[product];
}

async function getManual(manual: string): Promise<string> {
  const file = await fs.readFile(process.cwd() + `/public/${manual}`, "utf8");
  return file;
}

function getRange(header1:string, header2:string, markdown: string[]): string {
  const start = markdown.findIndex((m) => m.startsWith(header1));
  const end = header2.length > 0 ? markdown.findIndex((m) => m.startsWith(header2)) : markdown.length - 1;
  const range = markdown.slice(start, end);
  return marked.parse(range.join("\n"));
}

export default async function Page({
  params,
  searchParams,
}: {
  params: { slug: string };
  searchParams?: { [key: string]: string | string[] | undefined };
}) {
  const product = await getData(params.slug);
  const manual = await getManual(product.manual);
  const mitems = manual.split("\n");

  const sections = [
    {
      start: "## Features",
      end: "## Technical",
    },
    {
      start: "## Reviews",
      end: "## FAQ",
    },
    {
      start: "## FAQ",
      end: "",
    },
    {
      start: "## Return",
      end: "## Reviews",
    },
    {
      start: "## Caution",
      end: "## Warranty",
    },
    {
      start: "## Technical",
      end: "## User Guide",
    },

    {
      start: "## Warranty",
      end: "## Return",
    },
    {
      start: "## User Guide",
      end: "## Caution",
    },
  ];

  const getSection = (idx: number) => {
    const section = sections[idx];
    const range = getRange(section.start, section.end, mitems);
    return range;
  };

  const extraclasses =
    "[&_li]:ml-8 [&_ol]:list-decimal [&_ul]:list-disc [&_h2]:text-2xl [&_h2]:font-extrabold [&_h2]:pt-3 [&_h2]:pb-3" +
    "[&_h3]:text-xl [&_h3]:font-bold [&_h3]:pt-3 [&_h3]:pb-3" +
    "[&_h4]:text-lg [&_h4]:font-semibold [&_h4]:pt-3 [&_h4]:pb-3" +
    "[&_ol]:list-decimal [&_ol]:list-outside [&_ul]:list-outside";
  return (
    <>
      <Header params={params} searchParams={searchParams} />
      <Block innerClassName="pt-6 pb-6">
        <div className="text-6xl pb-5 pt-8 subpixel-antialiased font-serif ">
          {product.name}
        </div>
        <div
          className="first-line:uppercase first-line:tracking-widest
                  first-letter:text-8xl first-letter:font-bold first-letter:text-slate-900
                  first-letter:mr-3 first-letter:float-left"
        >
          {product.description}
        </div>
      </Block>
      {product.images.map((image, i) => (
        <Block
          key={i}
          outerClassName={clsx(i % 2 == 0 ? "bg-zinc-100" : "bg-inherit")}
          innerClassName={clsx(
            "p-6 flex items-start",
            i % 2 == 1 ? "flex-row-reverse" : "flex-row"
          )}
        >
          <Image
            src={image}
            alt={product.name}
            width={550}
            height={550}
            className="rounded-3xl mr-6"
          />
          <div
            className={clsx(
              "text-left mt-2 grow text-lg",
              extraclasses,
              i % 2 == 1 ? "mr-8" : "ml-8"
            )}
            dangerouslySetInnerHTML={{ __html: getSection(i) }}
          />
        </Block>
      ))}
      <Block innerClassName={clsx("p-4 flex items-start")}>
        <div
          className={clsx("text-left mt-2 grow", extraclasses)}
          dangerouslySetInnerHTML={{ __html: getSection(7) }}
        />
      </Block>
      <Block
        outerClassName="bg-zinc-100"
        innerClassName={clsx("p-6 flex items-start")}
      >
        <div
          className={clsx("text-left mt-2 grow pr-6", extraclasses)}
          dangerouslySetInnerHTML={{ __html: getSection(6) }}
        />
        <div
          className={clsx("text-left mt-2 grow pl-6", extraclasses)}
          dangerouslySetInnerHTML={{ __html: getSection(5) }}
        />
      </Block>
    </>
  );
}
