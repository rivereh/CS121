from tkinter import *
import random

class DeckOfCardsGUI:
    def __init__(self):
        window = Tk()
        window.title("Random Card Example")

        self.imageList = []
        for i in range(1, 53):
            self.imageList.append(PhotoImage(file = "card/" + str(i) + ".gif"))

        frame = Frame(window)
        frame.pack()

        self.labelList = []
        for i in range(4):
            self.labelList.append(Label(frame, image = self.imageList[i]))
            self.labelList[i].pack(side = LEFT)

        Button(window, text = "Shuffle", command = self.shuffle).pack()

        window.mainloop()

    def shuffle(self):
        random.shuffle(self.imageList)
        for i in range(4):
            self.labelList[i]["image"] = self.imageList[i]

DeckOfCardsGUI()