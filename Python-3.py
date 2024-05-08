import subprocess
import speech_recognition as sr

def extract_audio(video_path, audio_path):
    cmd = ["ffmpeg", "-i", video_path, "-vn", "-ac", "1", "-ar", "16000", "-acodec", "pcm_s16le", audio_path]
    subprocess.run(cmd, capture_output=True)

def transcribe_audio(audio_path):
    recognizer = sr.Recognizer()
    with sr.AudioFile(audio_path) as source:
        audio_data = recognizer.record(source)
    
    try:
        text = recognizer.recognize_sphinx(audio_data)
        print("Transcript: {}".format(text))
    except sr.UnknownValueError:
        print("Sphinx could not understand the audio")
    except sr.RequestError as e:
        print("Sphinx error; {0}".format(e))

# 使用例
video_path = "/Users/natsume/Desktop/sample.mp4"  # 入力の動画ファイルへのパス
audio_path = "output_audio.wav"  # 出力の音声ファイルへのパス
extract_audio(video_path, audio_path)
transcribe_audio(audio_path)