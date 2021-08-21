# Jarvis : Personal Assistant built using python libraries

import pyttsx3  # pip install pyttsx3 
import datetime



engine = pyttsx3.init()
voices = engine.getProperty('voices')       
engine.setProperty('voice', voices[1].id)

def speak(audio): 
    engine.say(audio)
    engine.runAndWait()

"""speak ("Hello! This is python assistant tutorial")"""


def time():
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak("the current time is")
    speak(Time)

"time()"

def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    speak("the current date is")
    speak(date)
    speak(month)
    speak(year)

"date()"

def wishme():
    speak("Wwlcome back sir!")
    time()
    date()
    hour = datetime.datetime.now().hour

    if hour >=6 and hour <=12:
        speak("Good morning")
    elif hour >=12 and hour < 18:
        speak("Good afternoon")
    elif  hour >=18 and hour <=24:
        speak("Good evening")
    else:
        speak("Good night")

    speak("Jarvis at your service, How I can help you?")

wishme()