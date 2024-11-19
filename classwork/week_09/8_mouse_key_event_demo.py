"""
    CS121 W18
    DISPLAYS A WINDOW WITH A CANVAS
    AND PRINTS MOUSE AND KEYBOARD EVENTS
    PYTHON 3.6.4
"""

from tkinter import *


class MouseKeyEventDemo:
    def __init__(self):
        window = Tk()
        window.title("Event Demo")

        canvas = Canvas(window, bg="white", width=200, height=100)
        canvas.pack()

        canvas.bind("<Button-1>", self.processMouseEvent)
        canvas.focus_set()

        canvas.bind("<Key>", self.processKeyEvent)
        canvas.focus_set()

        window.mainloop()

    def processMouseEvent(self, event):
        print("Clicked at", event.x, event.y)
        print("Position in the screen", event.x_root, event.y_root)
        print("Which button clicked? ", event.num)

    def processKeyEvent(self, event):
        print("keysym?", event.keysym)
        print("char? ", event.char)
        print("keycode?", event.keycode)


MouseKeyEventDemo()
