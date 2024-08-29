import os
import django
import requests
from openai import OpenAI
from pathlib import Path
from pydub import AudioSegment
from django.conf import settings

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
        "per_page": 2,
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


def combine_audio_files(input_files, output_file, silence_duration=1000):
    """
    複数の音声ファイルを1つのファイルに結合し、間に無音を挿入する関数
    silence_duration: 挿入する無音の長さ（ミリ秒）
    """
    combined = AudioSegment.empty()
    silence = AudioSegment.silent(duration=silence_duration)
    
    for i, file in enumerate(input_files):
        audio = AudioSegment.from_mp3(file)
        if i > 0:  # 最初のファイル以外の前に無音を挿入
            combined += silence
        combined += audio
    
    combined.export(output_file, format="mp3")

# メイン処理
client = init_openai()
summaries = summarize_prtimes_bodies(client)
output_dir = Path(__file__).parent.parent / "static/audio"
# output_dir = Path(settings.BASE_DIR) / "static/audio"
output_dir.mkdir(exist_ok=True)

temp_files = []

# 各サンプルテキストを音声ファイルに変換
for i, summary in enumerate(summaries):
    temp_file_path = output_dir / f"temp_{i}.mp3"
    text_to_speech(client, summary, temp_file_path)
    temp_files.append(temp_file_path)

# 全ての音声ファイルを1つに結合
final_output_path = output_dir / "combined_output.mp3"
combine_audio_files(temp_files, final_output_path, silence_duration=2000)

# 一時ファイルを削除
for file in temp_files:
    file.unlink()