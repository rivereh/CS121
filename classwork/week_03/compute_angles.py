"""
    CS121 W18
    CALCULATES THE ANGLES OF A TRIANGLE
    2/13/18
    PYTHON 3.6.4
"""

import math

# ask user for the coordinates of three points
x1, y1, x2, y2, x3, y3 = eval(input("Enter six coordinates of three points \
separated by commas like x1, y1, x2, y2, x3, y3: "))

# calculate the angles of the triangle
a = math.sqrt((x2 - x3) * (x2 - x3) + (y2 - y3) * (y2 - y3))
b = math.sqrt((x1 - x3) * (x1 - x3) + (y1 - y3) * (y1 - y3))
c = math.sqrt((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2))

A = math.degrees(math.acos((a * a - b * b - c * c) / (-2 * b * c)))
B = math.degrees(math.acos((b * b - a * a - c * c) / (-2 * a * c)))
C = math.degrees(math.acos((c * c - b * b - a * a) / (-2 * a * b)))

print("The three angles are ", round(A * 100) / 100.0,
      round(B * 100) / 100.0, round(C * 100) / 100.0)

# TEST CASE for (0, 0) (10, 0) (5, 10) Should output 63, 63, 53
