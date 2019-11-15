import pyautogui as pg
import psutil
from pynput import keyboard
from pynput.keyboard import Key, KeyCode
from chrome_hotkeys_funcs import *
from photkey_script_funcs import *
import photkey_script_funcs as psf
import ctypes


ctypes.windll.kernel32.SetConsoleTitleW("Chrome_hotkey")  # change cmd name

current_keys = set()


hotkeys_to_funcs={frozenset([KeyCode(char='`'), KeyCode(char='b')]): [bookmark_process],
                  frozenset([Key.tab, Key.left]): [change_web_tab_to_left],
                  frozenset([Key.tab, Key.right]): [change_web_tab_to_right],
                  frozenset([KeyCode(char='`'), Key.delete]): [close_all_but_one_new_tab],
                  frozenset([KeyCode(char='`'), KeyCode(char='y')]): [open_youtube],
                  frozenset([KeyCode(char='`'), KeyCode(char='n')]): [opne_netflix],
                  frozenset([KeyCode(char='`'), KeyCode(char='t')]): [open_ticktick],
                  frozenset([KeyCode(char="`"), KeyCode(char="x")]): [delete_key_once, psf.close_current_window]
                  }


def on_press(key):
    print('\nKey {0} pressed'.format(key))
    current_keys.add(key)  # add current key for checking
    #print(current_keys)


def on_release(key):
    if frozenset(current_keys) in hotkeys_to_funcs:  # if curtain hotkey is pressed
        for func in hotkeys_to_funcs[frozenset(current_keys)]:  # execute functions
            func()
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
            #break
        else:
            time.sleep(1)


if __name__ == '__main__':
    main()

