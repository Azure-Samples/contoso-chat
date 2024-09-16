import logging
import os
from pathlib import Path
from fastapi import FastAPI
from dotenv import load_dotenv
from prompty.tracer import trace
from fastapi.middleware.cors import CORSMiddleware
from opentelemetry import metrics

from .contoso_chat.chat_request import get_response, provide_feedback
from .telemetry import setup_telemetry
from azure.core.tracing.decorator import distributed_trace


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


@app.get("/")
async def root():
    root_counter.add(1)
    logger.info("Hello from root endpoint")
    return {"message": "Hello World"}


@app.post("/api/create_response")
@distributed_trace(name_of_span="create_response")
def create_response(question: str, customer_id: str, chat_history: str) -> dict:
    result = get_response(customer_id, question, chat_history)
    return result

@app.post("/api/give_feedback")
@distributed_trace(name_of_span="provide_feedback")
def give_feedback(customer_id: str, responseId: str, feedback: str) -> dict:
    result = provide_feedback(customer_id, responseId, feedback)
    return result