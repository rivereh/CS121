"""
    CS121 W18
    DISPLAYS A WINDOW WITH A LABEL THAT 
    CAN CHANGE TEXT AND COLOR
    PYTHON 3.6.4
"""

from tkinter import *


class ChangeLabelDemo:
    def __init__(self):
        window = Tk()
        window.title("Change Label Demo")

        frame1 = Frame(window)
        frame1.pack()

        self.lbl = Label(frame1, text="Programming is fun")
        self.lbl.pack()

        frame2 = Frame(window)
        frame2.pack()

        label = Label(frame2, text="Enter text: ")
        self.msg = StringVar()
        entry = Entry(frame2, textvariable=self.msg)

        btChangeText = Button(frame2, text="Change Text",
                              command=self.processButton)

        self.v1 = StringVar()
        rbRed = Radiobutton(frame2, text="Red", bg="Red", variable=self.v1,
                            value="R", command=self.processRadioButton)
        rbYellow = Radiobutton(frame2, text="Yellow", bg="Yellow",
                               variable=self.v1, value="Y", command=self.processRadioButton)

        label.grid(row=1, column=1)
        entry.grid(row=1, column=2)
        btChangeText.grid(row=1, column=3)
        rbRed.grid(row=1, column=4)
        rbYellow.grid(row=1, column=5)

        window.mainloop()

    def processRadioButton(self):
        if self.v1.get() == 'R':
            self.lbl["fg"] = "Red"
        elif self.v1.get() == 'Y':
            self.lbl["fg"] = "Yellow"

    def processButton(self):
        self.lbl["text"] = self.msg.get()


ChangeLabelDemo()
