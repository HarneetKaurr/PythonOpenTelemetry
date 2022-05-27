from opentelemetry import trace
#The Tracer Provider from the SDK is instantiated, which is required to create a trace because it holds the configuration for all the trace objects.
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor, ConsoleSpanExporter

trace.set_tracer_provider(TracerProvider())
'''The trace object then uses that to set the span processor as BatchSpanProcessor, 
which is one type of implementation of the SpanProcessor specification from the SDK. 
As you might expect from the name, this processor batches together spans before sending 
them to an exporter.'''
trace.get_tracer_provider().add_span_processor(
BatchSpanProcessor(ConsoleSpanExporter())
)
'''ConsoleSpanExporter is used so that the output is sent to your terminal; 
this is useful for testing situations or if you don’t want to set up somewhere to export your 
data yet.'''
tracer = trace.get_tracer(__name__)
'''The tracer object is assigned to the tracer variable and a span is created in the final two lines of code.'''
with tracer.start_as_current_span("span name"):
    print("doing some work here")