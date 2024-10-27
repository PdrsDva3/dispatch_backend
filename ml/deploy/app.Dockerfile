FROM python:3.9

WORKDIR /usr/src/ml

COPY requirements.txt ./requirements.txt
COPY ../ ./

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "main.py"]
