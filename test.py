import time
import pyautogui as pg
import pynput                      
from pynput.keyboard import Key, Listener
from pynput.mouse import Listener as mL
import keyboard as kd
import subprocess
import win32gui
from PIL import ImageGrab
import math

def get_mouse_coords():

    def on_click(x, y, button, clicking):
        print(x,y)

    def on_release():
        pass

    with mL(on_click=on_click, on_move=on_release()) as l:
        l.join()

                     
def timing_val(func):
    def wrapper(*arg, **kw):
        '''source: http://www.daniweb.com/code/snippet368.html'''
        t1 = time.time()
        res = func(*arg, **kw)
        t2 = time.time()
        print((t2 - t1), res, func.__name__)
    return wrapper


def teszt(num=0):
    pos = pg.position()
    pg.click((410+num*48), 1050)
    pg.moveTo(pos[0],pos[1])
  

def get_color():

    def on_press(key):
        if key == pynput.keyboard.Key.space: 
            coord = pg.position()
            screen = ImageGrab.grab()
            color = screen.getpixel(coord)
            print(color)

    def on_release(key):
        pass

    with Listener(on_press=on_press, on_release=on_release) as kl:
        kl.join()


def get_pos_space():

    def on_press(key):
        if key == pynput.keyboard.Key.space: 
            coord = pg.position()
            print(coord)

    def on_release(key):
        pass

    with Listener(on_press=on_press, on_release=on_release) as kl:
        kl.join()


def test():
    time.sleep(2)
    t0 = time.time()
    to_check = [(a,0) for a in range(0,1704)]


    screen = ImageGrab.grab()
    colors = map(screen.getpixel, to_check)
    c = [color for color in colors if color == (255,255,255)]
    print(len(c))
    print(time.time()-t0)


def binary_split_list(length):
    def get_middle(li):
        length = len(li)
        index = math.ceil(((length + 1)/2) -1)
        return li[index]
        
    result = []
    indices = [[a for a in range(0,length)]]
    while len(result) != length:
        n = []
        for listt in indices.copy():
            if len(listt) == 1:
                indices.remove(listt)
                n.append(listt[0])
                indices.remove(listt)
            elif len(listt) == 2:
                indices.remove(listt)
                n.append(listt[0])
                indices.append([listt[1]])
            elif len(listt) >=3:
                num = get_middle(listt)
                n.append(num)
                indices.remove(listt)
                indices.append(listt[0:num])
                indices.append(listt[num+1:])

        for a in n:
            result.append(a)

    return result


def split_list(head, tail):
    def get_middle(head, tail):
        index = math.ceil((head + tail)/2)
        return index

    to_check = [(head, tail)]
    result = []
    while len(to_check) != 0:
        for a in to_check.copy():
            to_check.remove(a)
            n = get_middle(a[0],a[1])
            head1 = head if n != head else None
            tail1 = n-1 if n-1 >head1 else None
            head2 = n+1 if n+1 <tail else None
            tail2 = tail if n != tail else None

            if head1 and tail1:
                to_check.append((head1, tail1))
            if head2 and tail2:
                to_check.append((head2, tail2))
            result.append(n)
    
    return result

get_pos_space()  