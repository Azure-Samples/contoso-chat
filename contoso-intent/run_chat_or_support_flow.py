from promptflow import tool
from promptflow.connections import AzureOpenAIConnection
import os, openai
from jinja2 import Template

@tool
def run_chat_or_support_flow(
    query: str,
    chat_history: list[str],
    customer_id: str,
    azure_open_ai_connection: AzureOpenAIConnection,
    intent: str,
) -> str:
    """
    run chat or support flow based on the intent
    """
    if intent == "chat":
        return run_chat_flow(
            query=query,
            chat_history=chat_history,
            customer_id=customer_id,
            azure_open_ai_connection=azure_open_ai_connection,
        )
    elif intent == "support":
        return run_support_flow(
            query=query,
            chat_history=chat_history,
            customer_id=customer_id,
            azure_open_ai_connection=azure_open_ai_connection,
        )
    else:
        raise ValueError("unknown intent")
    