"""
    CS121 W18
    PRINTS A PYRAMID OF NUMBERS
    RIVER HILL
    3/6/18
    PYTHON 3.6.4
"""
from tkinter import *


class NumberPyramid:
    def __init__(self):
        window = Tk()

        # initialize number array
        text_to_label = ["1"]
        for i in range(10):
            # for each iteration, add a new element to the array
            # to print that's one higher than the previous iteration
            Label(window, text = text_to_label).pack(fill = BOTH)
            text_to_label.append(str(int(text_to_label[i]) + 1))

        window.mainloop()


NumberPyramid()