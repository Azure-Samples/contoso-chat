from pydantic import BaseModel

class ChatRequestModel(BaseModel):
    question: str
    customer_id: str
    chat_history: list
    session_id: str

class FeedbackItem(BaseModel):
    responseId: str
    feedback: int
    extra: dict
