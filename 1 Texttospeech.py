import pyttsx3
import speech_recognition
import pyaudio
import webbrowser

i = speech_recognition.Recognizer()

def SpeakText(command):

    engine = pyttsx3.init()
    rate = engine.getProperty('rate')
    engine.setProperty('rate',rate-80)
    engine.say(command)
    engine.runAndWait()

def Listen():
    with speech_recognition.Microphone() as source2:

        i.adjust_for_ambient_noise(source2,duration=1)
        SpeakText("What do you need me to do")

        audio2 = i.listen(source2)

        try:
            Mytext = i.recognize_google(audio2)
            Mytext = Mytext.lower()
            print(Mytext)

        except:
            SpeakText("Didnt understand you")
            SpeakText("Try again")
            Listen()
            return
    if Mytext.__contains__("youtube"):
        with speech_recognition.Microphone() as source2:
            SpeakText("What video do you want to see?")
            i.adjust_for_ambient_noise(source2, duration=1)

            audio2 = i.listen(source2)

            try:
                video = i.recognize_google(audio2)
            except:
                SpeakText("Didnt understand you")
                SpeakText("Try again")
                Listen()
                return
            video = video.lower()

            SpeakText("Searching"+video)

        webbrowser.open('https://www.youtube.com/results?search_query='+ video)
Listen()