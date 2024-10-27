FROM python:3.12

WORKDIR /usr/src/app

COPY requirements.txt ./requirements.txt
COPY ../ ./

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "main.py"]
