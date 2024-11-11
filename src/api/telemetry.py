import os
import logging
from azure.core.settings import settings
from fastapi import FastAPI
from opentelemetry._events import set_event_logger_provider
from opentelemetry.sdk._events import EventLoggerProvider
from opentelemetry.instrumentation.fastapi import FastAPIInstrumentor
from prompty.tracer import Tracer, PromptyTracer,console_tracer
from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential    
from azure.monitor.opentelemetry import configure_azure_monitor


def setup_telemetry(app: FastAPI):
    settings.tracing_implementation = "OpenTelemetry"
    local_tracing_enabled=os.getenv("LOCAL_TRACING_ENABLED")
    app_insights_conn_str = os.getenv("APPINSIGHTS_CONNECTIONSTRING")
    otel_exporter_endpoint = os.getenv("OTEL_EXPORTER_OTLP_ENDPOINT")
    
    
    # Configure OpenTelemetry using Azure AI Project 
    ai_project_conn_str = os.getenv("AZURE_LOCATION")+".api.azureml.ms;"+os.getenv("AZURE_SUBSCRIPTION_ID")+";"+os.getenv("AZURE_RESOURCE_GROUP")+";"+os.getenv("AZURE_AI_PROJECT_NAME")

    # Configure OpenTelemetry using Azure AI Project 
    with AIProjectClient.from_connection_string(
    credential=DefaultAzureCredential(),
    conn_str=ai_project_conn_str,
    ) as project_client:
        
        application_insights_connection_string = project_client.telemetry.get_connection_string()
        if not application_insights_connection_string:
            print("Application Insights was not enabled for this project.")
            print("Enable it via the 'Tracing' tab in your AI Studio project page.")
            exit()
        
        if local_tracing_enabled and local_tracing_enabled.lower() == "true":
            project_client.telemetry.enable(destination=otel_exporter_endpoint)            
            Tracer.add("console", console_tracer)
            json_tracer = PromptyTracer()
            Tracer.add("PromptyTracer", json_tracer.tracer)
        elif application_insights_connection_string:
            Tracer.add("console", console_tracer)
            project_client.telemetry.enable(destination=None)
            configure_azure_monitor(connection_string=application_insights_connection_string)            
            event_provider = EventLoggerProvider()
            set_event_logger_provider(event_provider)    

    # Instrument FastAPI
    FastAPIInstrumentor.instrument_app(app)
