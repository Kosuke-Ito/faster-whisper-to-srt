データからyoutubeの字幕やテロップを作るプログラムのリポジトリです。

文字起こしには、Fater whisperを使用しています。
https://github.com/SYSTRAN/faster-whisper

## 使い方
python-dotenvをインストール
```
pip install python-dotenv
```

.env.sampleを.envにリネームしてINPUT_MOVIE_PATHとOUTPUT_AUDIO_PATHを設定してください。