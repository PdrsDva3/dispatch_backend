# import config
import requests
import json
from pprint import pprint

YAN_API_KEY = 'AQVN0YxuUPrTFVCSYCYTJaRjmu8QM42ZV1CTls4s'
YAN_URL = 'b1gdrtn45hu22d0p7pn9'

api_key = YAN_API_KEY
yan_url = YAN_URL

with open('./internal/api/body.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

data['modelUri'] = "gpt://" + yan_url + "/yandexgpt-lite"

with open('body.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)


def gpt(data):
    url = 'https://llm.api.cloud.yandex.net/foundationModels/v1/completion'

    auth_headers = {
        'Authorization': 'Api-Key AQVN0YxuUPrTFVCSYCYTJaRjmu8QM42ZV1CTls4s'
    }

    with open('body.json', 'r', encoding='utf-8') as f:
        jj = json.load(f)

    jj["messages"].append(data)

    resp = requests.post(url, headers=auth_headers, json=jj)

    if resp.status_code != 200:
        raise RuntimeError(
            'Invalid response received: code: {}, message: {}'.format(
                *{resp.status_code}, *{resp.text}
            )
        )

    return resp.json()["result"]["alternatives"][0]["message"]["text"]


print(gpt({
    "role": "user",
    "text": "4 вагонов, 0 человека, 1 машины, 2 больших вагона"
}))
