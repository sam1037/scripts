from photkey_script_funcs import *
from pynput.keyboard import Key, Listener
import pyautogui as pg
from photkey_script_funcs import chrome


class Website:
    def __init__(self, bookmark, func=None):
        self.bookmark = bookmark
        self.func = func

    def open(self):
        if self.bookmark is None:
            return
        click_bookmark(self.bookmark)
        if self.func is not None:
            self.func()

    def open_in_new(self):
        pg.hotkey('ctrl', 't')
        time.sleep(0.1)
        self.open()


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
    pg.click(103,15, button='right')
    time.sleep(0.1)
    pg.click(206,247)  # close tabs that are on the right of the first tab
    time.sleep(0.5)
    pg.hotkey('ctrl','t')
    time.sleep(0.1)
    pg.hotkey('ctrl', 'shift', 'tab')
    time.sleep(0.1)
    pg.hotkey('ctrl', 'w')
    time.sleep(0.1)
    pg.hotkey('esc')


def yt_func():
    # todo if website already exist, switch to it istead of bring a new one
    time.sleep(1)
    pg.click(880, 130)


def ticktick_func():
    pos = pg.position()
    time.sleep(3)
    pg.click(117, 293)
    pg.moveTo(pos)

def open_chrome_by_selenium():

    def kill_all_chrome_processes():
        import psutil
        import os
        import signal

        psutil.process_iter(attrs=None, ad_value=None)
        processes_list = []
        for proc in psutil.process_iter():
            try:
                # Get process name & pid from process object.
                processName = proc.name()
                processID = proc.pid
                # append them to a list
                a = []
                a.append(processName)
                a.append(processID)
                processes_list.append(a)

            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                pass

        # kill chrome processes
        for proc in processes_list:
            if 'CHROME' in proc[0].upper():
                os.kill(proc[1], signal.SIGTERM)

    def launch_chrome():
        try:
            global driver
            kill_all_chrome_processes()  # driver will only work if there are no chrome processes for god know reason
            from selenium import webdriver
            options = webdriver.ChromeOptions()
            user_data_dir = 'user-data-dir=C:\\Users\\manyi\\AppData\\Local\\Google\\Chrome\\User Data'
            options.add_argument(user_data_dir)
            driver = webdriver.Chrome(executable_path='D:\\文件\\chromedriver_win32\\chromedriver.exe', options=options)
        except Exception as e:
            print(e)
        finally:
            global chrome_opened, chrome_handle
            chrome_opened = True
            chrome_handle = (win32gui.GetForegroundWindow())
            print('launched chrome')

    def main_func():
        try:
            if chrome_opened:
                chrome.open()  # switch to chrome
                print('switched to chrome')
        except Exception as e:
            print(e)
            launch_chrome()  # open chrome if chrome isn't opened

    main_func()


youtube = Website(1, yt_func)
ticktick = Website(4, ticktick_func)
teams = Website(7)
leetcode = Website(8)







