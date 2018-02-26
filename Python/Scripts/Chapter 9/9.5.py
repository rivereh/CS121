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

        btChangeText = Button(frame2, text="Change Text", command=self.processButton)
        self.v1 = StringVar()
