
from tkinter import *

class CheckerBoard:
    def __init__(self):
        window = Tk()
        window.title("Checkerboard")

        self.canvas = Canvas(window, width = 500, height = 500, bg = 'white')
        self.canvas.pack()

        for i in range(10):
            if i % 2 == 0:
                self.canvas.create_rectangle(100 * i, 100, 100 * i, 100)

        window.mainloop()


CheckerBoard()