from tkinter import *


class Popup:
    def __init__(self):
        window = Tk()
        window.title("Popup")

        self.menu = Menu(window, tearoff = 0)
        self.menu.add_command(label = "Show Profit Cat", command = self.showCat)
        self.menu.add_command(label = "Clear", command = self.clearCanvas)
        self.menu.add_command(label="Quit", command=window.quit)

        self.canvas = Canvas(window, width = 200, height = 100, bg = "white")
        self.canvas.pack()

        self.canvas.bind("<Button-3>", self.popup)

        window.mainloop()

    def showCat(self):
        catImage = PhotoImage('http://thetango.net/wp-content/uploads/2013/11/Depressed.jpg')
        self.canvas.create_image(90, 50, image = catImage)

    def clearCanvas(self):
        print("te")

    def popup(self, event):
        self.menu.post(event.x_root, event.y_root)


Popup()