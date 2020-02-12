import eel
import sqlite3
import ctypes
import time
import speech_recognition as sr
from gtts import gTTS
import requests
import playsound
import os
from io import BytesIO
from io import StringIO
import sys

vDecision =''

num = 2
def assistant_speaks(output):
    global num
    
    toSpeak = gTTS(text=output, lang='en-US', slow=False)
    file = str(num)+".mp3"
    toSpeak.save(file)
    playsound.playsound(file, True)
    if os.path.isfile(file):
      os.remove(file)
    num +=1



@eel.expose
def name_entry(vName):
    conn = sqlite3.connect('Register.db')
    c=conn.cursor()
    vName = vName.title()
    c.execute("Select * FROM RegName WHERE (name=?)",(vName,))
    entry = c.fetchone()
    if entry is None:
        c.execute("INSERT INTO RegName (name) Values(?)",(vName,))
        vDecision = '1'
        assistant_speaks("Welcome"+vName+", We love having you with us.")
        print(vName)
    else:
        vDecision = '2'
        assistant_speaks('Welcome back'+vName+'Good to see you again')
        print(vName)
        
    conn.commit()
    c.close()
    conn.close()
    sys.exit(0)


def on_close(page, sockets):
	print(page, 'closed and'+sockets)


assistant_speaks('Hello Human,Please enter your name.')
eel.init('web')
eel.start('main.html', size=(900, 700),callback=on_close,host="localhost", port=3333 , disable_cache=True)
#assistant_speaks('Hello Human,Please enter your name.')
#eel.start('main.html', size=(900, 700), disable_cache=True)
#ctypes.windll.user32.MessageBoxW(0, vName, "Message", 1)







        


