# Jarvis - Python Desktop Assistant

![Jarvis Python Desktop Assistant](assets/jarvis-banner.png)

Jarvis is a simple Python desktop assistant that works through typed terminal commands. It can open websites, launch Windows applications, open common folders, search YouTube, open Google News, tell the current time and date, tell programming jokes, and search Google for anything it does not recognize.

This version is designed to be reliable on desktops and laptops without needing a microphone, speech recognition, API keys, or paid AI services.

## Features

- Open popular websites such as Google, YouTube, Gmail, Instagram, WhatsApp Web, and GitHub.
- Launch Windows apps such as Notepad, Calculator, Paint, and Command Prompt.
- Open common folders such as Desktop, Downloads, Documents, and Pictures.
- Play or search songs on YouTube.
- Open today's top stories on Google News.
- Tell the current time and date.
- Tell random programming jokes using `pyjokes`.
- Search Google for unknown commands or custom questions.
- Exit cleanly from the terminal.

## Tech Stack

- **Python**
- **pyttsx3** for text-to-speech output
- **pyjokes** for random programming jokes
- **webbrowser** for opening websites and searches
- **subprocess** for launching desktop apps
- **datetime** for time and date commands
- **pathlib** and **os** for opening common folders

## Installation

Clone the repository or download the project files.

Install the required Python packages:

```powershell
pip install pyttsx3 pyjokes
```

If `pyttsx3` has voice issues on your system, make sure Windows text-to-speech voices are installed and enabled.

## How To Run

Open a terminal in the project folder and run:

```powershell
python main.py
```

You should see:

```text
Jarvis: Initializing Jarvis
Type command for Jarvis:
```

Now type a supported command and press Enter.

## Supported Commands

| Command | Action |
| --- | --- |
| `open google` | Opens Google |
| `open youtube` | Opens YouTube |
| `open gmail` | Opens Gmail |
| `open instagram` | Opens Instagram |
| `open whatsapp` | Opens WhatsApp Web |
| `open github` | Opens GitHub |
| `open notepad` | Opens Notepad |
| `open calculator` | Opens Calculator |
| `open paint` | Opens Microsoft Paint |
| `open cmd` | Opens Command Prompt |
| `open desktop` | Opens the Desktop folder |
| `open downloads` | Opens the Downloads folder |
| `open documents` | Opens the Documents folder |
| `open pictures` | Opens the Pictures folder |
| `play believer` | Searches YouTube for the song |
| `search youtube python tutorial` | Searches YouTube for a topic |
| `news` | Opens Google News top stories |
| `time` | Tells the current time |
| `date` | Tells today's date |
| `joke` | Tells a random programming joke |
| `tell me about virat kohli` | Searches Google for the topic |
| `exit` | Stops Jarvis |
| `quit` | Stops Jarvis |
| `stop` | Stops Jarvis |

## Example Usage

```text
Type command for Jarvis: open notepad
Jarvis: Opening notepad

Type command for Jarvis: time
Jarvis: The time is 02:30 AM

Type command for Jarvis: joke
Jarvis: [random joke from pyjokes]

Type command for Jarvis: tell me about artificial intelligence
Jarvis: Searching about artificial intelligence
```

## Project Structure

```text
project-3 jarvis/
├── assets/
│   └── jarvis-banner.png
├── main.py
└── README.md
```

## Notes And Limitations

- This version uses typed terminal commands.
- Voice recognition was removed because the project should work reliably without a microphone.
- Hugging Face API, NewsAPI, and screenshot features were removed or replaced to avoid API-key issues and unreliable behavior.
- Some commands are Windows-specific, especially app launching and folder opening.
- The `play` command opens YouTube search results instead of directly controlling YouTube playback.

## Future Improvements

- Add a graphical user interface.
- Add a command history feature.
- Add custom user-defined shortcuts.
- Add support for more Windows apps.
- Add cross-platform support for macOS and Linux.
- Add optional voice input only when a microphone is available.

## Author

Built as a Python desktop assistant project.

If you like this project, consider giving it a star on GitHub.
