"""
    CS121 W18
    Draws various patterns with turtle
    Check bottom of script for draw functions
    RIVER HILL
    1/14/18
    PYTHON 3.6.4
"""
import turtle


def draw_squares():
    turtle.penup()
    turtle.goto(-100, 0)
    turtle.pendown()
    turtle.goto(100, 0)
    turtle.penup()
    turtle.goto(0, 100)
    turtle.pendown()
    turtle.goto(0, -100)
    turtle.penup()
    turtle.goto(100, 100)
    turtle.pendown()
    turtle.goto(100, -100)
    turtle.goto(-100, -100)
    turtle.goto(-100, 100)
    turtle.goto(100, 100)
    turtle.done()


def draw_cross():
    turtle.penup()
    turtle.goto(-100, 0)
    turtle.pendown()
    turtle.goto(100, 0)
    turtle.penup()
    turtle.goto(0, 100)
    turtle.pendown()
    turtle.goto(0, -100)
    turtle.done()


def draw_triangle():
    turtle.goto(50, -75)
    turtle.goto(-50, -75)
    turtle.goto(0, 0)
    turtle.done()


def draw_two_triangles():
    turtle.goto(50, -75)
    turtle.goto(-50, -75)
    turtle.goto(50, 75)
    turtle.goto(-50, 75)
    turtle.goto(0, 0)
    turtle.done()


def draw_rectanguloid():
    turtle.goto(0, 100)
    turtle.goto(200, 100)
    turtle.goto(200, 0)
    turtle.goto(0, 0)
    turtle.goto(-30, -30)
    turtle.goto(170, -30)
    turtle.goto(170, 70)
    turtle.goto(200, 100)
    turtle.penup()
    turtle.goto(170, -30)
    turtle.pendown()
    turtle.goto(200, 0)
    turtle.penup()
    turtle.goto(-30, -30)
    turtle.pendown()
    turtle.goto(-30, 70)
    turtle.goto(0, 100)
    turtle.penup()
    turtle.goto(-30, 70)
    turtle.pendown()
    turtle.goto(170, 70)
    turtle.done()


# Uncomment which one you'd like to see
# draw_squares()
# draw_cross()
# draw_triangle()
# draw_two_triangles()
# draw_rectanguloid()
