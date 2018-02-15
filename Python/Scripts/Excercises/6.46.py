import turtle

numberOfSides, speed = eval(input("Enter number of sides and speed: "))
turnAmount = 360 / numberOfSides
points = []

turtle.speed(speed)
turtle.penup()
turtle.goto(-25, 12.5 * numberOfSides)

# draw shape with x number of sides
for x in range(numberOfSides):
    turtle.pendown()
    # store points in array for connecting later
    points.append(turtle.position())
    turtle.forward(50)
    turtle.right(turnAmount)

# draw lines connecting points
for x in range(numberOfSides):
    for y in range(len(points)):
        turtle.penup()
        turtle.goto(points[x])
        turtle.pendown()
        turtle.goto(points[y])

turtle.penup()
turtle.goto(0, 0)

turtle.done()

# clap controlled edpy