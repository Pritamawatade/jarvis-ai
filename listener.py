import speech_recognition as sr
from rich import print

recognizer = sr.Recognizer()

def listen():
    with sr.Microphone() as source:
        print("[cyan]🎤 Listening...[/cyan]")
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio)
        print(f"[green]You said:[/green] {text}")
        return text.lower()
    except:
        return ""

