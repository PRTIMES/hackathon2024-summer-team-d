import os
from .jounrnal import get_api_data
import requests
from django.http import HttpResponse
from django.shortcuts import render
from .summary import get_releaces_data
from .voice import generate_audio

# url = settings.MEDIA_URL + "project/app/outputs/summary_0.mp3"

# Create your views here.
def indexfunc(request):
    
    # 記事データ取得
    res = get_releaces_data()
    
    # 音声を生成
    # generate_audio()
    
    context = {
        "releases": res,
    }
    return render(request, "index.html", context)

def convert_json_to_html(data):
    """
    JSONデータをHTMLテーブルに変換する関数

    Args:
        data: 変換するJSONデータ

    Returns:
        str: 変換されたHTML文字列
    """

    html = "<table border='1'>"
    if isinstance(data, dict):
        for key, value in data.items():
            html += f"<tr><th>{key}</th><td>{convert_json_to_html(value)}</td></tr>"
    elif isinstance(data, list):
        html += "<ul>"
        for item in data:
            html += f"<li>{convert_json_to_html(item)}</li>"
        html += "</ul>"
    else:
        html += str(data)
    html += "</table>"
    return html


def display_prtimes_data(request):
    BASE_URL = os.environ["PRTIMES_URL"]
    ACCESS_TOKEN = os.environ["PRTIMES_API_KEY"]
    url = BASE_URL + "/releases"
    headers = {
        "Accept": "application/json",
        "Authorization": f"Bearer {ACCESS_TOKEN}",
    }
    res = requests.get(url, headers=headers)

    # JSONデータをデコード
    json_data = res.json()  # encoding引数を削除

    # JSONデータをHTMLに変換
    html_content = convert_json_to_html(json_data)

    # HTMLレスポンスを返す
    return HttpResponse(html_content, content_type="text/html; charset=utf-8")
