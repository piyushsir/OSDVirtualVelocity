import speech_recognition as sr
from googletrans import Translator
def Listen():

    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold=1
        audio=r.listen(source,0,8)
    try:
        print("Recognizing...")
        query=r.recognize_google(audio,language="hi")
    except:
        return ""
    
    query=str(query).lower()
    return query

def Trans(Text):
    line=str(Text)
    translate=Translator()
    result=translate.translate(line)
    data=result.text
    print(f"You : {data}.")
    return data


def Connection():
    query=Listen()
    data=Trans(query)
    return data

print(Connection())
