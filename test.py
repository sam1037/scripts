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
a = 'asdfasdf\\bsdf'
print(a)
a = a.encode()
print(a)