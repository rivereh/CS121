"""
    CS121 W18
    DRAWS A TRIANGLE, SQUARE,
    PENTAGON, HEXAGON, AND CIRCLE
    2/13/18
    PYTHON 3.6.4
"""

import turtle

# Draw a triangle
turtle.pensize(3)  # Set pen thickness to 3 pixels
turtle.penup()  # Pull the pen up
turtle.goto(-200, -50)
turtle.pendown()  # Pull the pen down
turtle.begin_fill()  # Begin to fill color in a shape
turtle.color("red")
turtle.circle(40, steps=3)  # Draw a triangle
turtle.end_fill()  # Fill the shape

# Draw a square
turtle.penup()
turtle.goto(-100, -50)
turtle.pendown()
turtle.begin_fill()  # Begin to fill color in a shape
turtle.color("blue")
turtle.circle(40, steps=4)  # Draw a square
turtle.end_fill()  # Fill the shape

# Draw a pentagon
turtle.penup()
turtle.goto(0, -50)
turtle.pendown()
turtle.begin_fill()  # Begin to fill color in a shape
turtle.color("green")
turtle.circle(40, steps=5)  # Draw a pentagon
turtle.end_fill()  # Fill the shape

# Draw a hexagon
turtle.penup()
turtle.goto(100, -50)
turtle.pendown()
turtle.begin_fill()  # Begin to fill color in a shape
turtle.color("yellow")
turtle.circle(40, steps=6)  # Draw a hexagon
turtle.end_fill()  # Fill the shape

# Draw a circle
turtle.penup()
turtle.goto(200, -50)
turtle.pendown()
turtle.begin_fill()  # Begin to fill color in a shape
turtle.color("purple")
turtle.circle(40)  # Draw a circle
turtle.end_fill()  # Fill the shape

# Write text
turtle.color("green")
turtle.penup()
turtle.goto(-100, 50)
turtle.pendown()
turtle.write("Cool Colorful Shapes",
             font=("Times", 18, "bold"))
turtle.hideturtle()

turtle.done()
