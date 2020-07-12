import pywinauto 
from pywinauto import Desktop
windows = Desktop(backend="uia").windows()

#for w in windows:
#   print(w.window_text())
print("======================================")
windows = Desktop(backend="win32").windows()
for a in dir(windows[0]):
    print(a)

MainWindows = Desktop(backend="uia").windows()
for w in windows:
    print(w.window_text(),"\n", w.is_active(),"="*20,"\n")
    


#hwndwrapper.DialogWrapper - '一般 (4D) | Microsoft Teams', Chrome_WidgetWin_1
#uiawrapper.UIAWrapper - '一般 (4D) | Microsoft Teams，主視窗', Pane