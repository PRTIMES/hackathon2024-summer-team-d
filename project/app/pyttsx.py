import pyttsx3

# 初期化
engine = pyttsx3.init()

# 声の選択
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)
engine.setProperty("rate", 150)

# for voice in voices:
#     print(f'voice: {voice.name}')
#     print(f'id: {voice.id}')
#     print('')

engine.say("その音声をファイルとして保存することもできます。以下のコードを使用することで、というファイル名で音声ファイルを保存することができます。")
engine.runAndWait()