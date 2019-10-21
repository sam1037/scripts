from photkey_script_funcs import *
from pynput.keyboard import Key, Listener


def choose_bookmark(num):  # todo fix not working in not full screen
    import pyautogui as pg

    pg.click(1901, 53, button='left')

    pg.click(1840, 211, button='left')

    pg.click(1460, 345 + (num - 1) * 22, button='left')

def bookmark_process():  # take a number and open certain bookmark
    time.sleep(0.1)
    print('-----------------------------------')
    print('processing')
    print("listening for keystroke")

    # listen for once if key input is int
    def on_press(key):
        pass

    def on_release(key):
        try:
            key = int(key.char)
            print('on release')

        except ValueError as err:
            print("Expected int input, but didn't get one")

        else:
            choose_bookmark(num=key)

        finally:
            print('End with key {0} pressed\n-----------------------------------'.format(key))
            return False  # end listening, end process

    with Listener(
            on_press=on_press,
            on_release=on_release) as bookmark_listener:
        bookmark_listener.join()


def change_web_tab_to_left():
    print('change web tab to left')
    pg.hotkey('ctrl', 'shift', 'tab')


def change_web_tab_to_right():
    print('change web tab to right')
    pg.hotkey('ctrl', 'tab')

