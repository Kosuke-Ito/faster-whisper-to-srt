from moviepy.editor import VideoFileClip
from dotenv import load_dotenv
import os

# 環境変数の読み込み
load_dotenv()

# 環境変数からパスを取得
OUTPUT_AUDIO_PATH = os.getenv("OUTPUT_AUDIO_PATH")
INPUT_MOVIE_PATH = os.getenv("INPUT_MOVIE_PATH")

def extract_audio(video_file_path, audio_file_path):
  # ビデオファイルを読み込む
  video = VideoFileClip(video_file_path)
  
  # ビデオから音声を抽出し、ファイルとして保存する
  video.audio.write_audiofile(audio_file_path)

extract_audio(INPUT_MOVIE_PATH, OUTPUT_AUDIO_PATH)
