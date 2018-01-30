"""
    CS121 W18
    WELCOME PROJECT
    RIVER HILL
    ASKS USER FOR TWO POINTS ON SPHERE AND
    CALCULATES DISTANCE BETWEEN
    1/25/18
    PYTHON 3.6.4
"""
import math

RADIUS = 6371.01

x1, x2, y1, y2 = eval(input("Enter two sets of latitude and longitude separated by commas\n"
                            " e.g. x1, x2, y1, y2: "))
distance = RADIUS * math.acos(math.radians(math.sin(x1) * math.sin(x2)
                              + math.cos(x1) * math.cos(x2) * math.cos(y1 - y2)))

print("The distance between the two is", str(distance) + "km")

# test case for 39.55, -116.25, 41.5, 87.37 should be 10015.955km
