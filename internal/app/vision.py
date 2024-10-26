import cv2
from ultralytics import YOLO
from fastapi import FastAPI, WebSocket, BackgroundTasks, Request
import asyncio
import uvicorn
import base64
from PIL import Image
import json
import io

app = FastAPI()

video_path = "/Users/alexgorin/Documents/Development/pythonProject2/itc2024/rzhd2_dataset/2_5208500968638928983.mp4"

# Load the YOLO model
model = YOLO("/Users/alexgorin/Documents/Development/pythonProject2/itc2024/best.onnx")  # pretrained YOLO11n model

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    
    # Open the video file
    cap = cv2.VideoCapture(video_path)

    # Loop through the video frames
    frame_count = 0
    while cap.isOpened():
        frame_count += 1
        # Read a frame from the video
        success, frame = cap.read()

        if success:

            # Run YOLO inference on the frame
            if frame_count % 3 == 0:
                results = model(frame)
                big_train_count = 0
                # print("boxes---")
                for r in results:
                    for i in range(len(r.boxes.cls)):
                        if r.boxes.cls[i] == 4:
                            # print("coords", r.boxes.xywh[i])
                            w = r.boxes.xywh[i][2]
                            h = r.boxes.xywh[i][3]
                            if w > 200 and h > 300:
                                big_train_count += 1

                # Visualize the results on the frame
                annotated_frame = results[0].plot()
                _, buffer = cv2.imencode('.jpg', annotated_frame)
                base64_frame = base64.b64encode(buffer).decode('utf-8')
                
                # Отправка кадра через WebSocket
                await websocket.send_text(base64_frame)

                # send base64 to frontend!!!

                print("Big trains", big_train_count)
                # Display the annotated frame
                # cv2.imshow("YOLO Inference", annotated_frame)

                # Break the loop if 'q' is pressed
                # if cv2.waitKey(1) & 0xFF == ord("q"):
                #     break
        else:
            # Break the loop if the end of the video is reached
            break

    # Release the video capture object and close the display window
    cap.release()
    # cv2.destroyAllWindows()
