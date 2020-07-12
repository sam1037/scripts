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


hotkeys_to_funcs={frozenset([KeyCode(char='`'), KeyCode(char='b')]):
                      [bookmark_process],
                  frozenset([Key.tab, Key.left]):
                      [change_web_tab_to_left],
                  frozenset([Key.tab, Key.right]):
                      [change_web_tab_to_right],
                  frozenset([KeyCode(char='`'), Key.delete]):
                      [close_all_but_one_new_tab],
                  frozenset([KeyCode(char='`'), KeyCode(char="1"), Key.delete]):
                      [close_other_tabs],
                  frozenset([KeyCode(char='`'), KeyCode(char='y')]):
                      [youtube.open],
                  frozenset([KeyCode(char='`'), KeyCode(char="1"),KeyCode(char='y')]):
                      [youtube.open_in_new],
                  frozenset([KeyCode(char='`'), KeyCode(char='t')]):
                      [ticktick.open],
                    frozenset([KeyCode(char='`'), KeyCode(char='1'),KeyCode(char='t')]):
                      [ticktick.open_in_new],
                  frozenset([KeyCode(char="`"), KeyCode(char="x")]):
                      [delete_key_once, psf.close_current_window],
                  frozenset([KeyCode(char="`"), KeyCode(char="l")]):
                      [delete_key_once, leetcode.open],
                  frozenset([KeyCode(char="`"), KeyCode(char="1"), KeyCode(char="l")]):
                      [delete_key_once, leetcode.open_in_new],
                  }


def on_press(key):
    print('\nKey {0} pressed'.format(key))
    current_keys.add(key)  # add current key for checking
    #print(current_keys)


def on_release(key):
    s_time = time.time()
    # if curtain hotkey is pressed
    if frozenset(current_keys) in hotkeys_to_funcs:
        print('-' * 120)
        # execute functions
        for func in hotkeys_to_funcs[frozenset(current_keys)]:
            func()
        time_used = round((time.time() - s_time), 5)
        # give information
        print('{0} second used to \nexecute {1}'.format(time_used, (hotkeys_to_funcs[frozenset(current_keys)])))
        print('\n'+'-' * 120)
    current_keys.clear()


def listen():
    with keyboard.Listener(on_press=on_press, on_release=on_release) as kl:
        kl.join()


def main():
    listen()


if __name__ == '__main__':
    main()

