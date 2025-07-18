import speech_recognition as sr
import pyttsx3


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
                    audio = r.listen(source)
                    command = r.recognize_google(audio).lower()
                    print(command)

                
        except Exception as e:
            print("Error",e)