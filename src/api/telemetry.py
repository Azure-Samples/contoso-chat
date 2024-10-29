import os
import logging
from azure.core.settings import settings
from azure.monitor.opentelemetry.exporter import AzureMonitorTraceExporter, AzureMonitorMetricExporter, AzureMonitorLogExporter
from fastapi import FastAPI
from opentelemetry import metrics
from opentelemetry import trace
from opentelemetry.sdk._logs.export import BatchLogRecordProcessor
from opentelemetry.sdk._logs import (
    LoggerProvider,
    LoggingHandler,
)
from opentelemetry._logs import set_logger_provider
from opentelemetry.sdk._logs import LoggerProvider, LoggingHandler
from opentelemetry.sdk.metrics import MeterProvider
from opentelemetry.sdk.metrics.export import PeriodicExportingMetricReader
from opentelemetry.sdk.resources import SERVICE_NAME, Resource
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.instrumentation.fastapi import FastAPIInstrumentor
from azure.ai.inference.tracing import AIInferenceInstrumentor


def setup_azure_monitor_exporters(conn_str: str):
    OTEL_SERVICE_NAME = os.getenv("OTEL_SERVICE_NAME", "contoso-chat-api")
    resource = Resource(attributes={
        SERVICE_NAME: OTEL_SERVICE_NAME
    })

    # Traces
    tracer_provider = TracerProvider(resource=resource)
    trace.set_tracer_provider(tracer_provider)
    processor = BatchSpanProcessor(
        AzureMonitorTraceExporter.from_connection_string(conn_str)
    )
    tracer_provider.add_span_processor(processor)

    # Metrics
    exporter = AzureMonitorMetricExporter.from_connection_string(conn_str)
    reader = PeriodicExportingMetricReader(
        exporter, export_interval_millis=60000)
    meter_provider = MeterProvider(metric_readers=[reader], resource=resource)
    metrics.set_meter_provider(meter_provider)

    # Logs
    logger_provider = LoggerProvider(resource=resource)
    set_logger_provider(logger_provider)
    exporter = AzureMonitorLogExporter.from_connection_string(conn_str)
    logger_provider.add_log_record_processor(
        BatchLogRecordProcessor(exporter, schedule_delay_millis=60000))

    handler = LoggingHandler(level=logging.NOTSET,
                             logger_provider=logger_provider)
    logging.getLogger().addHandler(handler)


def setup_otlp_traces_exporter(endpoint: str):
    from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter
    from opentelemetry.exporter.otlp.proto.grpc.metric_exporter import OTLPMetricExporter
    from opentelemetry.exporter.otlp.proto.grpc._log_exporter import OTLPLogExporter
    OTEL_SERVICE_NAME = os.getenv("OTEL_SERVICE_NAME", "contoso-chat-api-dev")
    resource = Resource(attributes={
        SERVICE_NAME: OTEL_SERVICE_NAME
    })

    # Traces
    tracer_provider = TracerProvider(resource=resource)
    processor = BatchSpanProcessor(
        OTLPSpanExporter(endpoint=endpoint, insecure=True))
    tracer_provider.add_span_processor(processor)
    trace.set_tracer_provider(tracer_provider)

    # Metrics
    exporter = OTLPMetricExporter(endpoint=endpoint, insecure=True)
    reader = PeriodicExportingMetricReader(
        exporter, export_interval_millis=60000)
    meter_provider = MeterProvider(metric_readers=[reader], resource=resource)
    metrics.set_meter_provider(meter_provider)

    # Logs
    logger_provider = LoggerProvider(resource=resource)
    set_logger_provider(logger_provider)
    exporter = OTLPLogExporter(endpoint=endpoint)
    logger_provider.add_log_record_processor(BatchLogRecordProcessor(exporter))
    handler = LoggingHandler(level=logging.NOTSET,
                             logger_provider=logger_provider)
    handler.setFormatter(logging.Formatter("Python: %(message)s"))
    logging.getLogger().addHandler(handler)


def setup_telemetry(app: FastAPI):
    settings.tracing_implementation = "OpenTelemetry"
    app_insights_conn_str = os.getenv("APPINSIGHTS_CONNECTIONSTRING")
    otel_exporter_endpoint = os.getenv("OTEL_EXPORTER_OTLP_ENDPOINT")

    # Instrument AI Inference API
    AIInferenceInstrumentor().instrument()

    # Set up exporters
    if app_insights_conn_str:
        setup_azure_monitor_exporters(conn_str=app_insights_conn_str)
    elif otel_exporter_endpoint:
        setup_otlp_traces_exporter(endpoint=otel_exporter_endpoint)

    # Instrument FastAPI
    FastAPIInstrumentor.instrument_app(app)
