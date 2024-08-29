import os
import requests
from openai import OpenAI


def init_openai():
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    return client


def summarize(text):
    """
    OpenAI APIを使ってテキストを要約する関数
    """
    client = init_openai()
    response = client.chat.completions.create(
        model=os.getenv("OPENAI_MODEL"),  # 最新のモデルを使用
        messages=[
            {
                "role": "system",
                "content": "You are a helpful assistant that summarizes text.",
            },
            {
                "role": "user",
                "content": f"次の文章を要約してください:\n\n{text}",
            },
        ],
        max_tokens=240,
        temperature=0.7,
    )
    return response.choices[0].message.content


def extract_body_from_prtimes():
    """
    PR TIMES APIからデータを取得し、bodyの値だけを抽出する関数
    """
    BASE_URL = os.environ["PRTIMES_URL"]
    ACCESS_TOKEN = os.environ["PRTIMES_API_KEY"]
    url = BASE_URL + "/releases"
    headers = {
        "Accept": "application/json",
        "Authorization": f"Bearer {ACCESS_TOKEN}",
    }
    params = {
        "per_page": 2,
    }
    res = requests.get(url, headers=headers, params=params)
    
    # bodies = []
    # for item in res.json():
    #     bodies.append(item["body"])
    
    if res.status_code == 200:
        res = res.json()
    else:
        res = {}
    return res


def summarize_prtimes_bodies():
    """
    PR TIMES APIから取得した本文を要約する関数
    """
    
    res = extract_body_from_prtimes()
    for post in res:
        post["items"] = summarize(post["body"])
    
    return res


# メイン処理
# print(summarize_prtimes_bodies())
