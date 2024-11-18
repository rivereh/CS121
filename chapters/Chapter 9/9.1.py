from tkinter import *  # imports everything from tkinter

window = Tk()  # creates window
label = Label(window, text="Hello, world!")  # creates label
button = Button(window, text="Submit")  # creates button
label.pack()  # places label in window
button.pack()  # place button in window

window.mainloop()  # creates event loop
