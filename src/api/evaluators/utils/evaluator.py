# evaluator.py

import re
from tenacity import retry, stop_after_attempt, wait_exponential, retry_if_exception_type

@retry(
    retry=retry_if_exception_type(Exception),
    stop=stop_after_attempt(3),
    wait=wait_exponential(multiplier=1, min=1, max=10)
)
def evaluate_metric(question: str, context: str, answer: str, client, model_deployment, prompt: str) -> int:
    """
    Evaluates an answer based on the question and context using a specified evaluation metric.

    Args:
        question (str): The question provided.
        context (str): The context related to the question.
        answer (str): The answer to evaluate.
        client: The AzureOpenAI client instance.
        model_deployment: The deployment name of the model.
        prompt (str): The evaluation prompt to use.

    Returns:
        int: Evaluation score based on the metric, between 1 and 5.
    """

    # Prepare the messages
    system_prompt = (
        "You are an AI assistant. You will be given the definition of an evaluation metric for assessing "
        "the quality of an answer in a question-answering task. Your job is to compute an accurate evaluation "
        "score using the provided evaluation metric."
    )

    # Replace placeholders in the prompt with actual values
    user_prompt = prompt.replace("{{question}}", question).replace("{{context}}", context).replace("{{answer}}", answer)

    # Prepare the messages
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt}
    ]

    # Call the Azure OpenAI API using the client
    response = client.chat.completions.create(
        model=model_deployment,
        messages=messages,
        max_tokens=512,
        temperature=0.2
    )

    # Extract the stars from the response
    stars_text = response.choices[0].message.content.strip()

    # Extract only the numerical score from the response
    match = re.search(r'\b[1-5]\b', stars_text)
    if match:
        stars = int(match.group(0))
        return stars
    else:
        print(f"Error parsing stars from response, so would be NULL: {stars_text}")
        return None  # Return None or handle as per your requirement
