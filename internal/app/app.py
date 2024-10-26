import os

from fastapi import FastAPI, HTTPException
# from tests.test_python import image

from deploy.migrations import get_employee, create_employee, login_employee

from opentelemetry import trace
from opentelemetry.exporter.jaeger.thrift import JaegerExporter
from opentelemetry.sdk.resources import Resource
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.instrumentation.fastapi import FastAPIInstrumentor
from deploy import config
from internal.app.vision import photo
from fastapi.responses import HTMLResponse
import time
import cv2
import io
import base64
from matplotlib import pyplot as plt
# import dotenv

app = FastAPI()

trace.set_tracer_provider(
    TracerProvider(
        resource=Resource.create({"service.name": "my-fastapi-service"})
    )
)

# dotenv.DotEnv("/home/setqbyte/PycharmProjects/dispatch_backend/deploy/.env")
jaeger_exporter = JaegerExporter(
    agent_host_name=config.TRACE_HOST,
    agent_port=config.TRACE_PORT,
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

html = """
<!DOCTYPE html>
<html>
    <head>
        <title>Chat</title>
    </head>
    <body>
        <h1>WebSocket Chat</h1>
        <form action="" onsubmit="sendMessage(event)">
            <input type="text" id="messageText" autocomplete="off"/>
            <button>Send</button>
        </form>
        <ul id='messages'>
        </ul>
        <script>
            var ws = new WebSocket("ws://localhost:8000/ws");
            ws.onmessage = function(event) {
            var imageContainer = document.getElementById('image-container');
            imageContainer.innerHTML = '';
            var image = document.createElement('img');
            image.src = event.data;
            imageContainer.appendChild(image);
        };


            function sendMessage(event) {
                var input = document.getElementById("messageText")
                ws.send(input.value)
                input.value = ''
                event.preventDefault()
            }
        </script>
    </body>
</html>
"""


@app.get("/")
async def get():
    return HTMLResponse(html)


from fastapi import WebSocket
import asyncio

async def generate_byte_stream():
    """Генерация потока байт в реальном времени."""
    while True:
        # Генерация случайных байт (например, 10 байт)
        byte_data = b'\x00\x01\x02\x03\x04\x05\x06\x07\x08\x09'
        yield byte_data
        await asyncio.sleep(1)  # Задержка для имитации реального времени

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = get_photo()
        # time.sleep(1)
        await websocket.send_text(f"Message text was: {data}")


async def get_photo():
    # Предположим, что results[0].plot() возвращает изображение в формате numpy array
    annotated_frame = photo

    # Преобразуем изображение из BGR в RGB (если используется OpenCV)
    annotated_frame_rgb = cv2.cvtColor(annotated_frame, cv2.COLOR_BGR2RGB)

    # Создаем буфер в памяти
    buf = io.BytesIO()

    # Сохраняем изображение в буфер с помощью matplotlib
    plt.imsave(buf, annotated_frame_rgb, format='png')

    # Получаем байты из буфера
    image_bytes = buf.getvalue()

    # Преобразуем байты в строку Base64
    image_base64 = base64.b64encode(image_bytes).decode('utf-8')

    # Закрываем буфер
    buf.close()

    # Создаем HTML-код с изображением
    html_img = f'<img src="data:image/png;base64,{image_base64}" alt="Annotated Frame"/>'
    return html_img



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
