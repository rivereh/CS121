"""
    CS121 W18
    DISPLAYS A WINDOW WITH A CANVAS AND BUTTONS
    TO DRAW RECTANGLE AND OVAL SHAPES
    PYTHON 3.6.4
"""

from tkinter import *


class RectangleOval:
    def __init__(self):
        window = Tk()
        window.title("Canvas Demo")

        # create blank canvas to draw shapes on
        self.canvas = Canvas(window, width=200, height=100, bg="white")
        self.canvas.pack()

        # initializing frame for buttons
        frame = Frame(window)
        frame.pack()

        # set first variable and set it to the values of the rectangle
        # and oval radio buttons
        self.v = IntVar()

        # create buttons and set first variable to check button
        rdRectangle = Radiobutton(
            frame, text="Rectangle", variable=self.v, value=1, command=self.displayRect)
        rdOval = Radiobutton(frame, text="Oval", variable=self.v,
                             value=2, command=self.displayOval)
        self.v2 = IntVar()
        checkFilled = Checkbutton(
            frame, variable=self.v2, command=self.displayFilled)

        # align buttons in a single row
        rdRectangle.grid(row=1, column=1)
        rdOval.grid(row=1, column=2)
        checkFilled.grid(row=1, column=3)

        window.mainloop()

    # function for displaying rectangle
    def displayRect(self):
        self.clearCanvas()
        self.canvas.create_rectangle(10, 10, 190, 90, tags="rect")

    # function for displaying oval
    def displayOval(self):
        self.clearCanvas()
        self.canvas.create_oval(10, 10, 190, 90, tags="oval")

    def displayFilled(self):
        # if check button is pressed and set to 1 and rectangle is selected then
        # fill in the rectangle shape otherwise fill in the oval shape
        if self.v2.get() == 1:
            if self.v.get() == 1:
                self.canvas.create_rectangle(
                    10, 10, 190, 90, fill="grey", tags="rect")
            else:
                self.canvas.create_oval(
                    10, 10, 190, 90, fill="grey", tags="oval")
        # if check button is pressed and set to 0 then clear both oval and rectangle shapes
        else:
            if self.v.get() == 1:
                self.clearCanvas()
                self.canvas.create_rectangle(10, 10, 190, 90, tags="rect")
            else:
                self.clearCanvas()
                self.canvas.create_oval(10, 10, 190, 90, tags="oval")

    # function for clearing the canvas
    def clearCanvas(self):
        self.canvas.delete("rect", "oval")


RectangleOval()
