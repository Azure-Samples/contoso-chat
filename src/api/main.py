import logging
import os
from pathlib import Path
from fastapi import FastAPI, Request
from dotenv import load_dotenv
from fastapi.middleware.cors import CORSMiddleware
from opentelemetry import metrics
from opentelemetry import trace

from .contoso_chat.chat_request import get_response
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

tracer = trace.get_tracer("contoso.chat.main")

@app.get("/")
async def root():
    root_counter.add(1)
    logger.info("Hello from root endpoint")
    return {"message": "Hello World"}


@app.post("/api/create_response")
@tracer.start_as_current_span("create_response")
def create_response(question: str, customer_id: str, chat_history: str, request: Request) -> dict:
    session_id = request.cookies.get('sessionid')
    if session_id:
        span = trace.get_current_span()
        span.set_attribute("session.id", session_id)
    result = get_response(customer_id, question, chat_history)
    return result
