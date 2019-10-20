from photkey_script_funcs import *
from pynput.keyboard import Key, Listener


def choose_bookmark(num):
    if type(num) != int:
        print('ERROR: input should be int')
        return
    global bookmarks
    # todo update bookmarks automatical constantly
    bookmarks = {1: 'hello',
                 2: 'https://www.netflix.com/browse',
                 3: 'https://github.com/',
                 4: 'https://www.ticktick.com/#q/all/tasks',
                 5: 'https://www.evernote.com/client/web?login=true#?an=true&n=23508630-e7c2-4132-98ac-43b8e246c2e0&s'
                    '=s570&',
                 6: 'https://stackoverflow.com/'}  # bookmarknum to url

    pg.hotkey('ctrl', 't')
    time.sleep(0.1)
    pg.typewrite(bookmarks[num])  # todo fix why alaways type slowly except for a few times after using after a while
    pg.hotkey('enter')

def bookmark_process():  # take a number and open certain bookmark
    time.sleep(0.1)
    print('---------------------------')
    print('processing')
    print("listening for keystroke")

    # listen for once if key input is int
    def on_press(key):
        pass

    def on_release(key):
        try:
            key = int(key.char)
            print('on release')

        except ValueError as err:
            print("Expected int input, but didn't get one")

        else:
            choose_bookmark(num=key)

        finally:
            print('End with {0} key pressed\n-----------------------------------'.format(key))
            return False  # end listening, end process

    with Listener(
            on_press=on_press,
            on_release=on_release) as bookmark_listener:
        bookmark_listener.join()

