import os
from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.sdk.trace.export import ConsoleSpanExporter
from opentelemetry.sdk.trace.export import SimpleSpanProcessor
from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import SystemMessage, UserMessage, CompletionsFinishReason
from azure.core.credentials import AzureKeyCredential
from azure.core.tracing.ai.inference import AIInferenceInstrumentor
from azure.core.tracing.decorator import distributed_trace
from azure.core.settings import settings
from azure.identity import DefaultAzureCredential


def setup_azure_monitor_trace_exporter():
    from azure.monitor.opentelemetry.exporter import AzureMonitorTraceExporter
    trace.set_tracer_provider(TracerProvider())
    tracer = trace.get_tracer(__name__)
    connection_string = os.environ.get("APPINSIGHTS_CONNECTIONSTRING")
    span_processor = BatchSpanProcessor(
        AzureMonitorTraceExporter.from_connection_string(
            connection_string
        )
    )
    trace.get_tracer_provider().add_span_processor(span_processor)


def setup_console_trace_exporter():
    exporter = ConsoleSpanExporter()
    trace.set_tracer_provider(TracerProvider())
    tracer = trace.get_tracer(__name__)
    trace.get_tracer_provider().add_span_processor(SimpleSpanProcessor(exporter))


@distributed_trace(name_of_span="sample_chat_completions_with_tools")
def sample_chat_completions_with_tools():
    import os
    import json

    try:
        endpoint = "{}openai/deployments/{}".format(
            os.environ['AZURE_OPENAI_ENDPOINT'], os.environ['AZURE_OPENAI_CHAT_DEPLOYMENT'])
    except KeyError:
        print(
            "Missing environment variable 'AZURE_OPENAI_ENDPOINT' or 'AZURE_OPENAI_CHAT_DEPLOYMENT'")
        print("Set them before running this sample.")
        exit()

    from azure.ai.inference import ChatCompletionsClient
    from azure.ai.inference.models import (
        AssistantMessage,
        ChatCompletionsToolDefinition,
        CompletionsFinishReason,
        FunctionDefinition,
        SystemMessage,
        ToolMessage,
        UserMessage,
    )
    from azure.core.credentials import AzureKeyCredential

    # Define a function that retrieves flight information
    def get_flight_info(origin_city: str, destination_city: str):
        """
        This is a mock function that returns information about the next
        flight between two cities.

        Parameters:
        origin_city (str): The name of the city where the flight originates.
        destination_city (str): The destination city.

        Returns:
        str: The airline name, fight number, date and time of the next flight between the cities, in JSON format.
        """
        if origin_city == "Seattle" and destination_city == "Miami":
            return json.dumps({
                "airline": "Delta",
                "flight_number": "DL123",
                "flight_date": "May 7th, 2024",
                "flight_time": "10:00AM"})
        return json.dumps({"error": "No flights found between the cities"})

    # Define a function 'tool' that the model can use to retrieves flight information
    flight_info = ChatCompletionsToolDefinition(
        function=FunctionDefinition(
            name="get_flight_info",
            description="Returns information about the next flight between two cities. This includes the name of the airline, flight number and the date and time of the next flight, in JSON format.",
            parameters={
                "type": "object",
                "properties": {
                    "origin_city": {
                        "type": "string",
                        "description": "The name of the city where the flight originates",
                    },
                    "destination_city": {
                        "type": "string",
                        "description": "The flight destination city",
                    },
                },
                "required": ["origin_city", "destination_city"],
            },
        )
    )

    client = ChatCompletionsClient(
        endpoint=endpoint,
        credential=DefaultAzureCredential(
            exclude_interactive_browser_credential=False),
        credential_scopes=["https://cognitiveservices.azure.com/.default"],
        api_version="2023-03-15-preview",
        logging_enable=True,
    )

    # Make a chat completions call asking for flight information, while providing a tool to handle the request
    messages = [
        SystemMessage(
            content="You an assistant that helps users find flight information."),
        UserMessage(content="What is the next flights from Seattle to Miami?"),
    ]

    response = client.complete(
        messages=messages,
        tools=[flight_info],
    )

    # Note that in the above call we did not specify `tool_choice`. The service defaults to a setting equivalent
    # to specifying `tool_choice=ChatCompletionsToolChoicePreset.AUTO`. Other than ChatCompletionsToolChoicePreset
    # options, you can also explicitly force the model to use a function tool by specifying:
    # tool_choice=ChatCompletionsNamedToolChoice(function=ChatCompletionsNamedToolChoiceFunction(name="get_flight_info"))

    # The model should be asking for a tool call
    if response.choices[0].finish_reason == CompletionsFinishReason.TOOL_CALLS:

        # Append the previous model response to the chat history
        messages.append(AssistantMessage(
            tool_calls=response.choices[0].message.tool_calls))

        # In this sample we assume only one tool call was requested
        if response.choices[0].message.tool_calls is not None and len(response.choices[0].message.tool_calls) == 1:

            tool_call = response.choices[0].message.tool_calls[0]

            # Only tools of type function are supported. Make a function call.
            function_args = json.loads(
                tool_call.function.arguments.replace("'", '"'))
            print(
                f"Calling function '{tool_call.function.name}' with arguments {function_args}.")
            callable_func = locals()[tool_call.function.name]

            function_response = callable_func(**function_args)
            print(f"Function response = {function_response}")

            # Provide the tool response to the model, by appending it to the chat history
            messages.append(ToolMessage(
                tool_call_id=tool_call.id, content=function_response))

            # With the additional tools information on hand, get another response from the model
            response = client.complete(messages=messages, tools=[flight_info])

            print(f"Model response = {response.choices[0].message.content}")


if __name__ == "__main__":
    settings.tracing_implementation = "OpenTelemetry"

    # setup_console_trace_exporter()
    setup_azure_monitor_trace_exporter()

    # Instrument AI Inference API
    AIInferenceInstrumentor().instrument()

    sample_chat_completions_with_tools()
    print("===== chat_with_function_tool() done =====")
    AIInferenceInstrumentor().uninstrument()
