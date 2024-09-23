'use client'

import { FaRegThumbsUp, FaRegThumbsDown } from "react-icons/fa6";
import { MessageFeedback } from "@/lib/types";
import { sendFeedback } from "@/lib/feedback";
import styles from './feedback.module.css';
import { useState } from "react";

type Props = {
    responseId: string;
};

export const Feedback = ({ responseId }: Props) => {
    const [currentFeedback, setCurrentFeedback] = useState<MessageFeedback | null>(null);
    const [isAnimating, setIsAnimating] = useState<boolean>(false);
    const [feedbackSubmitted, setFeedbackSubmitted] = useState<boolean>(false);
    
    var iconsVisible: Boolean = false;

    if (responseId && responseId != '') {
        iconsVisible = true;
    }

    async function ProvideFeedback(feedback: MessageFeedback) {
        setCurrentFeedback(feedback);
        setIsAnimating(true);
        await sendFeedback(feedback);
        setTimeout(() => setIsAnimating(false), 1000); // Reset animation state after 1 second
        setFeedbackSubmitted(true);
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


     return (            
        <div className={styles.feedbackContainer}>
            {feedbackSubmitted ? (
                <p>Thank you for your feedback!</p>
            ) : (
                iconsVisible && (
                    <>
      <button
        className={`${styles.button} ${currentFeedback?.feedback === 1 ? styles.selected : ''} ${isAnimating && currentFeedback?.feedback === 1 ? styles.animate : ''}`}
        onClick={OnThumbsUpClick}
      >
      <FaRegThumbsUp />
      </button>
      <button
        className={`${styles.button} ${currentFeedback?.feedback === -1 ? styles.selected : ''} ${isAnimating && currentFeedback?.feedback === -1 ? styles.animate : ''}`}
        onClick={OnThumbsDownClick}
      >
         <FaRegThumbsDown />
      </button>
      </>
                )
            )}
        </div>
    );
};

export default Feedback;
