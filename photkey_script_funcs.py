"""
TIL home key can bring me to the start of the line
"""
import time

import psutil
import pyautogui as pg
import win32con
import win32gui
import os


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

    # if app already exist, bring app to foreground

    # check if app exist
    for p in psutil.process_iter():
        print(p.name())
    print('------------------------')


    if app_exe_file in (p.name() for p in psutil.process_iter()):

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


def close_current_window():
    handle = (win32gui.GetForegroundWindow())  # handle is the process of current window
    win32gui.PostMessage(handle, win32con.WM_CLOSE, 0, 0)


def open_chrome():
    open_app("chrome.exe", "Google Chrome", "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe")


def open_pycharm():
    open_app("pycharm64.exe", "Pycharm",
             "C:\Program Files\JetBrains\PyCharm Community Edition 2019.2.1\\bin\pycharm64.exe")
    # use \\ because \b does some nasty stuff


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


def open_lol():
    open_app('Garena', 'Garena', "C:\Program Files (x86)\Garena\Garena\Garena.exe")



def get_mouse_coords():
    import win32api
    while True:
        time.sleep(0.1)
        x, y = win32api.GetCursorPos()
        print(x,y)


def open_anki():
    open_app("anki.exe", 'anki', "C:\Program Files\Anki\\anki.exe")



