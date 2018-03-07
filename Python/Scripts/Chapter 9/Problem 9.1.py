from tkinter import *

class ControlBall:
    def __init__(self):
        window = Tk()
        window.title("Control Ball Demo")

        self.width = 250
        self.canvas = Canvas(window, bg = "white", width = self.width, height = 50)
        self.canvas.pack()

        frame = Frame(window)
        frame.pack()

        btStop = Button(frame, text = "Stop", command = self.stop)
        btStop.pack(side = LEFT)
        btResume = Button(frame, text = "Resume")