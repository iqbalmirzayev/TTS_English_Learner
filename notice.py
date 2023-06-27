#!/usr/bin/python3

import os
import glob
import random
from playsound import playsound
import time
# -*- coding: utf-8 -*-


directory = '/home/iqbal/Documents/Python'
pattern = '*.mp3'
mp3_files = glob.glob(os.path.join(directory, pattern))
mp3_files_names = []

for file in mp3_files:
    file_name = os.path.basename(file)
    mp3_files_names.append(file_name)

# Shuffle the list of MP3 file names
random.shuffle(mp3_files_names)

for file_name in mp3_files_names:
    file_path = os.path.join(directory, file_name)
    playsound(file_path)
    time.sleep(1.5)

print("Iqbal")

 
