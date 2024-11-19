"""
    CS121 W18
    ASKS THE USER FOR TWO POINTS AND FINDS
    DISTANCE BETWEEN ON SPHERE
    2/13/18
    PYTHON 3.6.4
"""

import math
RADIUS = 6371.01


# ask user for two points
x1, y1 = eval(
    (input("Enter a set of latitude and longitude separated by commas e.g. x1, y1: ")))
x2, y2 = eval(
    (input("Enter a set of latitude and longitude separated by commas e.g. y2, y2: ")))

# convert points to radians
x1, x2, y1, y2 = map(math.radians, [x1, x2, y1, y2])

# find distance using formula for finding distance between points on sphere
distance = RADIUS * math.acos(math.sin(x1) * math.sin(x2) +
                              math.cos(x1) * math.cos(x2) * math.cos(y1 - y2))

# print results
print("The distance between the two points is", distance, "km")

# 39.55, -116.25
# 41.5, 87.37
