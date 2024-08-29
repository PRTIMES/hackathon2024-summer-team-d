import pyttsx3

# 初期化
engine = pyttsx3.init()

# 声の選択
voices = engine.getProperty("voices")
engine.setProperty("rate", 190)

# for voice in voices:
#     print(f'voice: {voice.name}')
#     print(f'id: {voice.id}')
#     print('')

engine.say("FIMフラットトラック世界選手権にアジアから唯一参戦している大森雅俊は、8月24日にイギリスのキングズ・リンで行われた第3戦にZAETA CORSE TRICOLORE TEAMのファクトリーライダーとして参加しました。寒さと雨による厳しいコンディションの中でのレースとなりました。大森は序盤からマシントラブルに見舞われ、2回目のヒートレースでは時間切れでポイントを獲得できず、その後もジャンプスタートの反則により最後尾からのスタートを余儀なくされました。結果として決勝レースには進めず、全体で19位となり、わずか2ポイントを獲得して次回のフランス戦に向かいます。")
engine.runAndWait()