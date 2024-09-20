import { MessageFeedback } from "./types";

export const sendFeedback = async (
    feedback: MessageFeedback,
): Promise<any> => {
    const payload = {
        responseId: feedback.responseId,
        feedback: feedback.feedback,
        extra: feedback.extra,
    };

    console.log(payload);

    const response = await fetch("/api/chat/feedback", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify(payload),
    });

    if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
    }

    const data = await response.json();
    console.log(data);

    return data;
};