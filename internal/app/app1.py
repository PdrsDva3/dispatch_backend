from fastapi import FastAPI
from internal.app.vision import photo
from fastapi.responses import HTMLResponse
import cv2
import io
import base64
from matplotlib import pyplot as plt
import time


app1 = FastAPI()


html = """
<!DOCTYPE html>
<html>
    <head>
        <title>Chat</title>
    </head>
    <body>
         <h1>Video Stream</h1>
    <img id="videoStream" alt="Video Stream" />

    <script>
        // URL вашего WebSocket-сервера
        const wsUrl = 'http://0.0.0.0:8001/';

        // Подключаемся к WebSocket-серверу
        const socket = new WebSocket(wsUrl);

        // Получаем элемент <img> для отображения видео
        const videoElement = document.getElementById('videoStream');

        // Обработчик события открытия соединения
        socket.onopen = function(event) {
            console.log('WebSocket connection opened');
        };

        // Обработчик события получения сообщения
        socket.onmessage = function(event) {
            // Предполагается, что сервер отправляет кадры в формате Base64
            const imageData = event.data;
            videoElement.src = 'data:image/jpeg;base64,' + imageData;
        };

        // Обработчик события закрытия соединения
        socket.onclose = function(event) {
            console.log('WebSocket connection closed');
        };

        // Обработчик ошибок
        socket.onerror = function(error) {
            console.error('WebSocket error:', error);
        };
    </script>
    </body>
</html>
"""


@app1.get("/")
async def get():
    return HTMLResponse(html)


from fastapi import WebSocket, FastAPI
import asyncio

# async def generate_byte_stream():
#     """Генерация потока байт в реальном времени."""
#     while True:
#         # Генерация случайных байт (например, 10 байт)
#         byte_data = b'\x00\x01\x02\x03\x04\x05\x06\x07\x08\x09'
#         yield byte_data
#         await asyncio.sleep(1)  # Задержка для имитации реального времени

@app1.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await get_photo()
        # time.sleep(1)
        await websocket.send_text(f"Message text was: {data}")


async def get_photo():
    # Предположим, что results[0].plot() возвращает изображение в формате numpy array
    annotated_frame = photo
    # cv2.imshow("annotader_frame", annotated_frame)
    # cv2.waitKey(1)
    print("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
    # cv2.destroyAllWindows()

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
