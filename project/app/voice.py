import os
import requests
from openai import OpenAI
from pathlib import Path


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
        "per_page": 1,
    }
    res = requests.get(url, headers=headers, params=params)
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


def text_to_speech(client, text, file_path):
    """
    OpenAIの音声合成機能を使ってテキストを音声ファイルに変換する関数
    """
    response = client.audio.speech.create(model="tts-1", voice="alloy", input=text)
    response.stream_to_file(file_path)


# メイン処理
client = init_openai()
summaries = summarize_prtimes_bodies(client)
output_dir = Path(__file__).parent / "outputs"
output_dir.mkdir(exist_ok=True)

for i, summary in enumerate(summaries):
    print(summary)
    speech_file_path = output_dir / f"summary_{i}.mp3"
    text_to_speech(client, summary, speech_file_path)
    print(f"Audio saved to {speech_file_path}")
