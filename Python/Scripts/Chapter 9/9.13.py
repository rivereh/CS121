from tkinter import *

class Menu:
    def __init__(self):
        window = Tk()
        window.title("Menu")

        # create menu bar
        menubar = Menu(window)
        window.config(menu=menubar)  # set windows Menu to menubar

        # create pulldown
        operationMenu = Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Operation", menu=operationMenu)
        operationMenu.add_command(label="Add", command=self.add)
        operationMenu.add_command(label="Subtract", command=self.subtract)
        operationMenu.add_separator()
        operationMenu.add_command(label="Multiply", command=self.multiply)
        operationMenu.add_command(label="Divide", command=self.divide)

        exitmenu = Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Exit", menu=exitmenu)
        exitmenu.add_cascade(label="Quit", command=window.quit)

        frame0 = Frame(window)
        frame0.grid(row=1, column=1, sticky=W)

        Button(frame0, label="+", command=self.add).grid(row=1, column=1, sticky=W)


    # NOT FINISHED

