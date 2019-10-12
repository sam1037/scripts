from photkey_script_funcs import *
from pynput.keyboard import Key, Listener


def choose_bookmark(num):
    if type(num) != int:
        return
    global bookmarks
    # todo update bookmarks automatical constantly
    bookmarks = {0: 'https://www.youtube.com/',
                 1: 'https://www.netflix.com/browse',
                 2: 'https://github.com/',
                 3: 'https://www.ticktick.com/#q/all/tasks',
                 4: 'https://www.evernote.com/client/web?login=true#?an=true&n=23508630-e7c2-4132-98ac-43b8e246c2e0&s'
                    '=s570&',
                 5: 'https://stackoverflow.com/'}  # bookmarknum: url

    pg.hotkey('ctrl', 't')
    pg.typewrite('{0}\n'.format(bookmarks(num)))


def bookmark_process():
    print('processing')
    while True:
        # listen for once if key input is int
        def on_press(key):
            print(key, type(key))
            global num
            # todo convert keycode class to int class
            # num = int(key) will give us error
        def on_release(key):
            # Stop listener
            if type(key) != int:
                print("input isn't int")
                time.sleep(1)
                return False

        with Listener(
                on_press=on_press,
                on_release=on_release) as bookmark_listener:
            bookmark_listener.join()

        if type(num) != int:  # if key input isn't int, end
            return
        else:
            choose_bookmark(num=num)
            print(num,'end')
            return

