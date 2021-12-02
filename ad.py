"""Giving data and gui are left only """
import pyttsx3
import speech_recognition as sr
import datetime

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"Patient said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query

def disease():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("I am Your doctor. Please tell me how may I help you")    
    speak("From which disease you are suffering from?")
    print("From which disease you are suffering from?")   


if __name__=="__main__":
    patient = takeCommand().lower()
    if 'fever' in patient:
        with open("fever.txt") as r:
            a= r.read()
            print(a)
    elif "" in patient:
        with open('.txt') as r:
            a= r.read()
            print(a)
    elif "" in patient:
        with open('.txt') as r:
            a= r.read()
            print(a)
    elif "" in patient:
        with open('.txt') as r:
            a= r.read()
            print(a)
