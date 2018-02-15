import turtle

turnAmount = 360 / 6

points = []

for x in range(6):
    points.append(turtle.position())
    turtle.forward(100)
    turtle.right(turnAmount)

for x in range(4):
    for y in range(len(points)):
        turtle.penup()
        turtle.goto(points[x])
        turtle.pendown()
        turtle.goto(points[y])

turtle.done()

# clap controlled edpy