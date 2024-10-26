import os
import json
import requests
from pprint import pprint
import time

from dotenv import load_dotenv

load_dotenv("/home/setqbyte/PycharmProjects/dispatch_backend/deploy/.env")
api_key = os.getenv('YAN_API_KEY')
yan_url = os.getenv('YAN_URL')


headers = {
    'Authorization': f'Api-Key {api_key}',
}
