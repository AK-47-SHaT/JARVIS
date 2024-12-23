import webbrowser
import pyttsx3
import speech_recognition as sr




r = sr.Recognizer()
engine=pyttsx3.init()



def speak(text):
    engine.say(text)
    engine.runAndWait()






def process(command):
    if"open google" in command.lower():
          webbrowser.open("http:\\google.com")

    elif"shut up" in command.lower():
        speak("ari pup")      
    elif"open youtube" in command.lower():
        webbrowser.open("https://www.youtube.com/")
        speak("okay")    
    listen()
     

def takingCommand():
    try:
        with sr.Microphone() as source:
            print("Say something!")
            audio = r.listen(source)
        command = r.recognize_google(audio)
        process(command)
                                    #speak("I thinks you said " + r.recognize_google(audio))
    except Exception as e :
        print(e)
        speak("could not lisen command")
        takingCommand()


    
def listen():
    # obtain audio from the microphone
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)



    # recognize speech using Google Speech Recognition
    try:
        if( r.recognize_google(audio).lower()=="jarvis"):
         speak("ya")
         print(f"you: {r.recognize_google(audio)}")
         print("jarvis: ya")
         takingCommand()
        
    except sr.UnknownValueError:
        print("I could not understand jarvis")
        listen()
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

        listen()

while(True):
    listen()        
