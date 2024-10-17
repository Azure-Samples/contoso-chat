import random
import uuid
import aiohttp
import asyncio
import logging
from opentelemetry._logs import set_logger_provider
from opentelemetry.sdk._logs import LoggerProvider, LoggingHandler
from azure.monitor.opentelemetry.exporter import AzureMonitorLogExporter
from opentelemetry.sdk.resources import SERVICE_NAME, Resource
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.sdk._logs.export import BatchLogRecordProcessor
from opentelemetry.sdk._logs import (
    LoggerProvider,
    LoggingHandler,
)
import os
from opentelemetry._events import Event


logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


async def make_post_request(session, url, data):
    delay = random.randint(1, 5)
    async with session.post(url, json=data) as response:
        return response


def generate_user_prompt():

    # list of questions that the user can ask
    questions = [
        "Tell me about hiking shoes",
        "What are the best hiking poles",
        "What are the best camping tents",
        "Looking waterproof tents",
        "What are the best hiking jackets"
    ]

    return {
        "customer_id": "2",
        "question": random.choice(questions),
        "chat_history": [],
        "session_id": uuid.uuid4().hex
    }


def generate_feedback(response_id: str):

    feedback = random.choice([1, -1])
    comment = "I found this response helpful" if feedback == 1 else "I did not find this response helpful"
    sentiment = "positive" if feedback == 1 else "negative"

    feedback_data = {
        "responseId": response_id,
        "feedback": feedback,
        "extra": {
            "comment": comment,
            "sentiment": "sentiment"
        }
    }

    return feedback_data


def submit_eval(response_id: str):
    evalscores = ["gen_ai.evaluation.groundedness",
                  "gen_ai.evaluation.coherence", "gen_ai.evaluation.relevance"]

    for score in evalscores:
        eval = {"gen_ai.response.id": response_id,
                "gen_ai.evaluation.score": random.choice([1, 2, 3, 4, 5]),
                "event.name": score,
                }
        logger.info(score, extra=eval)


async def main():
    create_response = 'http://127.0.0.1:8000/api/create_response'
    give_feedback = 'http://127.0.0.1:8000/api/give_feedback'

    # data = generate_user_prompt()

    async with aiohttp.ClientSession() as session:
        # list of tasks of response id
        response_id = []
        create_resposne_tasks = [make_post_request(
            session, create_response, generate_user_prompt()) for _ in range(10)]
        responses = await asyncio.gather(*create_resposne_tasks)
        for response in responses:
            response_id.append(response.headers.get('gen_ai.response.id'))
            print(response)

        # response_id = ['chatcmpl-ACEQtl2nQA5vSm9mA7WT7iE2WIT7S', 'chatcmpl-ACEQlESuI0IHHbV10ZtTVpMqCAjUE', 'chatcmpl-ACEQaWvVFgkMB83gOjH7zbWxL3al6',
        #                'chatcmpl-ACEQTxQi0oOnvtYqxFndgExr4Hxf4', 'chatcmpl-ACEQLtT0NyJjwDt9OsVZ0m1chzh8Q', 'chatcmpl-ACDqxRhDu1N9jZSQZbhhWVIVgcbZD']

        # For each response id, generate feedback
        submit_feedback_tasks = [make_post_request(
            session, give_feedback, generate_feedback(response_id[i])) for i in range(len(response_id))]
        user_feedback = await asyncio.gather(*submit_feedback_tasks)

        for response in user_feedback:
            print(response)

         # For each response id, generate feedback

        for response in response_id:
            submit_eval(response)


if __name__ == '__main__':
    OTEL_SERVICE_NAME = os.getenv("OTEL_SERVICE_NAME", "contoso-chat-api")
    resource = Resource(attributes={SERVICE_NAME: OTEL_SERVICE_NAME
                                    })
    logger_provider = LoggerProvider(resource=resource)
    set_logger_provider(logger_provider)
    exporter = AzureMonitorLogExporter.from_connection_string(
        os.getenv("APPINSIGHTS_CONNECTIONSTRING"))
    logger_provider.add_log_record_processor(
        BatchLogRecordProcessor(exporter, schedule_delay_millis=60000))
    handler = LoggingHandler(level=logging.NOTSET,
                             logger_provider=logger_provider)
    logging.getLogger().addHandler(handler)

    asyncio.run(main())
