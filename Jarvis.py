import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os



engine = pyttsx3.init('sapi5')
voices= engine.getProperty('voices') 
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio) 
    engine.runAndWait()
def user_name():
    speak ("Hello My name is jarvis what is ur name ")
    name = takeCommand()
    speak(f"Hii {name}\n ")
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak(" what can I do for u ")  

def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        speak("go ahead I am listening ")
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

if __name__ == "__main__":
    user_name()
    wishMe()
    while True:

        query = takeCommand().lower() 


        if 'wikipedia' in query:  
            speak('Searching Wikipedia please wait...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences= 1 ) 
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            speak("opening youtube please wait")
            webbrowser.open("youtube.com")
        
        elif 'open google' in query:
            speak("opening google please wait")
            webbrowser.open("google.com")

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")  
            print(f"Sir, the time is {strTime}")
            speak(f"Sir, the time is {strTime}")
        

        elif 'play music' in query:
            music_dir = 'E:\\Favorite song'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs [2]))
        
        elif 'open code' in query:
            speak("opening VS code please wait")
            code_path = "C:\\Program Files\\Microsoft VS Code\\Code.exe"
            os.startfile(code_path)
        
        elif 'open spotify' in query:
            codePath = "C:\\Users\\Prasad\\AppData\\Roaming\\Spotify\\Spotify.exe"  
        elif "I am not felling well" :
            print("Dont worry things will get better")
            speak("Dont worry things will get better they always do") 
        
        