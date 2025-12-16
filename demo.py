# import webbrowser

# # Open the YouTube homepage in the default web browser
# url = "https://www.youtube.com"
# webbrowser.open(url, new=1)
import subprocess

result = subprocess.run(["xdg-open", "https://youtube.com"], 
                                     stdout=subprocess.PIPE, 
                                     stderr=subprocess.PIPE)