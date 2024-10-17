import { ChatTurn, GroundedMessage } from "./types";

export const sendGroundedMessage = async (
  turn: ChatTurn
): Promise<ChatTurn> => {
  const message = [
    {
      role: turn.type === "user" ? "user" : "assistant",
      content: turn.message,
    },
  ];

  console.log(message);

  const response = await fetch("/api/chat/grounded", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(message),
  });

  const data = (await response.json()) as GroundedMessage;
  console.log(data);

  const newTurn: ChatTurn = {
    name: "Jane Doe",
    message: data.message,
    chat_history: [],
    session_id: null,
    status: "done",
    type: "assistant",
    responseId: data.responseId,
    avatar: "",
    image: null,
  };

  return newTurn;
};

export const sendPromptFlowMessage = async (
  turn: ChatTurn,
  customerId: string = "4" // Sarah Lee is Customer 4
): Promise<ChatTurn> => {
  const body = {
    chat_history: turn.chat_history,
    question: turn.message,
    customer_id: customerId.toString(),
    session_id: turn.session_id,
  };

  console.log(body);
  
  let response = await fetch("/api/chat/vnext", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(body),
  })
  
  let data;
  let answer = ""
  if (!response.ok) {
    answer = "I'm sorry, there was a problem."
  } else {
    data = await response.json();
    answer = data['answer']
  }

  const userMessage = {"role": "user", "content": turn.message}
  const assistantMessage = {"role": "assistant", "content": answer}

  const latestHistory = [...turn.chat_history, userMessage, assistantMessage]

  const newTurn: ChatTurn = {
    name: "Jane Doe",
    message: answer,
    chat_history: latestHistory,
    session_id: null,
    status: "done",
    type: "assistant",
    responseId: data.responseId,
    avatar: "",
    image: null,
  };

  return newTurn;
};

export const sendVisualMessage = async (
  turn: ChatTurn,
  customerId: string = "4" // Sarah Lee is Customer 4
): Promise<ChatTurn> => {
  let image_contents: any = {};

  if (turn.image) {
    const contents = turn.image.split(",");
    image_contents[contents[0]] = contents[1];
  } else {
    // send empty image - this is a single black pixel
    // which the prompt flow ignores given it's too small
    image_contents["data:image/png;base64"] =
      "iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR4nGNgYGD4DwABBAEAX+XDSwAAAABJRU5ErkJggg==";
  }

  const body = {
    chat_history: [],
    question: turn.message,
    customer_id: customerId.toString(),
  };

  console.log(body);

  const response = await fetch("/api/chat/visual", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(body),
  });

  const data = await response.json();
  console.log(data);

  const newTurn: ChatTurn = {
    name: "Jane Doe",
    message: data["answer"],
    chat_history: body.chat_history,
    session_id: null,
    status: "done",
    type: "assistant",
    responseId: data.responseId,
    avatar: "",
    image: null,
  };

  return newTurn;
};