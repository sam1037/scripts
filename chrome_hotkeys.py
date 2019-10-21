import pyautogui as pg
import psutil
from pynput import keyboard
from pynput.keyboard import Key, KeyCode
from chrome_hotkeys_funcs import *
from photkey_script_funcs import *

current_keys = set()


hotkeys_to_funcs={frozenset([KeyCode(char='`'), KeyCode(char='b')]): [delete_key_twice, bookmark_process],
                  frozenset([Key.tab, Key.left]): [change_web_tab_to_left],  # todo fix not able to use it continuously
                  frozenset([Key.tab, Key.right]): [change_web_tab_to_right],
                  }


def on_press(key):
    print('\nKey {0} pressed'.format(key))
    current_keys.add(key)  # add current key for checking
    #print(current_keys)
    if frozenset(current_keys) in hotkeys_to_funcs:  # if curtain hotkey is pressed
        for func in hotkeys_to_funcs[frozenset(current_keys)]:  # execute functions
            func()



def on_release(key):
    print('Key {0} released'.format(key))
    current_keys.clear()


def listen():
    with keyboard.Listener(on_press=on_press, on_release=on_release) as kl:
        kl.join()


def main():
    while True:  # if chrome is opened, activate the script
        if "chrome.exe" in (p.name() for p in psutil.process_iter()):
            print('main loop')
            listen()
            break


if __name__ == '__main__':
    main()
