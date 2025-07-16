# Nova-AI-Platform-
Nova is a simple voice-activated virtual assistant built using Python. It listens for voice commands and performs various tasks such as opening websites, playing music, and responding to user input using speech synthesis.
🔧 Features:
Wake Word Activation: Listens for the keyword “Nova” to activate.

Voice Recognition: Uses the speech_recognition library to convert spoken words into text.

Web Automation: Opens popular websites like Google, YouTube, Instagram, and more via simple voice commands.

Music Playback: Integrates with a custom musiclibrary module to play music based on voice commands.

Text-to-Speech: Uses pyttsx3 to provide spoken responses and feedback.

Graceful Exit: Say "stop" to terminate the assistant.

🧠 How It Works:
Nova continuously listens using the system's microphone.

When the wake word “Nova” is detected, it prompts the user for a command.

The command is recognized and processed accordingly—whether it’s opening a website or playing a song.

If the command isn’t recognized, Nova politely asks the user to try again.

📦 Libraries Used:
speech_recognition

pyttsx3

webbrowser

musiclibrary (custom module)
