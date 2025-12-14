from listener import listen
from intents import detect_intent
from tools import open_app, delete_file
from memory import get_todos
from rich import print

print("[bold magenta]🤖 Jarvis is online[/bold magenta]")

while True:
    text = listen()

    if not text:
        continue

    if "jarvis" not in text:
        continue

    intent = detect_intent(text)

    if intent == "OPEN_APP":
        response = open_app(text)
        print(response)

    elif intent == "READ_TODOS":
        todos = get_todos()
        print("[yellow]Today's Todos:[/yellow]")
        for t in todos:
            print(f" - {t}")

    elif intent == "DELETE_FILE":
        # very naive parsing for now
        words = text.split()
        filename = words[-1]
        response = delete_file(filename, "/home/youruser/Downloads")
        print(response)

    else:
        print("I heard you, but I don't know what to do yet.")

