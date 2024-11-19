"""
    CS121 W18
    DISPLAYS A WINDOW WITH TWO BUTTONS
    WHICH PRINT TO THE CONSOLE WHEN CLICKED
    PYTHON 3.6.4
"""

from tkinter import *  # imports everything from tkinter


def processOK():
    print("OK button is clicked")


def processCancel():
    print("Cancel button is clicked")


window = Tk()  # creates window
btOK = Button(window, text="OK", fg="red", command=processOK)
btCancel = Button(window, text="Cancel", bg="yellow", command=processCancel)

btOK.pack()
btCancel.pack()

window.mainloop()  # creates event loop
