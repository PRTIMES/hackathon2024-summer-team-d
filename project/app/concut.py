from pydub import AudioSegment
from pathlib import Path


def concatenate_audios_with_silence(audio_paths, output_path, silence_duration=2000):
    """
    複数の音声ファイルを結合して、一つのファイルにする関数。
    音声ファイルの繋ぎ目に無音を追加。

    Parameters:
    - audio_paths: リスト, 結合するMP3ファイルのパスのリスト
    - output_path: パス, 結合後のファイルの保存先
    - silence_duration: int, 無音の長さ（ミリ秒単位）
    """
    combined = AudioSegment.empty()
    silence = AudioSegment.silent(duration=silence_duration)

    for path in audio_paths:
        audio = AudioSegment.from_mp3(path)
        combined += audio + silence

    combined.export(output_path, format="mp3")


# 結合したい音声ファイルのパスをリストに追加
audio_files = [
    Path("/Users/koya/hackathon2024-summer-team-d/project/app/outputs/summary_0.mp3"),
    Path("/Users/koya/hackathon2024-summer-team-d/project/app/outputs/summary_1.mp3"),
    Path("/Users/koya/hackathon2024-summer-team-d/project/app/outputs/summary_2.mp3"),
    Path("/Users/koya/hackathon2024-summer-team-d/project/app/outputs/summary_3.mp3"),
    Path("/Users/koya/hackathon2024-summer-team-d/project/app/outputs/summary_4.mp3"),
    Path("/Users/koya/hackathon2024-summer-team-d/project/app/outputs/summary_5.mp3"),
]

# 出力ファイルのパス
output_file = Path(
    "/Users/koya/hackathon2024-summer-team-d/project/app/outputs/combined_audio_with_silence.mp3"
)

# 音声ファイルを結合（繋ぎ目に1秒の無音を追加）
concatenate_audios_with_silence(audio_files, output_file, silence_duration=1000)
print(f"Combined audio with silence saved to {output_file}")
