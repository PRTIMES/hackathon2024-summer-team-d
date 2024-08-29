from django.shortcuts import render
import os
import openai
from django.http import JsonResponse

# 環境変数からAPIキーを設定
openai.api_key = os.environ.get("OPENAI_API_KEY")

def chat_gpt(prompt):
    openai.api_key = openai.api_key
    openai.Model.list()

    # APIを使ってリクエストを投げる
    respose = openai

def example_view(request):
    try:
        # OpenAI APIを呼び出してレスポンスを取得
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # 新しいモデル
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": "Translate the following English text to French: 'Hello, how are you?'"}
            ],
            max_tokens=60
        )

        # レスポンスのテキストを取得
        result = response.choices[0].message['content']

        # 結果をテンプレートに渡す
        return render(request, 'index.html', {'response': result})

    except Exception as e:
        # エラー発生時の処理
        return render(request, 'index.html', {'response': f"Error: {str(e)}"})


def test_openai_api(request):
    try:
        # OpenAI APIにテストリクエストを送信
        response = openai.ChatCompletion.create(
            model="gpt-4o-mini",  # 新しいモデル
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": "Please summarize this text"}
            ],
            max_tokens=10
        )

        # レスポンスの確認
        return JsonResponse({
            'status': 'success',
            'data': response.choices[0].message['content'].strip()
        })

    except Exception as e:
        # エラー発生時の処理
        return JsonResponse({
            'status': 'error',
            'message': str(e)
        })


def indexfunc(request):
    return render(request, 'index.html')