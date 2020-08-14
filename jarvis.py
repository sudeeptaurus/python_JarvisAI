import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib
import pyaudio

# Load Microsoft Speak API
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices)
engine.setProperty('voice', voices[0].id)

# Function for speak command
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# Function for identifing time
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
    # It takes microphone input from user and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing....")
        query = r.recognize_google(audio, language='en-in')
        print(f"User Said: {query}\n")
    
    except Exception as e:
        print(e)
        print("Pardon. Say that again..")
        return "None"
    
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password')
    server.sendmail('youemail@gmail.com', to, content)
    server.close()


if __name__ == "__main__":
    # speak("Dhruv is a good Boy")
    wishMe()
    # takeCommand()
    # while True:
    if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak("Searching Wikipedia...")
            query = query.replace("Wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open taurusmail' in query:
            webbrowser.open("webmail.taurusonline.net")

        elif 'open trading' in query:
            webbrowser.open("in.trading.com")

        elif 'play music' in query:
            music_dir = "C:\\Users\\DD\\Music"
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
           strTime = datetime.datetime.now().strftime("%H:%M:%S")
           speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codePath = "C:\\Users\\DD\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
        
        elif 'email to sudeep' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "dnd.sudeep@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Pardon. I am not able to send this Email!")


