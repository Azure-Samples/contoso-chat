import Image from "next/image";
import Block from "@/components/block";
import { ProductGroup } from "@/lib/types";
import { promises as fs } from "fs";
import Header from "@/components/header";
import clsx from "clsx";

async function getData(): Promise<ProductGroup[]> {
  const file = await fs.readFile(
    process.cwd() + "/public/categories.json",
    "utf8"
  );
  const data: ProductGroup[] = JSON.parse(file);
  return data;
}

export default async function Home({
  params,
  searchParams,
}: {
  params: { slug: string };
  searchParams?: { [key: string]: string | string[] | undefined };
}) {
  const categories = await getData();

  return (
    <>
      <Header params={params} searchParams={searchParams} />
      <Block
        outerClassName="bg-blend-multiply bg-center bg-hero-image h-80 bg-neutral-600"
        innerClassName=""
      >
        <div className="text-zinc-100 pt-12 text-7xl font-black subpixel-antialiased">
          Contoso Outdoor Company
        </div>
        <div className="text-zinc-100 mt-4 text-2xl">
          Embrace Adventure with Contoso Outdoors - Your Ultimate Partner in
          Exploring the Unseen!
        </div>
        <div className="text-zinc-100 mt-2 text-lg w-2/3">
          Choose from a variety of products to help you explore the outdoors.
          From camping to hiking, we have you covered with the best gear and the
          best prices.
        </div>
      </Block>
      {/* Categories */}
      {categories.map((category, i) => (
        <Block
          key={i}
          innerClassName="p-8"
          outerClassName={clsx(i % 2 == 1 ? "bg-zinc-100" : "bg-inherit")}
        >
          <div className="text-5xl mb-3 font-semibold text-zinc-800">
            {category.name}
          </div>
          <div
            className="text-zinc-500 text-2xl first-line:uppercase first-line:tracking-widest
                  first-letter:text-6xl first-letter:font-bold first-letter:text-zinc-500
                  first-letter:mr-1 first-letter:float-left"
          >
            {category.description}
          </div>
          <div className="flex flex-row place-content-between gap-4 mt-4">
            {category.products.map((product, j) => (
              <a
                key={j}
                href={`/products/${product.slug}${
                  searchParams?.type ? "?type=" + searchParams.type : ""
                }`}
              >
                <div className="items-center">
                  <Image
                    src={product.images[0]}
                    alt={product.name}
                    width={350}
                    height={350}
                    className="rounded-3xl"
                  />
                  <div className="text-center mt-2 text-2xl font-semibold">
                    {product.name}
                  </div>
                </div>
              </a>
            ))}
          </div>
        </Block>
      ))}
    </>
  );
}
