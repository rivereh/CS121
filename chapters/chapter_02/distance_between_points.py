"""
    CS121 W18
    CALCULATES THE DISTANCE BETWEEN TWO POINTS
    RIVER
    1/18/18
    PYTHON 3.6.4
"""

import turtle

# ask user for the coordinates of two points
x1, y1 = eval(input("Enter x1 and y1 for point 1: "))
x2, y2 = eval(input("Enter x2 and y2 for point 2: "))

# calculate the distance between the two points
distance = ((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2)) ** 0.5

# print the distance between the two points
print("The distance between the two points is", distance)

# draw the two points and the distance between them
turtle.penup()
turtle.goto(x1, y1)
turtle.pendown()
turtle.write("Point 1")
turtle.goto(x2, y2)
turtle.write("Point 2")
turtle.penup()
turtle.goto((x1 + x2) / 2, (y1 + y2) / 2)
turtle.write(distance)
turtle.done()
