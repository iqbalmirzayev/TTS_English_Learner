#!/usr/bin/python3
import os
from tkinter_get_words import get_words_2
from gtts import gTTS
texta2=get_words_2()
print(texta2)
language="en"
for i in range(len(texta2)):

    speech= gTTS(text=texta2[i],lang=language,slow=False,tld="com.au")
    
    speech.save("{}/Documents/Python/{}.mp3".format(os.environ.get("HOME") ,texta2[i]))
