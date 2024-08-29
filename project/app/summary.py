import os
import requests
from openai import OpenAI


def init_openai():
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    return client


def summarize(client, text):
    """
    OpenAI APIを使ってテキストを要約する関数
    """
    response = client.chat.completions.create(
        model=os.getenv("OPENAI_MODEL"),  # 最新のモデルを使用
        messages=[
            {
                "role": "system",
                "content": "You are a helpful assistant that summarizes text.",
            },
            {
                "role": "user",
                "content": f"次の文章を日本語で簡潔に要約してください:\n\n{text}",
            },
        ],
        max_tokens=128,
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
    res = requests.get(url, headers=headers)

    bodies = []
    for item in res.json():
        bodies.append(item["body"])
    return bodies


def summarize_prtimes_bodies(client):
    """
    PR TIMES APIから取得した本文を要約する関数
    """
    bodies = extract_body_from_prtimes()
    summaries = []
    for body in bodies:
        summary = summarize(client, body)
        summaries.append(summary)
    return summaries


# メイン処理
client = init_openai()
summaries = summarize_prtimes_bodies(client)
for summary in summaries:
    print(summary)
