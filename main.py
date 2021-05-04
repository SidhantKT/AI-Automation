import webbrowser
import os
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import smtplib
engine = pyttsx3.init('sapi5')

voices= engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('email','pswd')
    server.sendmail('email', to, content)
    server.close()


def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("good morning!")
    elif hour>=12 and hour<18:
        speak("good afternoon")
    else:
        speak("good evening")
    speak("okay so waht i have to do")

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening you...")
        r.pause_threshold =1
        audio = r.listen(source)

    try:
        print("recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}\n")
    except Exception as e:
        print(e)
        print("say that again please")
        return "none"
    return query

if __name__ == "__main__":
    wishMe()
    while True:
        query = takecommand().lower()
        if query == 'ramu kaka stop listening':
            break
        #logic starts here:

        if 'wikipedia' in query:
            speak('Searching Wikipedia....')
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'play music' in query:
            music_dir = ''
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]) )
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"time is {strTime}\n")
            print(strTime)
        elif 'open code' in query:
            codePath = ""
            os.startfile(codePath)
        elif 'email to airforce' in query:
            try:
                speak("what should i say?")
                content = takecommand()
                to = "email-id"
                sendEmail(to,content)
                speak("email has been sent!")
            except Exception as e:
                print(e)
                speak("sorry brother i was not able to send it this time ")
