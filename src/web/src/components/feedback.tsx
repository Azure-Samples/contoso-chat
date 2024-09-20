'use client'

import { FaRegThumbsUp, FaRegThumbsDown } from "react-icons/fa6";
import { MessageFeedback } from "@/lib/types";
import { sendFeedback } from "@/lib/feedback";
import { clsx } from 'clsx';

type Props = {
    responseId: string;
};

export const Feedback = ({ responseId }: Props) => {
    var iconsVisible: Boolean = false;

    if (responseId && responseId != '') {
        iconsVisible = true;
    }

    async function ProvideFeedback(feedback: MessageFeedback) {
        await sendFeedback(feedback);
    }

    async function OnThumbsUpClick() {
        console.log("Thumbs up Clicked: " + responseId);
        const positiveFeedback: MessageFeedback = { responseId: responseId, feedback: 1, extra: { sentiment: 'positive', comments: '' } }
        await ProvideFeedback(positiveFeedback);
    }

    async function OnThumbsDownClick() {
        const negativeFeedback: MessageFeedback = { responseId: responseId, feedback: -1, extra: { sentiment: 'negative', comments: '' } }
        await ProvideFeedback(negativeFeedback);
    }


    if (iconsVisible) {
        return (
            <div>
                <p>&nbsp;</p>
                <div className='flex'>
                    <FaRegThumbsUp size='20px' onClick={OnThumbsUpClick} />
                    &nbsp;
                    <FaRegThumbsDown size='20px' onClick={OnThumbsDownClick} />
                </div>
            </div>
        );
    }
};

export default Feedback;
