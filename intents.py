def detect_intent(text):
    if "open" in text:
        return "OPEN_APP"
    if "delete" in text:
        return "DELETE_FILE"
    if "todo" in text:
        return "READ_TODOS"
    if text.startswith("jarvis"):
        return "GENERAL"
    return "UNKNOWN"

