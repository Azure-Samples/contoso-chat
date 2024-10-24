import clsx from "clsx";
import { ReactNode } from "react";
import Image from "next/image";
import Block from "@/components/block";
import { Bars3Icon } from "@heroicons/react/24/outline";

export const Header = async ({
  params,
  searchParams,
}: {
  params: { slug: string };
  searchParams?: { [key: string]: string | string[] | undefined };
}) => {

  const user = {
    name: "Sarah Lee",
    email: "sarahlee@example.com",
    image: "/people/sarahlee.jpg",
  };

  return (
    <Block
      outerClassName=""
      innerClassName="h-12 flex flex-row center items-center"
    >
      <div className="text-slate-800">
        <a href={`/${searchParams?.type ? "?type=" + searchParams.type : ""}`}>
          <Bars3Icon className="w-6" />
        </a>
      </div>
      <div className="grow">&nbsp;</div>
      <div className="flex flex-row items-center gap-3">
        <div>
          <div className="text-right font-semibold text-zinc-600">
            {user.name}
          </div>
          <div className="text-right text-xs text-zinc-400">{user.email}</div>
        </div>
        <div className="">
          <Image
            src={user.image}
            width={32}
            height={32}
            alt={user.name}
            className="rounded-full"
          />
        </div>
      </div>
    </Block>
  );
};

export default Header;
