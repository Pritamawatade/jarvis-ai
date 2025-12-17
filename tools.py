import os
import subprocess
from rich import print

def open_app(text):
    """
    Dynamically opens websites/URLs based on user command.
    Handles commands like: "open youtube", "open twitter", "open google.com", etc.
    """
    # Remove common words to extract the target
    words = text.lower().split()
    
    # Find the word after "open"
    try:
        open_index = words.index("open")
        if open_index + 1 < len(words):
            target = words[open_index + 1]
            
            # Remove common TLDs if user said them (e.g., "open youtube dot com")
            target = target.replace("dot", ".").replace(",", "")
            
            # Build the URL
            if target.startswith("http://") or target.startswith("https://"):
                url = target
            elif "." in target:
                # User said something like "peerlist.io" or "udemy.com"
                url = f"https://{target}"
            else:
                # User said just a name like "youtube", "twitter", "google"
                # Map common sites or default to .com
                common_sites = {
                    "youtube": "https://youtube.com",
                    "twitter": "https://twitter.com",
                    "x": "https://x.com",
                    "google": "https://google.com",
                    "discord": "https://discord.com",
                    "linkedin": "https://linkedin.com",
                    "github": "https://github.com",
                    "reddit": "https://reddit.com",
                    "facebook": "https://facebook.com",
                    "instagram": "https://instagram.com",
                }
                
                url = common_sites.get(target, f"https://{target}.com")
            
            # Open the URL
            subprocess.Popen(["xdg-open", url])
            return f"Opening {target}"
    except (ValueError, IndexError):
        pass
    
    return "Could not determine what to open"

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

