"""
Testing testing

"""

# todo run script constantly

from pynput import keyboard, mouse
from pynput.keyboard import Key, KeyCode
from photkey_script_funcs import *

run_hotkey = False


def test():
    print("test")
    print("test again")
    print('is there an git update????????????????')

current_keys = set()

hotkeys_to_funcs = {  # list of hotkey and its particular function
    frozenset([KeyCode(char="c")]): [delete_key_once, open_chrome],
    frozenset([KeyCode(char="x")]): [delete_key_once, close_current_window],
    frozenset([KeyCode(char="p")]): [delete_key_once, open_pycharm],
    frozenset([KeyCode(char="g")]): [delete_key_once, select_and_search],
    frozenset([KeyCode(char="l")]): [delete_key_once, open_lol],

    # todo create more hotkeys:
}


def on_press(key):
    current_keys.add(key)  # add current key for checking
    #print(current_keys)
    if frozenset(current_keys) in hotkeys_to_funcs:  # if curtain hotkey is pressed
        if run_hotkey:
            for func in hotkeys_to_funcs[frozenset(current_keys)]:  # execute functions
                func()


def on_release(key):
    current_keys.clear()


def main():

    #minimaze cmd

    from pynput import mouse

    def on_click(x, y, button, pressed):
        global run_hotkey
        if pressed:
            if button == mouse.Button.middle:
                run_hotkey = True
        else:
            run_hotkey = False

    with mouse.Listener(on_click=on_click) as ml, keyboard.Listener(on_press=on_press, on_release=on_release) as kl:
        ml.join()
        kl.join()


if __name__ == "__main__":
    main()