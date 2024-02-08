from pynput import mouse, keyboard
from pynput.keyboard import Key, Controller

keyboard =  Controller()
press = lambda key: keyboard.press(key)
release = lambda key: keyboard.release(key)
shortcut = lambda string: keyboard.type(string)

