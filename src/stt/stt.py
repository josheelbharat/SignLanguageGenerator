import speech_recognition as sr

def stt_from_audio(audio_file):
    recognizer = sr.Recognizer()
    with sr.AudioFile(audio_file) as source:
        audio = recognizer.record(source)
    try:
        return recognizer.recognize_vosk(audio, language='en-in')  # Update with Assamese model
    except sr.UnknownValueError:
        return "Unknown"