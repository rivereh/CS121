from tkinter import *


class PackManagerSideDemo:
    window = Tk()
    window.title("Pack Manager Side Demo")

    Label(window, text="Blue", bg="blue").pack(side = LEFT)
    Label(window, text="Red", bg="red").pack(side = LEFT, fill = BOTH, expand = 1)
    Label(window, text="Green", bg="green").pack(side = LEFT, fill = BOTH)

    window.mainloop()


PackManagerSideDemo()

# The side option can be LEFT, RIGHT, TOP, or BOTTOM.
# By default, it is set to TOP.
