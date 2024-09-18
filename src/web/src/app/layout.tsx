import "./globals.css";
import type { Metadata } from "next";
import Chat from "@/components/chat";
import Block from "@/components/block";
import Header from "@/components/header";

export const metadata: Metadata = {
  title: "Contoso Outdoors Company",
  description:
    "Embrace Adventure with Contoso Outdoors - Your Ultimate Partner in Exploring the Unseen!",
};

export default async function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {

  return (
    <html lang="en" className="h-full antialiased" suppressHydrationWarning>
      <body className="bg-zinc-50 text-zinc-900">
        <div className="flex min-h-screen flex-col">
          <main className="flex-grow">

            {children}
            <Block
              outerClassName="bg-zinc-800"
              innerClassName="text-zinc-100 text-right text-xs p-2"
            >
              &copy;Microsoft 2024
            </Block>
          </main>
          <Chat />
        </div>
      </body>
    </html>
  );
}
