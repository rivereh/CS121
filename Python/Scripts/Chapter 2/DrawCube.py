"""
    CS121 W18
    ASKS USER FOR DIMENSIONS OF CUBE
    THEN DRAWS IT
    RIVER HILL
    1/18/18
    PYTHON 3.6.4
"""
import turtle

# Computes the volume of the circle
x, y, z = eval(input("Enter the cubes width, height, and length separated by commas: "))
volume = (x * y * z)
print("The volume of a cube is", round(volume))


# Function to draw the cube
def draw_cube():
    turtle.goto(x, 0)
    turtle.goto(x, y)
    turtle.penup()
    turtle.goto(x, 0)
    turtle.pendown()
    turtle.goto((z / 2) + x, z / 2)
    turtle.goto((z / 2) + x, (z / 2) + y)
    turtle.goto(x, y)
    turtle.goto(0, y)
    turtle.goto(0, 0)
    turtle.penup()
    turtle.goto(0, y)
    turtle.pendown()
    turtle.goto((z / 2), (z / 2) + y)
    turtle.goto((z / 2) + x, (z / 2) + y)
    turtle.penup()
    turtle.goto((z / 2), (z / 2) + y)
    turtle.pendown()
    turtle.goto((z / 2), (z / 2))
    turtle.goto(0, 0)
    turtle.penup()
    turtle.goto((z / 2), (z / 2))
    turtle.pendown()
    turtle.goto((z / 2) + x, z / 2)
    turtle.penup()
    turtle.goto(0, -15)
    turtle.write(volume)
    turtle.done()


draw_cube()

# Test case for 10, 10, 10 should output 1000
