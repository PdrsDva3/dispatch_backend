import os
from dotenv import load_dotenv

import json
import requests
from pprint import pprint
import time

load_dotenv("/home/setqbyte/PycharmProjects/dispatch_backend/deploy/.env")
api_key = os.getenv('YAN_API_KEY')
yan_url = os.getenv('YAN_URL')

headers = {
    'Authorization': f'Bearer {api_key}',
    'x-folder-id': f'{yan_url}'
}

with open('dialogue.json', 'r', encoding='utf-8') as f:
    data = json.load(f)
f.close()
data['modelUri'] = "gpt://" + yan_url + "/yandexgpt"

with open('dialogue.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)
f.close()


def yangpt(prompt: str):
    url = 'https://llm.api.cloud.yandex.net/foundationModels/v1/completion'
    with open('dialogue.json', 'r', encoding='utf-8') as f:
        dialogue = json.load(f)
    f.close()

    dialogue['messages'] +=[{
        "role": "user",
        "text": prompt
    }]

    with open('dialogue.json', 'w', encoding='utf-8') as f:
        json.dump(dialogue, f, ensure_ascii=False, indent=4)
    f.close()

    resp = requests.post(url, headers=headers, data=dialogue)

    if resp.status_code != 200:
        dialogue['messages'].pop()
        with open('dialogue.json', 'w', encoding='utf-8') as f:
            json.dump(dialogue, f, ensure_ascii=False, indent=4)
        f.close()
        raise RuntimeError(
            'Invalid response received: code: {}, message: {}'.format(
                *{resp.status_code}, *{resp.text}
            )
        )

    with open('dialogue.json', 'r', encoding='utf-8') as f:
        dialogue = json.load(f)
    f.close()

    stream = dialogue["messages"]

    with open('stream.json', 'w', encoding='utf-8') as f:
        json.dump(stream, f, ensure_ascii=False, indent=4)
    f.close()

    return

pprint(yangpt("какие грузовые вагоны ты знаешь?"))