"""
"""
import time
import pyautogui as pg
import win32con
import win32gui
import os
import time
import pywinauto


def maximaze_current_window():
    pg.click(x=960, y=540)
    pg.hotkey("winleft", "up")
    handle = (win32gui.GetForegroundWindow())  # handle is the id of current window
    win32gui.ShowWindow(handle, win32con.SW_MAXIMIZE)


def delete_key(times):
    #time.sleep(0.0001)
    for cycle in range(times):
        pg.press("backspace")


def open_app(app_name, app_path):
    import win32gui
    import pywinauto
    import win32con
    import subprocess

    def open():
        file = app_path.split("\\")[-1]
        print(file)
        dir = app_path.split("\\")[0:-1]
        dir = "\\".join(dir)
        print(dir)
        os.chdir(dir)
        os.startfile(file)
        print(f"Opened {app_name}")

    def switch(hwnd):
        win32gui.SetForegroundWindow(hwnd)
        win32gui.ShowWindow(w.handle, win32con.SW_MAXIMIZE)
        print(f"Switched to {app_name}")
        return

    windows = pywinauto.Desktop(backend="uia").windows()

    #check if the app is opened
    for w in windows:
        print(w)
        if app_name in w.window_text():
            #bring it to foreground
            switch(w.handle)
            return
    #open the app if it hasn't been opened
    open()
    return


def close_current_window():
    pg.hotkey("alt", "f4")


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
    def __init__(self, barnum=None, name=None, path=None):
        self._barnum = barnum
        self._name = name
        self._path = path
        # the barnum of file_explorer is 1, mc is 2

    def open(self):
        # if current app is the app, do nothing
        if self._name in win32gui.GetWindowText(win32gui.GetForegroundWindow()):
            print("do nothing")
            return
        
        # open the app
        if self._barnum is not None:
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
            return
        else:
            open_app(app_name=self._name, app_path=self._path) # this is buggy for some reason, maybe i should try ahk to be honest, it is made for doing hotkey
            return

netflix = App(name='Netflix',barnum=8)
anki = App(name="anki",barnum=6)
file_explorer = App(name="file_explorer", barnum=1)
chrome = App(name="- Google Chrome", path="C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe")
vscode = App(name="Visual Studio Code", barnum=10, path="C:\\Users\\manyi\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe")
pycharm = App(name="- Pycharm", barnum=5)
lol = App(name="Garena", barnum=9)
teams = App(name='Microsoft Teams', path='C:\\Program Files (x86)\\Teams_windows_x64.exe')


def kill_window_activate_notice():
    windows = pywinauto.Desktop(backend="uia").windows()
    for w in windows:
        if w.window_text() == "啟用 Windows.移至 [設定] 以啟用 Windows。":
            win32gui.PostMessage(w.handle, win32con.WM_CLOSE,0,0)
            win32gui.CloseWindow(w.handle)
            return