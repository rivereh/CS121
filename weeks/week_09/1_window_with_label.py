"""
    CS121 W18
    DISPLAYS A WINDOW WITH A LABEL AND A BUTTON
    PYTHON 3.6.4
"""

from tkinter import *

window = Tk()  # creates window
label = Label(window, text="Hello, world!")  # creates label
button = Button(window, text="Submit")  # creates button
label.pack()  # places label in window
button.pack()  # place button in window

window.mainloop()  # creates event loop
