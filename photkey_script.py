"""
Testing testing

"""

from pynput import keyboard, mouse
from pynput.keyboard import Key, KeyCode
from photkey_script_funcs import *
import ctypes


ctypes.windll.kernel32.SetConsoleTitleW("Photekey_script")  # change cmd name


def test():
    print("test")

current_keys = set()

hotkeys_to_funcs = {  # list of hotkey and its particular function
    frozenset([KeyCode(char="`"), KeyCode(char="x")]): [delete_key_once, close_current_window],
    frozenset([KeyCode(char="`"), KeyCode(char="p")]): [delete_key_once, open_pycharm],
    frozenset([KeyCode(char="`"), KeyCode(char="g")]): [select_and_search],
    frozenset([KeyCode(char="`"), KeyCode(char="l")]): [delete_key_once, open_lol],
    frozenset([KeyCode(char="`"), KeyCode(char="a")]): [delete_key_once, open_anki],
    # todo create more hotkeys:


}


def on_press(key):
    current_keys.add(key)  # add current key for checking
    #print(current_keys)


def on_release(key):
    s_time = time.time()
    # if curtain hotkey is pressed
    if frozenset(current_keys) in hotkeys_to_funcs:
        print('-'*120)
        # execute functions
        for func in hotkeys_to_funcs[frozenset(current_keys)]:
            func()
        time_used = round((time.time()-s_time),5)
        # give information
        print('{0} second used to \nexecute {1}'.format(time_used, (hotkeys_to_funcs[frozenset(current_keys)])))
        print('\n'+'-'*120)
    current_keys.clear()

def main():
    with keyboard.Listener(on_press=on_press, on_release=on_release) as kl:
        kl.join()


if __name__ == "__main__":
    main()
