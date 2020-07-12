def open_chrome_by_selenium():  
    import win32gui

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
            driver = webdriver.Chrome(executable_path='C:\\chromedriver\\chromedriver.exe', options=options)
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



def kill_window_activate_notice():
    import pywinauto, win32gui, win32con
    windows = pywinauto.Desktop(backend="uia").windows()
    for w in windows:
        if w.window_text() == "啟用 Windows.移至 [設定] 以啟用 Windows。":
            win32gui.PostMessage(w.handle, win32con.WM_CLOSE,0,0)
            win32gui.CloseWindow(w.handle)
            return


kill_window_activate_notice()


