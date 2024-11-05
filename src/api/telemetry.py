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
from opentelemetry import trace as oteltrace
import contextlib
from prompty.tracer import Tracer, PromptyTracer


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

@contextlib.contextmanager
def trace_span(name: str):    
    tracer = oteltrace.get_tracer("prompty")    
    with tracer.start_as_current_span(name, attributes={"task": name}) as span:        
        def verbose_trace(key, value):            
            if isinstance(value, dict):             
                for k, v in value.items():                  
                    verbose_trace(f"{key}.{k}", v)        
            elif isinstance(value, (list, tuple)):
                for index, item in enumerate(value):
                    span.set_attribute(f"{index}", str(item))  
            else:
                # switch on key names to set attributes
                if "result.model.api" in key:
                    span.set_attribute("gen_ai.operation.name", value)
                elif "result.model.api.config.azure_deployment" in key:
                    span.set_attribute("gen_ai.request.modelfile", value)
                elif "inputs.prompt.model.configuration.type" in key:
                    span.set_attribute("gen_ai.system", value)
                elif "result.model" in key:
                    span.set_attribute("gen_ai.response.model", value)
                elif "result.usage.total_tokens" in key:
                    span.set_attribute("gen_ai.usage.input_tokens", value)
                elif "result.usage.completion_tokens" in key:
                    span.set_attribute("gen_ai.usage.output_tokens", value)
                elif key == "run" and isinstance(value, (list, tuple)) and len(value) > 0:
                        span.set_attribute("gen_ai.choice", value[0])
                # elif "gen_ai.event.content" in key:
                #     span.set_attribute("gen_ai.event.content", value)
                # elif "gen_ai.evaluation" in key:
                #     span.set_attribute("gen_ai.evaluation", value)
                # elif "gen_ai.response.id" in key:
                #     span.set_attribute("gen_ai.response.id", value)
                else:
                    span.set_attribute(f"{key}", value)  
        yield verbose_trace

def setup_telemetry(app: FastAPI):
    settings.tracing_implementation = "OpenTelemetry"
    app_insights_conn_str = os.getenv("APPINSIGHTS_CONNECTIONSTRING")
    otel_exporter_endpoint = os.getenv("OTEL_EXPORTER_OTLP_ENDPOINT")

    # Get prompty tracer
    Tracer.add("prompty_span", trace_span)
    # Instrument AI Inference API
    AIInferenceInstrumentor().instrument()

    # Set up exporters
    if app_insights_conn_str:
        setup_azure_monitor_exporters(conn_str=app_insights_conn_str)
    elif otel_exporter_endpoint:
        setup_otlp_traces_exporter(endpoint=otel_exporter_endpoint)

    # Instrument FastAPI
    FastAPIInstrumentor.instrument_app(app)
