import pyttsx3 
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser 

engine = pyttsx3.init()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def time():
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak("the current time is")
    speak(Time)

def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    speak("the current date is")
    speak(date)
    speak(month)
    speak(year)

def wishme():
    speak("Welcome back sir!")
    time()
    date()
    hour = datetime.datetime.now().hour
    if hour>+6 and hour<12:
        speak("Good Morning sir!")
    elif hour>=12 and hour <18:
        speak("Good Afternoon sir!")
    elif hour>=18 and hour <24:
        speak("Good Evening sir!")
    else:
        speak("Good Night sir!")

    speak("Jarvis at your service. Please tell me how may I help you?")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in') 
        print(query) 

    except Exception as e: 
        print("Say that again please...")  
        return "None" 
    return query

if __name__ =="__main__":
    wishme()
    while True:
        query = takeCommand().lower()

        if 'time' in query:
            time()
        elif 'date' in query:
            date()
        elif 'wikipedia' in query:
            speak("Searching....")
            query = query.replace("wikipedia", "")
            #result  = wikipedia.search(query)
            result = wikipedia.summary(query, sentences=2)
            print(result)
            speak(result)
        
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        
        

        
        elif 'offline' in query:
            quit()
          





     