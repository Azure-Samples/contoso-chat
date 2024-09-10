
# Azure AI Inferencing API Tracing

## Installation

Azure AI Inferencing API tracing for python is provided by Azure Core Tracing Opentelemetry package. More information about Azure Core Tracing Opentelemetry can be found here: https://learn.microsoft.com/en-us/python/api/overview/azure/core-tracing-opentelemetry-readme?view=azure-python-preview

```
pip install azure-ai-inference
pip install --force-reinstall azure_core-1.31.0-py3-none-any.whl 
pip install opentelemetry-sdk 
pip install azure-monitor-opentelemetry
```

## Setup

The environment variable AZUREAI_INFERENCE_API_ENABLE_CONTENT_TRACING controls whether the actual message contents will be included in the traces or not. By default, the message contents are not include as part of the trace. Set the value of the environment variable to true (case insensitive) for the message contents to be included as part of the trace. Any other value will cause the message contents not to be traced.

You also need to configure the tracing implmenetation in your code, like so:

```
from azure.core.settings import settings
settings.tracing_implementation = "opentelemetry"
```

## Trace Exporter(s)

In order for the traces to be captured, you need to setup the applicable trace exporters. The chosen exporter will be based on where you want the traces to be output. You can also implement your own exporter. Below are a couple of samples how to setup an exportere to Azure Insights and to console output.

```
def setup_azure_monitor_trace_exporter():
    from azure.monitor.opentelemetry.exporter import AzureMonitorTraceExporter
    trace.set_tracer_provider(TracerProvider())
    tracer = trace.get_tracer(__name__)
    span_processor = BatchSpanProcessor(
        AzureMonitorTraceExporter.from_connection_string(
            os.environ["APPLICATIONINSIGHTS_CONNECTION_STRING"]
        )
    )
    trace.get_tracer_provider().add_span_processor(span_processor)
```

```
def setup_console_trace_exporter():
    exporter = ConsoleSpanExporter()
    trace.set_tracer_provider(TracerProvider())
    tracer = trace.get_tracer(__name__)
    trace.get_tracer_provider().add_span_processor(SimpleSpanProcessor(exporter))
```
## Instrumentation

Use the AiInferenceInstrumentor to instrument the Azure AI Inferencing API for LLM tracing, this will cause the LLM traces to be emitted from Azure AI Inferencing API.

```
from azure.core.tracing import AiInferenceApiInstrumentor
# Instrument AI Inference API
AiInferenceApiInstrumentor().instrument()
```

It is also possible to uninstrument the Azure AI Inferencing API by using the uninstrument call. After this call, the LLM traces will no longer be emitted by the Azure AI Inferencing API until instrument is called again.

```
AiInferenceApiInstrumentor().uninstrument()
```

## Tracing Your Own Functions
The @distributed_trace decorater can be used to trace your own functions. You can provide attributes to be included in the trace, as part of the decorator as shown in the sample code. You can also add further attributes to the span in the function implementation as demonstrated below.

```
# The distributed_trace decorator will trace the function call and enable adding additional attributes
# to the span in the function implementation.
@distributed_trace
def get_temperature(city: str) -> str:

    # Adding attributes to the current span
    span = trace.get_current_span()
    span.set_attribute("requested_city", city)

    if city == "Seattle":
        return "75"
    elif city == "New York City":
        return "80"
    else:
        return "Unavailable"


# Attributes can be passed to the decorator to be traced with the span
@distributed_trace(tracing_attributes={"test_value": "test_attribute"})
def get_weather(city: str) -> str:
    if city == "Seattle":
        return "Nice weather"
    elif city == "New York City":
        return "Good weather"
    else:
        return "Unavailable"

```

## Example Output
Below is an example LLM trace outputs from a run of the provided [sample code](inference_tracing_sample.py).


Output from the chat completion using streaming:

