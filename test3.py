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

def get_path(func):  
     if type(func).__name__ == 'function' : 
         return func.__code__.co_filename
     else: 
         raise ValueError("'func' must be a function") 


a = get_path(deleteKeyOnce)
print(a)