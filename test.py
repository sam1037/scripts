"""def main():
    from pynput import mouse

    def listen_hotkey():
        print("listening")

    def on_click(x, y, button, pressed):
        if pressed:
            if button == mouse.Button.middle:
                listen_hotkey()

    with mouse.Listener(on_click=on_click) as l:
        l.join()"""
import pyautogui as pg

bookmarks = {1: 'https://www.youtube.com/',
             2: 'https://www.netflix.com/browse',
             3: 'https://github.com/',
             4: 'https://www.ticktick.com/#q/all/tasks',
             5: 'https://www.evernote.com/client/web?login=true#?an=true&n=23508630-e7c2-4132-98ac-43b8e246c2e0&s'
                '=s570&',
             6: 'https://stackoverflow.com/'}

pg.typewrite('{0}\n'.format(bookmarks[1]))