```
{
    "name": "ChatCompletionsClient.complete",
    "context": {
        "trace_id": "0xd42f2d5f907bde3619ef4ed5c5b0c58b",
        "span_id": "0x988434e5b6447f10",
        "trace_state": "[]"
    },
    "kind": "SpanKind.INTERNAL",
    "parent_id": null,
    "start_time": "2024-08-20T15:41:40.350275Z",
    "end_time": "2024-08-20T15:41:42.368945Z",
    "status": {
        "status_code": "UNSET"
    },
    "attributes": {
        "gen_ai.system": "azure.ai.inference",
        "gen_ai.request.model": "gpt-4o",
        "gen_ai.response.id": "chatcmpl-9yLHJ2cQK5BLKxXhL8L6pF2rbWVl7",
        "gen_ai.response.model": "gpt-4o-2024-05-13",
        "gen_ai.response.finish_reason": "CompletionsFinishReason.STOPPED"
    },
    "events": [
        {
            "name": "gen_ai.system.message",
            "timestamp": "2024-08-20T15:41:40.350275Z",
            "attributes": {
                "get_ai.system": "azure.ai.inference",
                "gen_ai.event.content": "{\"role\": \"system\", \"content\": \"You are a helpful assistant.\"}"
            }
        },
        {
            "name": "gen_ai.user.message",
            "timestamp": "2024-08-20T15:41:40.350275Z",
            "attributes": {
                "get_ai.system": "azure.ai.inference",
                "gen_ai.event.content": "{\"role\": \"user\", \"content\": \"Tell me about software engineering in five sentences.\"}"
            }
        },
        {
            "name": "gen_ai.choice",
            "timestamp": "2024-08-20T15:41:42.368945Z",
            "attributes": {
                "get_ai.system": "azure.ai.inference",
                "gen_ai.event.content": "{\"message\": {\"content\": \"Software engineering is a disciplined approach to designing, creating, and maintaining software by applying engineering principles and best practices. It involves systematic activities including requirements gathering, design, implementation, testing, and maintenance to ensure the software functions as intended. The field emphasizes collaboration among developers, stakeholders, and users to meet project goals efficiently. Modern software engineering also incorporates methodologies like Agile and DevOps to enhance flexibility and accelerate delivery. Continuous learning and adaptation to new technologies are crucial in this ever-evolving field.\"}, \"finish_reason\": \"stop\"}"
            }
        }
    ],
    "links": [],
    "resource": {
        "attributes": {
            "telemetry.sdk.language": "python",
            "telemetry.sdk.name": "opentelemetry",
            "telemetry.sdk.version": "1.26.0",
            "service.name": "unknown_service"
        },
        "schema_url": ""
    }
}

```

