#python -m pip install --upgrade pip
#python -m pip  install clipboard
#python -m pip install pynput

import pyperclip as pc
from pynput.keyboard import Key, Controller
import time

keyboard = Controller()

paste_list = []

while True:
    coord = input()
    if coord != '.':
        paste_list.append(coord)
    else:
        break

time.sleep(5)

for item in paste_list:
    for char in item:
        keyboard.press(char)
    keyboard.press(Key.enter)
    

    
  
