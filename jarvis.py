import speech_recognition as sr
import webbrowser
import pyttsx3
import requests
import muscLibrary

recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()
    newsapi="8333aadbfea14afe86e252037f972e9b"

def processcommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = muscLibrary.music[song]
        webbrowser.open(link)
    
    elif "news" in c.lower():
        r = requests.get(f"https://newsapi.org/v2/top-headlines?country=in&apiKey=8333aadbfea14afe86e252037f972e9b")
        if r.status_code == 200:
            data = r.json()

        articles = data.get('articles',[])

        for article in articles:
            speak(article['title'])

    
    else:
        #let OpenAI handel the request.
        pass
    
        

if __name__ == "__main__":
    speak("Initialising jarvis......")
    while True:
        # listen for the wake word jarvis.
        # obtain audio from the microphone.
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening.......")
            audio = r.listen(source, timeout=2,phrase_time_limit=1)


# recognize speech using Sphinx
        print("recognizing......")
        try:
            with sr.Microphone() as source:
                print("Listening.......")
                audio = r.listen(source, timeout=2,phrase_time_limit=1)
            word = r.recognize_google(audio)
            if word.lower() == "jarvis":
                speak("how can i help you")
                #Listening for command
                with sr.Microphone() as source:
                     print("Jarvis Active.......")
                     audio = r.listen(source)
                     command = r.recognize_google(audio)
                     processcommand(command)

     
        except Exception as e:
               print("Error; {0}".format(e))









