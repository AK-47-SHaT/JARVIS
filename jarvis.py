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
          speak("okay")
    elif"shut up" in command.lower():
        speak("ari pup")      
    elif"open youtube" in command.lower():
        webbrowser.open("https://www.youtube.com/")
        speak("okay")   
       

    listen()


def AIprocess(command):
    from openai import OpenAI
 

'''
client = OpenAI(
  api_key="<Your Key Here>",
 )

  completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a virtual assistant named jarvis skilled in general tasks like Alexa and Google Cloud"},
        {"role": "user", "content": "what is coding"}
    ]
    )

    print(completion.choices[0].message.content)'''
     

def takingCommand():
    try:
        with sr.Microphone() as source:
            print("Say your command!")
            audio = r.listen(source)
        command = r.recognize_google(audio)
        process(command)
                                    #speak("I thinks you said " + r.recognize_google(audio))
    except Exception as e :
        print(e)
        speak("could not lisen command , say again please")
        takingCommand()


    
def listen():
    # obtain audio from the microphone
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("waiting for the wake up word!")
        audio = r.listen(source)



    # recognize speech using Google Speech Recognition
    try:
        if( r.recognize_google(audio).lower()=="jarvis"):
         speak("yes sir yes")
         print(f"you: {r.recognize_google(audio)}")
         print("jarvis: yes sir yes")
         takingCommand()
        
    except sr.UnknownValueError:
        print("say the wakeup word jarvis to activate me")
        listen()
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

        listen()


    

#while(True):
#    listen()         


listen()