Output from chat completion using the function call tool:
```
{
    "name": "ChatCompletionsClient.complete",
    "context": {
        "trace_id": "0x9d139b1889cb911ddb758264c34d41eb",
        "span_id": "0x75c23aaf399a0d64",
        "trace_state": "[]"
    },
    "kind": "SpanKind.INTERNAL",
    "parent_id": null,
    "start_time": "2024-08-20T15:41:57.865379Z",
    "end_time": "2024-08-20T15:41:59.791924Z",
    "status": {
        "status_code": "UNSET"
    },
    "attributes": {
        "gen_ai.system": "azure.ai.inference",
        "gen_ai.request.model": "gpt-4o",
        "gen_ai.response.id": "chatcmpl-9yLHbpiG2czELxJ3Hmf03Ds1aFknp",
        "gen_ai.response.model": "gpt-4o-2024-05-13",
        "gen_ai.response.finish_reason": "CompletionsFinishReason.TOOL_CALLS",
        "gen_ai.usage.completion_tokens": 44,
        "gen_ai.usage.prompt_tokens": 111
    },
    "events": [
        {
            "name": "gen_ai.system.message",
            "timestamp": "2024-08-20T15:41:57.865379Z",
            "attributes": {
                "get_ai.system": "azure.ai.inference",
                "gen_ai.event.content": "{\"role\": \"system\", \"content\": \"You are a helpful assistant.\"}"
            }
        },
        {
            "name": "gen_ai.user.message",
            "timestamp": "2024-08-20T15:41:57.865379Z",
            "attributes": {
                "get_ai.system": "azure.ai.inference",
                "gen_ai.event.content": "{\"role\": \"user\", \"content\": \"What is the weather and temperature in Seattle?\"}"
            }
        },
        {
            "name": "gen_ai.choice",
            "timestamp": "2024-08-20T15:41:59.791924Z",
            "attributes": {
                "get_ai.system": "azure.ai.inference",
                "gen_ai.event.content": "{\"message\": {\"content\": null}, \"finish_reason\": \"CompletionsFinishReason.TOOL_CALLS\", \"index\": 0}"
            }
        }
    ],
    "links": [],
    "resource": {
        "attributes": {
            "telemetry.sdk.language": "python",
            "telemetry.sdk.name": "opentelemetry",
            "telemetry.sdk.version": "1.26.0",
            "service.name": "unknown_service"
        },
        "schema_url": ""
    }
}

{
    "name": "get_weather",
    "context": {
        "trace_id": "0xf0805e145afda3ecaabfd0cc87fe037c",
        "span_id": "0x933b1fcee8cd001a",
        "trace_state": "[]"
    },
    "kind": "SpanKind.INTERNAL",
    "parent_id": null,
    "start_time": "2024-08-20T15:42:01.413865Z",
    "end_time": "2024-08-20T15:42:01.413865Z",
    "status": {
        "status_code": "UNSET"
    },
    "attributes": {
        "test_value": "test_attribute"
    },
    "events": [],
    "links": [],
    "resource": {
        "attributes": {
            "telemetry.sdk.language": "python",
            "telemetry.sdk.name": "opentelemetry",
            "telemetry.sdk.version": "1.26.0",
            "service.name": "unknown_service"
        },
        "schema_url": ""
    }
}

{
    "name": "get_temperature",
    "context": {
        "trace_id": "0xad7bdf8684f197004c1f8b079139733b",
        "span_id": "0x293fff6bde23e715",
        "trace_state": "[]"
    },
    "kind": "SpanKind.INTERNAL",
    "parent_id": null,
    "start_time": "2024-08-20T15:42:01.808956Z",
    "end_time": "2024-08-20T15:42:01.808956Z",
    "status": {
        "status_code": "UNSET"
    },
    "attributes": {
        "requested_city": "Seattle"
    },
    "events": [],
    "links": [],
    "resource": {
        "attributes": {
            "telemetry.sdk.language": "python",
            "telemetry.sdk.name": "opentelemetry",
            "telemetry.sdk.version": "1.26.0",
            "service.name": "unknown_service"
        },
        "schema_url": ""
    }
}

{
    "name": "ChatCompletionsClient.complete",
    "context": {
        "trace_id": "0x930e31c745aba12793a5eca58c7ab35c",
        "span_id": "0x946b34c6e0ebab10",
        "trace_state": "[]"
    },
    "kind": "SpanKind.INTERNAL",
    "parent_id": null,
    "start_time": "2024-08-20T15:42:02.424650Z",
    "end_time": "2024-08-20T15:42:02.975318Z",
    "status": {
        "status_code": "UNSET"
    },
    "attributes": {
        "gen_ai.system": "azure.ai.inference",
        "gen_ai.request.model": "gpt-4o",
        "gen_ai.response.id": "chatcmpl-9yLHfdHFe8zRXov5Qh2a7Bjrr24F7",
        "gen_ai.response.model": "gpt-4o-2024-05-13",
        "gen_ai.response.finish_reason": "CompletionsFinishReason.STOPPED",
        "gen_ai.usage.completion_tokens": 17,
        "gen_ai.usage.prompt_tokens": 172
    },
    "events": [
        {
            "name": "gen_ai.system.message",
            "timestamp": "2024-08-20T15:42:02.424650Z",
            "attributes": {
                "get_ai.system": "azure.ai.inference",
                "gen_ai.event.content": "{\"role\": \"system\", \"content\": \"You are a helpful assistant.\"}"
            }
        },
        {
            "name": "gen_ai.user.message",
            "timestamp": "2024-08-20T15:42:02.424650Z",
            "attributes": {
                "get_ai.system": "azure.ai.inference",
                "gen_ai.event.content": "{\"role\": \"user\", \"content\": \"What is the weather and temperature in Seattle?\"}"
            }
        },
        {
            "name": "gen_ai.assistant.message",
            "timestamp": "2024-08-20T15:42:02.424650Z",
            "attributes": {
                "get_ai.system": "azure.ai.inference",
                "gen_ai.event.content": "{\"role\": \"assistant\", \"tool_calls\": [{\"function\": {\"arguments\": \"{\\\"city\\\": \\\"Seattle\\\"}\", \"name\": \"get_weather\"}, \"id\": \"call_Z6CT5rTvzTACkHnC5CWYT2c3\", \"type\": \"function\"}, {\"function\": {\"arguments\": \"{\\\"city\\\": \\\"Seattle\\\"}\", \"name\": \"get_temperature\"}, \"id\": \"call_VKsfdTHoZyeBnufYpowAwvTC\", \"type\": \"function\"}]}"
            }
        },
        {
            "name": "gen_ai.tool.message",
            "timestamp": "2024-08-20T15:42:02.424650Z",
            "attributes": {
                "get_ai.system": "azure.ai.inference",
                "gen_ai.event.content": "{\"role\": \"tool\", \"tool_call_id\": \"call_Z6CT5rTvzTACkHnC5CWYT2c3\", \"content\": \"Nice weather\"}"
            }
        },
        {
            "name": "gen_ai.tool.message",
            "timestamp": "2024-08-20T15:42:02.424650Z",
            "attributes": {
                "get_ai.system": "azure.ai.inference",
                "gen_ai.event.content": "{\"role\": \"tool\", \"tool_call_id\": \"call_VKsfdTHoZyeBnufYpowAwvTC\", \"content\": \"75\"}"
            }
        },
        {
            "name": "gen_ai.choice",
            "timestamp": "2024-08-20T15:42:02.975318Z",
            "attributes": {
                "get_ai.system": "azure.ai.inference",
                "gen_ai.event.content": "{\"message\": {\"content\": \"The weather in Seattle is nice, and the current temperature is 75\\u00b0F.\"}, \"finish_reason\": \"CompletionsFinishReason.STOPPED\", \"index\": 0}"
            }
        }
    ],
    "links": [],
    "resource": {
        "attributes": {
            "telemetry.sdk.language": "python",
            "telemetry.sdk.name": "opentelemetry",
            "telemetry.sdk.version": "1.26.0",
            "service.name": "unknown_service"
        },
        "schema_url": ""
    }
}

===== chat_with_function_tool() done =====
```

## Open Items
- Image input
- Embeddings
- Size constraints for emitted data