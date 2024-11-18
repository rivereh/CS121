"""
    CS121 W18
    PRINTS A SPIRAL
    RIVER
    1/14/18
    PYTHON 3.6.4
"""

import turtle

rotationAmount = 10
turtle.color("red")

for x in range(0, 3):
    turtle.circle(rotationAmount)
    turtle.circle(-rotationAmount)
    rotationAmount += 10
turtle.done()
