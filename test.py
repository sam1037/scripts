def main():
    from pynput import mouse

    def on_click(x, y, button, pressed):
        if pressed:
            print(x,y)

    with mouse.Listener(on_click=on_click) as l:
        l.join()


#main()


"""
import pyautogui as pg
import time

pg.hotkey('winleft')

pg.typewrite('chrome\n', 0.1)

time.sleep(1)

pg.typewrite('www.youtube.com\n')

pg.hotkey('winleft', 'up')
"""


def bk(num):
    import pyautogui as pg
    import pynput

    pg.hotkey('winleft')

    pg.typewrite('chrome\n', 0.1)

    pg.hotkey('winleft', 'up')

    pg.click(1901, 53, button='left')

    pg.click(1840,211, button='left')


bk(1)