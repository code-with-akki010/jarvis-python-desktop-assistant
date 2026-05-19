import os
import subprocess
import webbrowser
from datetime import datetime
from pathlib import Path
from urllib.parse import quote_plus

import pyttsx3


# ========== SETUP ==========
engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
engine.setProperty("rate", 170)

WEBSITES = {
    "google": "https://google.com",
    "youtube": "https://youtube.com",
    "gmail": "https://mail.google.com",
    "instagram": "https://instagram.com",
    "whatsapp": "https://web.whatsapp.com",
    "github": "https://github.com",
}

APPS = {
    "notepad": "notepad",
    "calculator": "calc",
    "paint": "mspaint",
    "cmd": "cmd",
}

FOLDERS = {
    "desktop": Path.home() / "Desktop",
    "downloads": Path.home() / "Downloads",
    "documents": Path.home() / "Documents",
    "pictures": Path.home() / "Pictures",
}


# ========== SPEAK ==========
def speak(text):
    print("Jarvis:", text)
    engine.say(text)
    engine.runAndWait()


# ========== HELPERS ==========
def open_website(command):
    for name, url in WEBSITES.items():
        if f"open {name}" in command:
            speak(f"Opening {name}")
            webbrowser.open(url)
            return True

    return False


def open_app(command):
    for name, app in APPS.items():
        if f"open {name}" in command:
            speak(f"Opening {name}")
            subprocess.Popen(app)
            return True

    return False


def open_folder(command):
    for name, folder in FOLDERS.items():
        if f"open {name}" in command:
            if folder.exists():
                speak(f"Opening {name}")
                os.startfile(folder)
            else:
                speak(f"{name} folder was not found")
            return True

    return False


def tell_joke():
    try:
        import pyjokes
    except ImportError:
        speak("Install pyjokes first by running pip install pyjokes")
        return

    speak(pyjokes.get_joke())


# ========== COMMAND ==========
def processCommand(command):
    command = command.lower().strip()

    if not command:
        return

    if open_website(command):
        return

    if open_app(command):
        return

    if open_folder(command):
        return

    if command.startswith("play"):
        song = command.replace("play", "", 1).strip()

        if song:
            speak(f"Playing {song}")
            webbrowser.open(f"https://www.youtube.com/results?search_query={quote_plus(song)}")
        else:
            speak("Say song name")

    elif command.startswith("search youtube"):
        query = command.replace("search youtube", "", 1).strip()

        if query:
            speak(f"Searching YouTube for {query}")
            webbrowser.open(f"https://www.youtube.com/results?search_query={quote_plus(query)}")
        else:
            speak("Say what you want to search on YouTube")

    elif "news" in command:
        speak("Opening today's news")
        webbrowser.open("https://news.google.com/topstories?hl=en-IN&gl=IN&ceid=IN:en")

    elif command in ["time", "what is the time", "current time"]:
        current_time = datetime.now().strftime("%I:%M %p")
        speak(f"The time is {current_time}")

    elif command in ["date", "today date", "what is the date"]:
        current_date = datetime.now().strftime("%d %B %Y")
        speak(f"Today's date is {current_date}")

    elif "joke" in command:
        tell_joke()

    elif command.startswith("tell me about"):
        topic = command.replace("tell me about", "", 1).strip()

        if topic:
            speak(f"Searching about {topic}")
            webbrowser.open(f"https://www.google.com/search?q={quote_plus(topic)}")
        else:
            speak("Say the topic name")

    else:
        speak("Searching Google")
        query = quote_plus(command)
        webbrowser.open(f"https://www.google.com/search?q={query}")


# ========== MAIN ==========
if __name__ == "__main__":
    speak("Initializing Jarvis")

    while True:
        command = input("Type command for Jarvis: ").strip()

        if command.lower() in ["exit", "quit", "stop"]:
            speak("Goodbye")
            break

        processCommand(command)
