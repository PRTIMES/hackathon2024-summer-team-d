import os
import requests


def extract_body_from_prtimes():
    """
    PR TIMES APIからデータを取得し、bodyの値だけを抽出する関数

    Returns:
      bodyの値のリスト
    """

    BASE_URL = os.environ["PRTIMES_URL"]
    ACCESS_TOKEN = os.environ["PRTIMES_API_KEY"]
    url = BASE_URL + "/releases"
    headers = {
        "Accept": "application/json",
        "Authorization": f"Bearer {ACCESS_TOKEN}",
    }
    res = requests.get(url, headers=headers)

    bodies = []
    for item in res.json():
        bodies.append(item["body"])
    return bodies


# bodyの値を抽出
extracted_bodies = extract_body_from_prtimes()

# 結果を表示
print(extracted_bodies)
