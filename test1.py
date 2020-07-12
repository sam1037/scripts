import time

from photkey_script_funcs import maximaze_current_window

def open_app(app_name, app_path):
    import win32gui
    import pywinauto
    import win32con
    import subprocess
    import os

    def open():
        file = app_path.split("\\")[-1]
        dir = app_path.split("\\")[0:-1]
        dir = "\\".join(dir)
        os.system(f"cd {dir}")     
        os.system(f"start {file}")     
        print(f"Opened {app_name}")

    def switch(hwnd):
        win32gui.SetForegroundWindow(hwnd)
        win32gui.ShowWindow(w.handle, win32con.SW_MAXIMIZE)
        print(f"Switched to {app_name}")
        return

    windows = pywinauto.Desktop(backend="uia").windows()

    # check if the app is on the foreground
    if app_name in win32gui.GetWindowText(win32gui.GetForegroundWindow()):
        print("do nothing")
        return
    #check if the app is opened
    for w in windows:
        if app_name in w.window_text():
            #bring it to foreground
            switch(w.handle)
            return
    open()

#open_app("Microsoft Teams", "C:\\Teams_windows_x64.exe")
#open_app("- Google Chrome", "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe")

def open(app_path):
    import os
    file = str(app_path.split("\\")[-1])
    dir = app_path.split("\\")[0:-1]
    dir = ("\\"+"\\").join(dir)
    print(file,dir)
    os.system(f"cd {dir}")     
    os.system(f"start {file}")     
    #print(f"Opened {app_name}")

#open("C:\\Users\\manyi\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe")

import os
os.system("cd C:\Users\manyi\AppData\Local\Programs\Microsoft VS Code")
os.system("start Code.exe")

print("finished")