from flask import Flask, request
from opentelemetry import trace
from opentelemetry.instrumentation.wsgi import collect_request_attributes
from opentelemetry.propagate import extract
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import (
BatchSpanProcessor,
ConsoleSpanExporter,
)

app = Flask(__name__)
trace.set_tracer_provider(TracerProvider())
tracer = trace.get_tracer_provider().get_tracer(__name__)
trace.get_tracer_provider().add_span_processor(
    BatchSpanProcessor(ConsoleSpanExporter())
)

@app.route("/home")
def server_request():
    with tracer.start_as_current_span(
    "home",
    context=extract(request.headers),
    kind=trace.SpanKind.SERVER,
    attributes=collect_request_attributes(request.environ)):
        print(request.args.get("param"))
        return "home page"
if __name__ == "__main__":
    app.run()