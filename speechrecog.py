import speech_recognition as sr

def speech_tr():
    # obtain audio from the microphone
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)

    return(r.recognize_google(audio, language= 'tr-TR'))

#text=speech_tr()
#print(text)
