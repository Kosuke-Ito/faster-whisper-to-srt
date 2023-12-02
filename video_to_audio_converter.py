from moviepy.editor import VideoFileClip

def extract_audio(video_file_path, audio_file_path):
  # ビデオファイルを読み込む
  video = VideoFileClip(video_file_path)
  
  # ビデオから音声を抽出し、ファイルとして保存する
  video.audio.write_audiofile(audio_file_path)

# 使用例

video_file_path = '/Users/itokosuke/Documents/Nerd Bench/vol2_iphone15/iphone.mp4'  # ここに動画ファイルのパスを入力
audio_file_path = '/Users/itokosuke/Documents/Nerd Bench/vol2_iphone15/output_audio.mp3'        # ここに抽出した音声を保存するファイル名を入力

extract_audio(video_file_path, audio_file_path)
