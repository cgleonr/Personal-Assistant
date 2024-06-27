import pyttsx3
from decouple import config
from datetime import datetime
import speech_recognition as sr
from random import choice
from utils import opening_text


USER = config('USER')
BOTNAME = config('BOTNAME')

engine = pyttsx3.init('sapi5') # microsoft speech api (to use voices): https://docs.microsoft.com/en-us/previous-versions/windows/desktop/ee125663(v=vs.85)


# Set rate
engine.setProperty('rate', 190)

# Set volume
engine.setProperty('volume', 1.0)

# Set voice (Female)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id) # 0 = male, 1 = female

def speak(text:str):
    """Used to speak whatever text is passed to the function using the TTS module
    Input:
        text: string, a message to be spoken by the machine
    Output:
        None: audio output
    """
    engine.say(text) # method to create audio output
    engine.runAndWait() # blocks during the event loop, returns when the commands queue is cleared.

def greet_user():
    """Greets the user according to the time and USER value"""
    hour = datetime.now().hour
    if (hour >= 0) and (hour < 12):
        speak(f"Good Morning {USER}")
    elif (hour >= 12) and (hour < 17):
        speak(f"Good afternoon {USER}")
    elif (hour >= 17):
        speak(f"Good Evening {USER}")
    speak(f"I am {BOTNAME}. How may I assist you?")

def take_user_input():
    """Takes user input, recognizes it using speech_recognition module and converts it into text"""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print('Recognizing...')
        query = r.recognize_google_cloud(audio, language='en-us')
        if not 'exit' in query or 'stop' in query:
            speak(choice(opening_text))
        else:
            hour = datetime.now().hour
            if hour >= 21:
                speak("Good night, take care!")
            else:
                speak("Have a good day!")

        exit()
    except Exception:
        speak("Sorry, I could not understand. Could you please say that again?")
        query = 'None'
    return query

if __name__ == "__main__":
    greet_user()
    speak("Both the greet and speak functions ran successfully")
