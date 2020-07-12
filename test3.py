from pynput import keyboard
from pynput.keyboard import KeyCode, Key
from photkey_script_funcs import delete_key_once


def deleteKeyOnce():
    import pyautogui as pg
    pg.press("backspace")

def on_press(key):
    print(f"{key} key pressed")
    if not key == Key.backspace:
        deleteKeyOncea()

def on_release(key):
    print(f"{key} key released")

def listen():
    with keyboard.Listener(on_press=on_press, on_release=on_release) as k:
        k.join()

import pyautogui
import time
time.sleep(3)
pyautogui.press("backspace")