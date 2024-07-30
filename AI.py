import pyaudio
import pyttsx3 
import speech_recognition as sr 
import datetime
import webbrowser
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("I am Jarvis Sir. Please tell me how may I help you")       

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
            
        print("Say that again please...")  
        return "None"
    return query

a = 0

if __name__ == "__main__":
    wishMe()
    while (a == 0):
   
        query = takeCommand().lower()

        if 'open youtube' in query:
            webbrowser.open("youtube.com")
            

        elif 'open google' in query:
            webbrowser.open("google.com") 
            


        elif 'play music' in query:
            music_dir = 'C:\\Users\\RAJDEEP\\OneDrive\\Desktop\\Sample song'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))
            

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")
            
        elif "exit" in query:
            speak(f"Exiting")
            a = 1