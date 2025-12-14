import os
import subprocess
from rich import print

def open_app(text):
    if "youtube" in text:
        subprocess.Popen(["xdg-open", "https://youtube.com"])
        return "Opening YouTube"

def delete_file(filename, directory):
    path = os.path.join(directory, filename)

    if not os.path.exists(path):
        return "File not found"

    confirm = input(f"Are you sure you want to delete {path}? (yes/no): ")
    if confirm.lower() == "yes":
        os.remove(path)
        return "File deleted"
    else:
        return "Deletion cancelled"

