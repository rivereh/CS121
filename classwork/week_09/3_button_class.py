"""
    CS121 W18
    DISPLAYS A WINDOW WITH TWO BUTTONS
    WHICH PRINT TO THE CONSOLE WHEN CLICKED
    USES A CLASS TO DEFINE THE EVENT HANDLERS
    PYTHON 3.6.4
"""

from tkinter import *


class ProcessButtonEvent:
    def __init__(self):
        window = Tk()
        btOK = Button(window, text="OK", fg="red", command=self.processOK)
        btCancel = Button(window, text="Cancel", bg="yellow",
                          command=self.processCancel)

        btOK.pack()
        btCancel.pack()

        window.mainloop()

    def processOK(self):
        print("OK button is clicked")

    def processCancel(self):
        print("Cancel button is clicked")


ProcessButtonEvent()
