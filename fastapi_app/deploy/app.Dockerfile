FROM python:3.9

WORKDIR /fastapi_app

COPY requirements.txt ./requirements.txt
COPY ../ ./


RUN pip install --no-cache-dir -r requirements.txt
RUN apt-get update && apt-get install -y ffmpeg libsm6 libxext6
RUN pip install -U opencv-python-headless
RUN apt-get update && apt-get install -y libgl1 libglib2.0-0

CMD ["python", "main.py"]
