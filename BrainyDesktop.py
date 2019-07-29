import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voice',voices[0].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def sendEmail(to,content):
    server=smtplib.SMTP("smtp.gmail.com",587)
    server.ehlo()
   # server.startls()
    server.login("shivanigoyal616@gmail.com","pwd here")
    server.sendmail('shivanigoyal616@gmail.com',to,content)
    server.close()
    


def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning:")
    elif hour>=12 and hour<18:
        speak("Good Afterneechoon:")
    else:
        speak("Good Evening:")
    speak("I am Brainy.Please tell me how can i help you")
def takeCommand():
    # it takes microphone input and returns string
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold=1
        audio=r.listen(source)
    
    try:
        print("Recognizing...")
        query=r.recognize_google(audio)
        print(f"User said:{query}\n")
    
    except Exception as e:
      #  print(e)

        print("Say it again please...")
        return "None"
    return query
if __name__ == "__main__":
    wishMe()
    while True:
        query=takeCommand().lower()

        #logic for installing task based on query
        if 'wikipedia' in query:
            speak("Searching wikipedia...")
            query=query.replace("wikipedia","")
            results=wikipedia.summary(query,sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'play music' in query:
            music_dir="" #path
            songs=os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[0]))
        elif 'time' in query:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {strTime}")
        elif 'open code' in query:
            codePath="C:\\Users\\hp\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)   
        elif 'email to shivani' in query:
            try:
                speak("What should i say?")
                content=takeCommand()
                to="shivanigoyal616@gmail.com"
                sendEmail(to,content)
                speak("Email has been sent")
            except Exception as e:
                print(e)
                speak("Sorry my friend,I m not able to send the mail")



            


    




