import os

from fastapi import FastAPI, HTTPException
from deploy.migrations import get_employee, create_employee, login_employee

from opentelemetry import trace
from opentelemetry.exporter.jaeger.thrift import JaegerExporter
from opentelemetry.sdk.resources import Resource
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.instrumentation.fastapi import FastAPIInstrumentor

app = FastAPI()

trace.set_tracer_provider(
    TracerProvider(
        resource=Resource.create({"service.name": "my-fastapi-service"})
    )
)

jaeger_exporter = JaegerExporter(
    agent_host_name=os.getenv("TRACE_HOST"),
    agent_port=int(os.getenv("TRACE_PORT")),
)

trace.get_tracer_provider().add_span_processor(
    BatchSpanProcessor(jaeger_exporter)
)

FastAPIInstrumentor.instrument_app(app)

tracer = trace.get_tracer(__name__)

@app.get("/employee={id}")
async def get_employee_h(employee_id: int):
    with tracer.start_as_current_span("get_employee_handler") as span:
        span.set_attribute("handler", "get_employee")
    employee = await get_employee(employee_id)
    if not employee:
        raise HTTPException(status_code=404, detail="User not found")
    return employee


@app.post("/create_employee")
async def create_employee_h(login: str, password: str, name: str, last_name: str, father_name: str, profession: str):
    with tracer.start_as_current_span("create_employee_handler") as span:
        span.set_attribute("handler", "create_employee")
    employee_id = await create_employee(login, password, name, last_name, father_name, profession)
    if employee_id is None:
        raise HTTPException(status_code=500, detail="Internal Server Error")
    return employee_id


@app.post("/login")
async def login_employee_h(login: str, password: str):
    with tracer.start_as_current_span("login_employee_handler") as span:
        span.set_attribute("handler", "login_employee")
    employee_id = await login_employee(login, password)
    if employee_id is None:
        raise HTTPException(status_code=404, detail="Invalid login or password")
    return employee_id
