import turtle, random

colors = ["blue", "red", "purple", "cyan", "pink"]

numberOfSides, speed = eval(input("Enter number of sides and speed: "))
turnAmount = 360 / numberOfSides
points = []

turtle.speed(speed)
turtle.penup()
turtle.goto(-25, 12.5 * numberOfSides)

# draw shape with x number of sides
for x in range(numberOfSides):
    turtle.color(random.choice(colors))
    turtle.pendown()
    # store points in array for connecting later
    points.append(turtle.position())
    turtle.forward(50)
    turtle.right(turnAmount)

# draw lines connecting points
for x in range(numberOfSides):
    for y in range(len(points)):
        turtle.color(random.choice(colors))
        turtle.penup()
        turtle.goto(points[x])
        turtle.pendown()
        turtle.goto(points[y])

turtle.done()

# clap controlled edpy