FROM python:3.7

WORKDIR /tgbot

COPY requirements.txt ./requirements.txt
COPY ./ ./

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "main.py"]
