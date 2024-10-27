from datetime import datetime

import cv2
from starlette.responses import HTMLResponse
from ultralytics import YOLO
from fastapi import FastAPI, WebSocket
import base64
from fastapi_app.internal.api.api import gpt
from ml.deploy.migrations import add_new_report

app1 = FastAPI()
label_dict = {0: 'Excavator', 1: 'car', 2: 'danger', 3: 'rail', 4: 'wagon', 5: 'worker'}

video_path = "ml/internal/app/2_5208500968638928983.mp4"

model = YOLO("ml/internal/app/best.onnx")  # pretrained YOLO11n model

html = """
<!DOCTYPE html>
<html>
    <head>
        <title>Chat</title>
    </head>
    <body>
    <h1>Video Stream</h1>
    <img id="videoStream" alt="Video Stream" style="max-width: 100%; height: auto;" />

    <script>
        // URL вашего WebSocket-сервера
        var ws = new WebSocket("ws://localhost:8001/ws");

        // Получаем элемент <img> для отображения видео
        var videoElement = document.getElementById('videoStream');

        // Обработчик события получения сообщения
        ws.onmessage = function(event) {
            // Предполагается, что сервер отправляет изображения в формате Base64
            var imageData = event.data;
            videoElement.src = 'data:image/jpeg;base64,' + imageData;
        };

        // Обработчик события открытия соединения
        ws.onopen = function(event) {
            console.log('WebSocket connection opened');
        };

        // Обработчик события закрытия соединения
        ws.onclose = function(event) {
            console.log('WebSocket connection closed');
        };

        // Обработчик ошибок
        ws.onerror = function(error) {
            console.error('WebSocket error:', error);
        };
    </script>
    </body>
</html>
"""


@app1.get("/")
async def get():
    return HTMLResponse(html)


def count_labels(array):
    result = {}

    for item in array:
        label = label_dict.get(item, None)

        if label is not None:
            if label in result:
                result[label] += 1
            else:
                result[label] = 1

    return result


@app1.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    count = {}
    for el in label_dict.values():
        count[el] = 0
    count["big wagon"] = 0
    cap = cv2.VideoCapture(video_path)
    cnt_free_problem = 0
    cnt = {}
    frame_count = 0
    while cap.isOpened():
        frame_count += 1
        success, frame = cap.read()
        if success:
            if frame_count % 5 == 0:
                results = model(frame)
                big_train_count = 0
                tt = [int(el) for el in results[0].boxes.cls]
                cnt = count_labels(tt)

                for r in results:

                    for i in range(len(r.boxes.cls)):
                        if r.boxes.cls[i] == 4:
                            w = r.boxes.xywh[i][2]
                            h = r.boxes.xywh[i][3]
                            if w > 200 and h > 300:
                                big_train_count += 1

                annotated_frame = results[0].plot()
                _, buffer = cv2.imencode('.jpg', annotated_frame)
                base64_frame = base64.b64encode(buffer).decode('utf-8')

                await websocket.send_text(base64_frame)
                if big_train_count > 0:
                    cnt["big wagon"] = big_train_count
                    cnt["wagon"] -= big_train_count
                for k, v in cnt.items():
                    count[k] += v
        else:
            break
        if frame_count % 30 == 0:
            out = {}
            for k, v in count.items():
                out[k] = int(v / 6)

            for el in label_dict.values():
                count[el] = 0
            count["big wagon"] = 0
            text = f"{out["wagon"]} вагонов, {out["worker"]} человека, {out["car"]} машины, {out["big wagon"]} больших вагона, {out["Excavator"]} экскаваторов"

            await add_new_report(out["worker"], out["wagon"], out["Excavator"], out["car"], out["big wagon"], datetime.now())

            risk = gpt({
                "role": "user",
                "text": text,
            })
            if int(risk.split()[0]) > 70 :
                await websocket.send_text("problem" + risk)
                cnt_free_problem = 0
            else:
                cnt_free_problem += 1
        if cnt_free_problem > 6:
            await websocket.send_text("no problem")
            cnt_free_problem = 0

    cap.release()
