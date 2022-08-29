import pyttsx3
import datetime
import  speech_recognition as sr
import wikipedia
import webbrowser as wb


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

engine.setProperty('voices',voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("good Morning!")
    elif hour>=12 and hour<18:
        speak("good Afternoon!")
    else:speak("good Evening!")
    speak("Hi iam jarvis how can i help you")


def takecammand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening......")
        r.pause_threshold = 0.5
        audio = r.listen(source)
    try:
        print("Recognizing.......")
        query = r.recognize_google(audio,language ="en-in")
        print(f"User said: {query} \n")
    except Exception as e :
        print(e)

        print("say that again please.......")
        return "none"

    return query





if __name__ == '__main__':
    wishme()
    while True:
        query = takecammand().lower()



        if "wikipedia" in query:
            speak("Searching  wikipedia......")
            query = query.replace("wikipedia","")
            result = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(result)
            speak(result)

        elif "exit" in query:
           # break
            exit()
        elif"open youtube"in query:
            wb.open("youtube.com")

        elif "open google" in query:
            wb.open("google.com")

        elif "open stackoverflow" in query:
            wb.open("stackoverflow.com")











