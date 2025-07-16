Nova is a lightweight, voice-activated desktop assistant developed in Python. It responds to spoken commands to perform basic tasks like opening websites or playing music. With simple voice interaction, Nova makes hands-free control of your computer easy and efficient.

💻 How It Works
 
   Wake Word Detection: Nova continuously listens for the wake word "Nova" using your microphone.
    Speech Recognition: Once activated, it captures the next spoken command using the speech_recognition library and converts it into text.
    Command Processing: Based on the recognized text, Nova checks for predefined commands and performs the appropriate action.
    Speech Response: Using pyttsx3, Nova speaks back to the user for confirmation or feedback.

🔧 Feature
   
    ✅ Voice-activated with the keyword “Nova”

    ✅ Opens popular websites like:

      Google, YouTube, Facebook, Instagram, Twitter, WhatsApp

    ✅ Plays music via a customizable musiclibrary module

    ✅ Responds to user with speech (TTS)
    
    ✅ Gracefully exits when the user says "stop"

    ✅ Basic error handling for unrecognized input

🧠 Technologies Used
  Python

    speech_recognition – for converting voice to text

    pyttsx3 – for text-to-speech feedback

    webbrowser – to open websites

    musiclibrary – custom module mapping song names to URLs

🚀 Usage
Run the script.

  Say “Nova” to activate the assistant.
  Speak a command like:
  "Open YouTube"
  "Play [song name]"
  "Stop" to exit


