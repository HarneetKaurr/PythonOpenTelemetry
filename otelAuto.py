from flask import Flask, request
from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.instrumentation.flask import FlaskInstrumentor
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

FlaskInstrumentor().instrument_app(app)

@app.route("/home")
def server_request():
    with tracer.start_as_current_span("server"):
        print(request.args.get("param"))
        return "home page"

if __name__ == "__main__":
    app.run()