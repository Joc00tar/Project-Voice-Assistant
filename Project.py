

import speech_recognition as sr
from time import ctime
import time
import os
from gtts import gTTS

def speak(audioString):
    print(audioString)
    tts = gTTS(text=audioString, lang='en')
    tts.save("audio.mp3")
    os.system("mpg123 audio.mp3")

def recordAudio():
# Record Audio
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)
 
    # Speech recognition using Google Speech Recognition
    data = ""
    try:
    # Uses the default API key
    # To use another API key: `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
        data = r.recognize_google(audio,language="Th")
        print("You said: " + data)
    except sr.UnknownValueError:
        speak("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
    
    return data
 
def dekdoydev(data):
    if "AI" in data or"Hello" in data:
        speak("May I help you? ")

    
    if "What time" in data:
        speak(ctime())

    if "covid News" in data:
        speak("okay")
        os.system("start https://www.google.com/search?q=covid-19&oq=covid&aqs=chrome.0.0j69i57j0l6.4783j0j15&sourceid=chrome&ie=UTF-8")
    # My friend Profile facebook 

    if "Mickey Profile" in data:
        speak("okay")
        os.system("start https://web.facebook.com/mixky.inthavongtham.9")

    if "Viva Profile" in data:
        speak("okay")
        os.system("start  https://web.facebook.com/vi.vilaiphone.1")

    if "ส่องสาว" in data:
        data = data.split(" ")
        speak("She is so cutest")
        os.system("start https://web.facebook.com/tatar.souvannasing")
    # whiching Movie 

    if "Netfix" in data:
        data = data.split(" ")
        speak("okay on Netfix")
        os.system("start https://www.netflix.com/la/login?nextpage=https%3A%2F%2Fwww.netflix.com%2Fbrowse")
    # listen to Music

    if "On joox" in data or "on joox" in data:
        speak("Okay on joox")
        os.system("start https://www.joox.com/intl")
        
    if "on youtube" in data or "On youtube" in data:
        speak("Okay on youtube")
        os.system("start https://www.youtube.com/watch?v=KBtk5FUeJbk&list=RDKBtk5FUeJbk&start_radio=1")
    #Open website

    if "open YouTube" in data or "open youtube" in data:
        speak("okay")
        os.system("start https://www.youtube.com/")

    if "Research Bird Pictures" in data:
        speak("ReSearching")
        os.system("start https://pixabay.com/images/search/bird/")

    if "open Facebook" in data:
        speak("okay opening")
        os.system("start https://web.facebook.com/?_rdc=1&_rdr")
    #Create folders
    
    if "create folder" in data:
        speak("What do you want to name the folder?")

    elif "New" in data:
        speak("Building folder"+ data)
        os.mkdir(''+data)

    if "rename folder" in data:
        speak("What do you want to rename the folder?")
    elif "folder new" in data:
        speak("How would you like to give it a new folder name?")
    if "rename to Test" in data:
        data = data.replace("rename to"," ")
        os.renames("New","" +data)




# Starting Conversation
time.sleep(2)
speak("Hello boss can I help you?")

while 1:
    data = recordAudio()
    dekdoydev(data)