import ctypes

# Suppress noisy ALSA internal messages on systems without a configured sound card.
# Using a no-op C callback is more robust than passing None on some systems.
try:
    libasound = ctypes.cdll.LoadLibrary("libasound.so.2")
    # C signature: void (*handler)(const char *fmt, va_list ap)
    CB = ctypes.CFUNCTYPE(None, ctypes.c_char_p, ctypes.c_void_p)
    def _noop(fmt, ap):
        return
    # Keep a reference to the callback alive to avoid it being GC'd which can
    # cause a segmentation fault when libasound later calls it.
    _alsa_cb = CB(_noop)
    libasound.snd_lib_error_set_handler(_alsa_cb)
except Exception:
    # If libasound isn't available or handler isn't found, just continue — this
    # is a non-fatal convenience measure to reduce console noise.
    pass

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
        print(f"[yellow]⚠️  Skipped (no 'jarvis' keyword): {text}[/yellow]")
        continue

    intent = detect_intent(text)

    if intent == "OPEN_APP":
        print(f"intent = {intent}")
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

