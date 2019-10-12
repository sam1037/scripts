import pyautogui as pg
import psutil
from pynput import keyboard
from pynput.keyboard import Key, KeyCode
from chrome_hotkeys_funcs import *
from photkey_script_funcs import *

current_keys = set()


hotkeys_to_funcs={frozenset([KeyCode(char='b')]): [delete_key_once, bookmark_process]
                  }


def on_press(key):
    current_keys.add(key)  # add current key for checking
    #print(current_keys)
    if frozenset(current_keys) in hotkeys_to_funcs:  # if curtain hotkey is pressed
        for func in hotkeys_to_funcs[frozenset(current_keys)]:  # execute functions
            func()


def on_release(key):
    current_keys.clear()


def main():
    with keyboard.Listener(on_press=on_press, on_release=on_release) as kl:
        kl.join()


while True:
    if __name__ == "__main__":
        if "chrome.exe" in (p.name() for p in psutil.process_iter()):
            print('main loop')
            main()
            break
