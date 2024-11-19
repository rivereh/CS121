"""
    CS121 W18
    DISPLAYS A WINDOW WITH A LABEL, ENTRY, BUTTON, AND MESSAGE
    PYTHON 3.6.4
"""

from tkinter import *


class WidgetsDemo:
    def __init__(self):
        window = Tk()
        window.title("Widgets Demo")

        frame1 = Frame(window)
        frame1.pack()

        self.v1 = IntVar()
        cbtBold = Checkbutton(
            frame1, text="Bold", variable=self.v1, command=self.processCheckButton)

        self.v2 = IntVar()
        rbRed = Radiobutton(frame1, text="Red", bg="Red",
                            variable=self.v2, value=1, command=self.processRadioButton)
        rbYellow = Radiobutton(frame1, text="Yellow", bg="Yellow",
                               variable=self.v2, value=2, command=self.processRadioButton)

        cbtBold.grid(row=1, column=1)
        rbRed.grid(row=1, column=2)
        rbYellow.grid(row=1, column=3)

        frame2 = Frame(window)
        frame2.pack()
        label = Label(frame2, text="Enter your name: ")
        self.name = StringVar()
        entryName = Entry(frame2, textvariable=self.name)

        btGetName = Button(frame2, text="Get Name", command=self.processButton)
        message = Message(frame2, text="It is a widgets demo")
        label.grid(row=1, column=1)
        entryName.grid(row=1, column=2)
        btGetName.grid(row=1, column=3)
        message.grid(row=1, column=4)

        text = Text(window)
        text.pack()
        text.insert(END, "Tip\nThe best way to learn Tkinter is to read ")
        text.insert(END, "these carefully designed examples and use them ")
        text.insert(END, "to create your applications.")

        window.mainloop()

    def processCheckButton(self):
        print("check button is " +
              ("checked" if self.v1.get() == 1 else "unchecked"))

    def processRadioButton(self):
        print(("Red " if self.v2.get() == 1 else "Yellow ") + "is selected")

    def processButton(self):
        print("Your name is", self.name.get())


WidgetsDemo()
