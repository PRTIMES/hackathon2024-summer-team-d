import os
import requests
import json

def get_api_data():
    # APIからデータを取得する
    BASE_URL = os.environ["PRTIMES_URL"]
    ACCESS_TOKEN = os.environ["PRTIMES_API_KEY"]
    url = BASE_URL + "/releases"
    headers = {
        "Accept": "application/json",
        "Authorization": f"Bearer {ACCESS_TOKEN}",
    }

    params = {
        "per_page":2
    }
    
    response = requests.get(url, headers=headers, params=params)
    
    if response.status_code == 200:
        res = response.json()
    else:
        res = {}  # エラーハンドリング用に空の辞書を返す

    return res
