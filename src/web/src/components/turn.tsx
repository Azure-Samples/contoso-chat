import clsx from "clsx";
import { ReactNode, useEffect } from "react";
import {
  UserCircleIcon,
  BuildingStorefrontIcon,
} from "@heroicons/react/24/outline";

import { useRemark } from "react-remark";
import remarkGemoji from "remark-gemoji";
import { ChatTurn, ChatType } from "@/lib/types";

type Props = {
  turn: ChatTurn;
  type: ChatType;
};

export const Turn = ({ turn, type }: Props) => {
  const [reactContent, setMarkdownSource] = useRemark({
    //@ts-ignore
    remarkPlugins: [remarkGemoji],
    remarkToRehypeOptions: { allowDangerousHtml: true },
    rehypeReactOptions: {},
  });

  useEffect(() => {
    setMarkdownSource(turn.message);
  }, [turn, setMarkdownSource]);

  const getContent = (turn: ChatTurn) => {
    if (turn.status === "waiting") {
      return (
        <div className="ml-2 flex flex-row">
          <svg
            className="animate-spin -ml-1 mr-2 h-5 w-5 text-zinc-600"
            xmlns="http://www.w3.org/2000/svg"
            fill="none"
            viewBox="0 0 24 24"
          >
            <circle
              className="opacity-25"
              cx="12"
              cy="12"
              r="10"
              stroke="currentColor"
              strokeWidth="4"
            ></circle>
            <path
              className="opacity-75"
              fill="currentColor"
              d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"
            ></path>
          </svg>
          <div>{turn.message}</div>
        </div>
      );
    } else {
      return (
        <div>
          {turn.image && (
            <div className="mb-2 flex items-center">
              <img
                src={turn.image}
                className="w-full h-full rounded-xl self-center"
                alt="{turn.message}"
              />
            </div>
          )}
          <div
            className={clsx(
              "[&_a]:text-sky-800 [&_ul]:list-disc [&_ul]:list-outside [&_li]:ml-9 p-1 [&_ul]:pt-2 [&_ul]:pb-2",
              type === ChatType.Grounded
                ? "[&_a]:align-super [&_a]:text-xs [&_a]:ml-1 "
                : "[&_a]:font-semibold"
            )}
          >
            {reactContent}
          </div>
        </div>
      );
    }
  };

  if (turn.type === "user") {
    return (
      <div className="ml-24 flex gap-1">
        <div className="grow bg-sky-700 text-zinc-100 p-2 rounded-md">
          {getContent(turn)}
        </div>
        <div>
          <UserCircleIcon className="w-6 stroke-zinc-500" />
        </div>
      </div>
    );
  } else {
    return (
      <div className="flex flex-row-reverse gap-1 mr-24">
        <div className="grow bg-zinc-200 text-zinc-600 p-2 rounded-md">
          {getContent(turn)}
        </div>
        <div>
          <BuildingStorefrontIcon className="w-6 stroke-zinc-500" />
        </div>
      </div>
    );
  }
};

export default Turn;
