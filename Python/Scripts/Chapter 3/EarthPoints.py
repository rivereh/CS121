"""
    CS121 W18
<<<<<<< HEAD
    ASKS THE USER FOR TWO POINTS AND FINDS
    DISTANCE BETWEEN ON SPHERE
    RIVER HILL
    2/13/18
    PYTHON 3.6.4
"""


=======
    WELCOME PROJECT
    RIVER HILL
    ASKS USER FOR TWO POINTS ON SPHERE AND
    CALCULATES DISTANCE BETWEEN
    1/25/18
    PYTHON 3.6.4
"""
>>>>>>> 08af1eac24a4af7529da9f6262825c1cc66d4b54
import math
RADIUS = 6371.01

<<<<<<< HEAD
# ask user for two points
x1, y1 = eval((input("Enter a set of latitude and longitude separated by commas e.g. x1, y1: ")))
x2, y2 = eval((input("Enter a set of latitude and longitude separated by commas e.g. y2, y2: ")))

# convert points to radians
x1, x2, y1, y2 = map(math.radians, [x1, x2, y1, y2])

# find distance using formula for finding distance between points on sphere
distance = RADIUS * math.acos(math.sin(x1) * math.sin(x2) + math.cos(x1) * math.cos(x2) * math.cos(y1 - y2))

# print results
print("The distance between the two points is", distance, "km")

# 39.55, -116.25
# 41.5, 87.37

=======
RADIUS = 6371.01

x1, x2, y1, y2 = eval(input("Enter two sets of latitude and longitude separated by commas\n"
                            " e.g. x1, x2, y1, y2: "))
distance = RADIUS * math.acos(math.radians(math.sin(x1) * math.sin(x2)
                              + math.cos(x1) * math.cos(x2) * math.cos(y1 - y2)))

print("The distance between the two is", str(distance) + "km")

# test case for 39.55, -116.25, 41.5, 87.37 should be 10015.955km
>>>>>>> 08af1eac24a4af7529da9f6262825c1cc66d4b54
