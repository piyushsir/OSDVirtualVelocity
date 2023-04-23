import os

from Brain.aibrain import ReplyBrain
from Body.listen import Connection
import winsound
import webbrowser

print(">>Starting You Trainer>>")
from Body.speak import speak


def MainExe():
    speak("hello sir")
    speak("i am ready to assist you baby")

    while True:

        data = Connection()
        if len(data) < 2:
            pass
        else:
            data = str(data.lower())
            if data == "sleep" or data == "leep" or data == "eep" or data == "leap" or data == "please" or data == "clip":
                #os.startfile(r"http://127.0.0.1:5000/")
                webbrowser.open(r"http://127.0.0.1:5000/", new=0)
                return
            else:
                if data == "play song":
                    winsound.PlaySound("Stay.wav", winsound.SND_ASYNC)
                    data2 = Connection()
                    data2 = str(data.lower())
                    if data2 == "stop" or data2 == "stop song" or "top song":
                        winsound.PlaySound(None, 0)
                        speak("song has been stopped successfully")

                else:
                    data = str(data)
                    Reply = ReplyBrain(data)
                    speak(Reply)

