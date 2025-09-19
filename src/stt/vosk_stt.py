# src/stt/vosk_stt.py
import os
import wave
import json
from vosk import Model, KaldiRecognizer

def vosk_stt(audio_file, model_path="C:/Users/jboff/Projects/SignLanguageGenerator/vosk-models/vosk-model-small-en-in"):
    if not os.path.exists(model_path):
        print(f"Model not found at {model_path}. Download from https://alpha.cepstral.com/vosk/models")
        return "Error: Model not found"

    model = Model(model_path)
    recognizer = KaldiRecognizer(model, 16000)

    if not audio_file.endswith(".wav"):
        print("Converting audio to WAV...")
        import soundfile as sf
        data, samplerate = sf.read(audio_file)
        sf.write("temp.wav", data, samplerate)
        audio_file = "temp.wav"

    with wave.open(audio_file, "rb") as wf:
        if wf.getnchannels() != 1 or wf.getsampwidth() != 2 or wf.getframerate() != 16000:
            print("Audio must be mono, 16-bit, 16kHz. Please convert using Audacity.")
            return "Error: Invalid audio format"

        while True:
            data = wf.readframes(4000)
            if len(data) == 0:
                break
            if recognizer.AcceptWaveform(data):
                result = json.loads(recognizer.Result())
                print("Recognized:", result.get("text", ""))
                return result.get("text", "")

        result = json.loads(recognizer.FinalResult())
        print("Final Recognized:", result.get("text", ""))
        return result.get("text", "")

if __name__ == "__main__":
    audio_file = "data/audio/hello.wav"
    text = vosk_stt(audio_file)
    print("Transcribed Text:", text)