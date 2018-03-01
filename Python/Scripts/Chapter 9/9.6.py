from tkinter import *

class CanvasDemo:
    def __init__(self):
        window = Tk()
        window.title("Canvas Demo")

        self.canvas = Canvas(window, width=200, height=100, bg="white")
        self.canvas.pack()

        frame = Frame(window)
        frame.pack()

        self.v = IntVar()

        rdRectangle = Radiobutton(frame, text="Rectangle", variable = self.v, value = 1, command=self.displayRect)
        rdOval = Radiobutton(frame, text="Oval", variable = self.v, value = 2, command=self.displayOval)
        self.v2 = IntVar()
        checkFilled = Checkbutton(frame, variable = self.v2, command=self.displayFilled)


        rdRectangle.grid(row=1, column=1)
        rdOval.grid(row=1, column=2)
        checkFilled.grid(row=1, column=3)

        window.mainloop()

    def displayRect(self):
        self.clearCanvas()
        self.canvas.create_rectangle(10, 10, 190, 90, tags="rect")

    def displayOval(self):
        self.clearCanvas()
        self.canvas.create_oval(10, 10, 190, 90, tags="oval")

    def displayFilled(self):
        print(self.v2.get())
        print(self.v.get())
        if self.v2.get() == 1:
            if self.v.get() == 1:
                self.canvas.create_rectangle(10, 10, 190, 90, fill = "grey", tags="rect")
            else:
                self.canvas.create_oval(10, 10, 190, 90, fill = "grey", tags="oval")
        else:
            if self.v.get() == 1:
                self.clearCanvas()
                self.canvas.create_rectangle(10, 10, 190, 90, tags="rect")
            else:
                self.clearCanvas()
                self.canvas.create_oval(10, 10, 190, 90, tags="oval")
    def clearCanvas(self):
        self.canvas.delete("rect", "oval")

CanvasDemo()