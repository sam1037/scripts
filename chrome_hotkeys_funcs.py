from photkey_script_funcs import *
from pynput.keyboard import Key, Listener


def click_bookmark(num):  # todo fix not working in not full screen
    import pyautogui as pg

    pg.click(1901, 53, button='left')

    pg.click(1840, 211, button='left')

    pg.click(1460, 345 + (num - 1) * 22, button='left')


def bookmark_process():  # take a number and open certain bookmark
    print('-----------------------------------')
    print('processing')
    print("listening for keystroke")

    current_keys = []

    # listen for once if key input is int
    def on_press(key):
        try:
            current_keys.append(int(key.char))
        except Exception as e:
            print(e)
            print('end')
            return False  # if key input isn't int, end process

    def on_release(key):
        try:
            click_bookmark(num=current_keys[0])
            print('end')
            return False
        except Exception as e:
            print(e)

    with Listener(
            on_press=on_press,
            on_release=on_release) as bookmark_listener:
        bookmark_listener.join()


def change_web_tab_to_left():
    print('change web tab to left')
    pg.hotkey('ctrl', 'shift', 'tab')
    pg.hotkey('tab')


def change_web_tab_to_right():
    print('change web tab to right')
    pg.hotkey('ctrl', 'tab')
    pg.hotkey('tab')


def close_all_but_one_new_tab():
    pg.hotkey('ctrl', 't')
    pg.click(40,10, button='right')
    pg.click(135,190)
    pg.hotkey('ctrl','t')
    pg.hotkey('ctrl', 'shift', 'tab')
    pg.hotkey('ctrl', 'w')
    pg.hotkey('esc')


def open_youtube():
    # todo if website already exist, switch to it istead of bring a new one
    click_bookmark(1)
    time.sleep(1)
    pg.click(880, 130)


def opne_netflix():
    click_bookmark(2)


def open_ticktick():
    click_bookmark(4)



