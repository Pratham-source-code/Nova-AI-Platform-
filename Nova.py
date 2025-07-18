import speech_recognition as sr
import pyttsx3
import webbrowser
import musiclibrary

#Function to execute the command
def processcommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://www.google.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://www.youtube.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://www.facebook.com")
    elif "open instagram" in c.lower():
        webbrowser.open("https://www.instagram.com")
    elif "open twitter" in c.lower():
        webbrowser.open("https://www.twitter.com")
    elif "open whatsapp" in c.lower():
        webbrowser.open("https://web.whatsapp.com")
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musiclibrary.music[song]
        webbrowser.open(link)
    elif "stop" in c.lower():
        speak("Goodbye!")
        exit()
    else:
        speak("Sorry, I didn't understand that command. Please try again.")


engine = pyttsx3.init()

#Function used by machine to speak
def speak(text):
    engine.say(text)
    engine.runAndWait()

#Nova get intialize
if __name__== "__main__":
    speak("Initializing Nova......")
    while True:
        try:
            r = sr.Recognizer()
            print("Processing...")  #Used to indicate the user how to wait for processing
        
            #Command for listeing 
            with sr.Microphone() as source:
                print("Listening...")
                Audio = r.listen(source, timeout=5, phrase_time_limit=3)

            Word = r.recognize_google(Audio).lower()
            
            #When user call Nova then only Nova get start
            if("Nova".lower() in Word):
                speak("Hello,sir how can I help you?")
                with sr.Microphone() as source:
                    print("Activated......")
                    Audio = r.listen(source)
                    Command = r.recognize_google(Audio).lower()

                    processcommand(Command)  #Function is called to run commmand
       
        except sr.UnknownValueError:
            print("Sorry, I did not understand that. Please try again.")
        except Exception as e:
            print("Error",e)