"""
    CS121 W18
    ASKS USER FOR A RADIUS THEN
    COMPUTES AND DRAWS THE AREA OF THE CIRCLE
    RIVER HILL
    1/18/18
    PYTHON 3.6.4
"""
import turtle
PI = 3.14159

# Computes the area of the circle
radius = eval(input("Enter the radius: "))
area = (radius ** 2) * PI
print("The area of a circle with a radius of", radius, "is", round(area))

# Draws circle with given radius under 300 and prints the radius
if radius <= 300:
    turtle.penup()
    turtle.goto(0, -radius)
    turtle.pendown()
    turtle.circle(radius)
    turtle.penup()
    turtle.goto(0, 0)
    turtle.write(round(area))
    turtle.done()
else:
    print(radius, "too big to draw on screen")

# Test case for 30 should output 2827
''