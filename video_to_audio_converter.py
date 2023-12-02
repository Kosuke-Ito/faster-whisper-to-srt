from moviepy.editor import VideoFileClip

def extract_audio(video_file_path, audio_file_path):
  # ビデオファイルを読み込む
  video = VideoFileClip(video_file_path)
  
  # ビデオから音声を抽出し、ファイルとして保存する
  video.audio.write_audiofile(audio_file_path)

# 使用例

video_file_path = ''  # ここに動画ファイルのパスを入力
audio_file_path = ''  # ここに抽出した音声を保存するファイル名のパス名

extract_audio(video_file_path, audio_file_path)
