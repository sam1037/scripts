"""
"""
import time

import psutil
import pyautogui as pg
import win32con
import win32gui
import os
import time


def maximaze_current_window():
    pg.click(x=960, y=540)
    pg.hotkey("winleft", "up")
    handle = (win32gui.GetForegroundWindow())  # handle is the process of current window
    win32gui.ShowWindow(handle, win32con.SW_MAXIMIZE)


def delete_key(times):
    #time.sleep(0.0001)
    for cycle in range(times):
        pg.press("backspace")


def open_app(app_exe_file, app_name, app_path):
    s_time = time.time()

    # if app already exist, bring app to foreground

    if app_exe_file in (p.name() for p in psutil.process_iter()):  # check if app exist

        import win32gui

        # switch app
        def windowEnumerationHandler(hwnd, top_windows):
            top_windows.append((hwnd, win32gui.GetWindowText(hwnd)))

        top_windows = []  # this list contains all the tasks and its name
        win32gui.EnumWindows(windowEnumerationHandler, top_windows)
        for i in top_windows:
            #print(i[1])
            if app_name in i[1]:  # if the task name is equal to the name we needed
                try:
                    win32gui.ShowWindow(i[0], 5)
                    win32gui.SetForegroundWindow(i[0])
                    maximaze_current_window()
                    print('switch to {0}'.format(i[1]))
                    break
                except Exception as e:
                    print(e)


    else:  # open app if app doesn't exist
        try:
            print("open {0}".format(app_name))
            os.startfile(app_path)
            maximaze_current_window()
        except Exception as error_msg:
            print(error_msg)

    time_used = round((time.time() - s_time), 5)
    print('Used {0} second to finished process'.format(time_used))


def close_current_window():
    handle = (win32gui.GetForegroundWindow())  # handle is the process of current window
    win32gui.PostMessage(handle, win32con.WM_CLOSE, 0, 0)
    # for open_chrome func
    try:
        if handle == chrome_handle:
            global chrome_opened
            del chrome_opened
    except Exception as e:
        print(e)


def delete_key_once():
    delete_key(1)


def delete_key_twice():
    delete_key(2)


def delete_key_thrice():
    delete_key(3)


def select_and_search():
    pg.hotkey('ctrl', 'c')
    pg.hotkey("ctrl", 't')
    pg.hotkey('ctrl','v')
    pg.hotkey('enter')

def get_mouse_coords():
    import win32api
    while True:
        time.sleep(0.1)
        x, y = win32api.GetCursorPos()
        print(x,y)

def lol_get_top():
    pg.click(500,860)
    time.sleep(0.01)
    pg.typewrite('top')
    time.sleep(0.01)
    pg.hotkey('enter')

class App():
    def __init__(self, barnum):
        self._barnum = barnum
        # the barnum of file_explorer is 1, mc is 2

    def open(self):
        # todo if current app is the app, don't switch
        if self._barnum == 10:
            num = 0
        else:
            num = self._barnum

        if self._barnum < 11:
            pg.hotkey('winleft', str(num))
        else:
            pos = pg.position()
            pg.click((410 + num * 48), 1050)
            pg.moveTo(pos[0], pos[1])


netflix = App(8)
anki = App(6)
file_explorer = App(7)
chrome = App(3)
vscode = App(10)
pycharm = App(5)
lol = App(9)

