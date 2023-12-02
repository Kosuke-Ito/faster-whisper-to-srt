# Google colabのコードを残すためのファイル

!pip install "faster-whisper @ git+https://github.com/guillaumekln/faster-whisper@master#faster-whisper[conversion]"
!wget -q http://groups.inf.ed.ac.uk/ami/AMICorpusMirror/amicorpus/ES2004a/audio/ES2004a.Mix-Headset.wav

!nvidia-smi

!ct2-transformers-converter --model openai/whisper-large-v2 --output_dir whisper-large-v2-ct2 \
    --copy_files tokenizer.json --quantization float16


from faster_whisper import WhisperModel

model_path = "whisper-large-v2-ct2/"

# Run on GPU with FP16
model = WhisperModel(model_path, device="cuda", compute_type="float16")

# or run on GPU with INT8
# model = WhisperModel(model_path, device="cuda", compute_type="int8_float16")
# or run on CPU with INT8
# model = WhisperModel(model_path, device="cpu", compute_type="int8")

%time segments, info = model.transcribe("/content/output_audio.mp3", beam_size=10)

print("Detected language '%s' with probability %f" % (info.language, info.language_probability))

srt_output = ""
for i, segment in enumerate(segments):
    start = segment.start
    end = segment.end
    text = segment.text

    # SRT形式で時間をフォーマット
    start_srt = f"{int(start // 3600):02}:{int(start % 3600 // 60):02}:{int(start % 60):02},{int(start % 1 * 1000):03}"
    end_srt = f"{int(end // 3600):02}:{int(end % 3600 // 60):02}:{int(end % 60):02},{int(end % 1 * 1000):03}"

    # SRT形式の文字列に追加
    srt_output += f"{i + 1}\n{start_srt} --> {end_srt}\n{text}\n\n"


# SRTファイルへの書き出しパス
srt_file_path = '/content/translated_subtitles.srt'

with open(srt_file_path, "w") as file:
    file.write(srt_output)