import logging
import os
import uuid

from pathlib import Path
from contoso_chat.models import ChatRequestModel, FeedbackItem
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse, Response
from dotenv import load_dotenv
from fastapi.middleware.cors import CORSMiddleware
from opentelemetry import metrics
from opentelemetry import trace
from dotenv import load_dotenv
from fastapi.middleware.cors import CORSMiddleware

from contoso_chat.chat_request import get_response, provide_feedback
from telemetry import setup_telemetry

load_dotenv()

app = FastAPI()

code_space = os.getenv("CODESPACE_NAME")
app_insights = os.getenv("APPINSIGHTS_CONNECTIONSTRING")

if code_space:
    origin_8000 = f"https://{code_space}-8000.app.github.dev"
    origin_5173 = f"https://{code_space}-5173.app.github.dev"
    origins = [origin_8000, origin_5173, os.getenv(
        "API_SERVICE_ACA_URI"), os.getenv("WEB_SERVICE_ACA_URI")]

    if app_insights:
        ingestion_endpoint = app_insights.split(';')[1].split('=')[1]
        origins.append(ingestion_endpoint)

else:
    origins = [
        o.strip()
        for o in Path(Path(__file__).parent / "origins.txt").read_text().splitlines()
    ]
    origins = ['*']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

setup_telemetry(app)

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# sample metrics, this can be removed for something more meaningful later
meter = metrics.get_meter_provider().get_meter("contoso-chat")
root_counter = meter.create_counter("root-hits")

tracer = trace.get_tracer(__name__)


class APIException(Exception):
    def __init__(self, code=500):
        self.code = code


@app.exception_handler(APIException)
async def api_exception_handler(request: Request, exc: APIException):
    return JSONResponse(
        status_code=exc.code,
        content=f"There was a problem.",
    )


@app.get("/")
async def root():
    root_counter.add(1)
    logger.info("Hello from Contoso Root")
    return {"message": "Hello from Contoso Root"}


@app.post("/api/create_response")
@tracer.start_as_current_span("create_response")
def create_response(chat_request: ChatRequestModel, response: Response) -> dict:
    span = trace.get_current_span()
    span.set_attribute("session.id", chat_request.session_id)

    try:
        result, metadata = get_response(
            chat_request.customer_id, chat_request.question, chat_request.chat_history)
    except Exception as e:
        raise APIException()

    response.headers.append("gen_ai.response.id", metadata['responseId'])
    response.headers.append("gen_ai.response.model", metadata['model'])
    response_body = {"question": result['question'],
                     "answer": result['answer'], "context": result['context']}
    return response_body


@app.post("/api/give_feedback")
@tracer.start_as_current_span("provide_feedback")
def give_feedback(feedback_item: FeedbackItem) -> dict:
    result = provide_feedback(feedback_item)
    return result
