export interface ChatTurn {
  name: string;
  avatar: string;
  image: string | null;
  message: string;
  status: "waiting" | "done";
  type: "user" | "assistant";
};

export enum ChatType {
  Grounded,
  Visual,
  Video,
  PromptFlow
};

export interface Product {
  id: number;
  name: string;
  price: number;
  category: string;
  brand: string;
  description: string;
  slug: string;
  manual: string;
  images: string[];
};

export interface ProductGroup {
    name: string;
    slug: string;
    description: string;
    products: Product[];
};

export interface Citation {
  index: number;
  productId: number;
  slug: string;
  chunk: string;
  manual: string;
  replace: string;
};

export interface GroundedMessage {
  message: string;
  citations: Citation[];
};