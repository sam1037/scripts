""" I decide to use autohotkey to accomplish this as it's easier to do in that way. 25/9/19
"""


"""
from pynput.keyboard import Key, KeyCode, Listener, Controller
from launch_program_functions import *
import time
# todo google list get messed up randomly: fix whyyyyyyyyyyyyyyy sometime [a,z] instead of [z, a] wtfffffffffffffffffffffffffffffffff
# todo not take bot generated words as input for trigger hotkey

def type_gmail():
    time.sleep(0.01)
    pg.typewrite("gmail for testingza", 0.01)


def function_2():
    print('Executed function_2')


# Create a mapping of keys to function (use frozenset as sets are not hashable - so they can't be used as keys)
combination_to_function = {
    frozenset([KeyCode(char='a'), KeyCode(char='b'), KeyCode(char="c"), KeyCode(char="d")]): [delete_key_twice, type_gmail],
    frozenset([Key.shift, KeyCode(char='b')]): [function_2],
    frozenset([Key.shift, KeyCode(char='B')]): [function_2]
}

# Currently pressed keys
current_keys = []

def on_press(key):
    # When a key is pressed, add it to the set we are keeping track of and check if this set is in the dictionary
    current_keys.append(key)
    print(current_keys)
    #if frozenset(current_keys) in combination_to_function:
        # If the current set of keys are in the mapping, execute the function
     #   combination_to_function[frozenset(current_keys)]()

    # this is working except the hotkey order will messed up sometime somehow someway wtffffffffff
    try:
        for hotkey in combination_to_function:
            le = len(hotkey)
            current_keys_list = [current_keys[i: i+le] for i in range(0, len(current_keys))]
            hotkey_copy = [e for e in hotkey]
            print(hotkey_copy)
            for e in current_keys_list:
                if e == hotkey_copy:
                    current_keys.clear()
                    # activiate hotkey
                    for func in combination_to_function[frozenset(hotkey)]:
                        func()
                        current_keys.clear()
                    return
    except Exception as e:
        print(e)
        pass

    
    try:
        i = 0
        for hotkey in combination_to_function:
            for k in current_keys:
                if k == hotkey[i]:
                    list_to_tested = current_keys[current_keys.index(i): current_keys.index(i)+len(hotkey)+1]
                    if list_to_tested == hotkey:  # if hotkey is pressed
                        for func in combination_to_function[frozenset(hotkey)]:
                            func()
                            current_keys.clear()
                        return
    except Exception as e:
        print(e)
    


def on_release(key):
    # When a key is released, remove it from the set of keys we are keeping track of
    pass

with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()"""