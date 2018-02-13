"""
    CS121 W18
    FINDS DISTANCE BETWEEN 4 STATES
    RIVER HILL
    2/13/18
    PYTHON 3.6.4
"""

import math
RADIUS = 6371.01

ATLANTA_X, ATLANTA_Y = 33.7489954, -84.3879824
ORLANDO_X, ORLANDO_Y = 28.5383355, -81.37923649999999
SAVANNAH_X, SAVANNAH_Y = 32.0835407, -81.09983419999998
CHARLOTTE_X, CHARLOTTE_Y = 35.2270869, -80.84312669999997


def side_calc(x1, x2, y1, y2):
    x1, x2, y1, y2 = map(math.radians, [x1, x2, y1, y2])
    return RADIUS * math.acos(math.sin(x1) * math.sin(x2) + math.cos(x1) * math.cos(x2) * math.cos(y1 - y2))


def area_calc(a, b, c):
    s = (a + b + c) / 2
    return (s*(s-a)*(s-b)*(s-c)) ** 0.5


t1side1 = side_calc(ATLANTA_X, CHARLOTTE_X, ATLANTA_Y, CHARLOTTE_Y)
t1side2 = side_calc(CHARLOTTE_X, SAVANNAH_X, CHARLOTTE_Y, SAVANNAH_Y)
t1side3 = side_calc(SAVANNAH_X, ATLANTA_X, SAVANNAH_Y, ATLANTA_Y)

area1 = area_calc(t1side1, t1side2, t1side3)

t2side1 = side_calc(ATLANTA_X, ORLANDO_X, ATLANTA_Y, ORLANDO_Y)
t2side2 = side_calc(ORLANDO_X, SAVANNAH_X, ORLANDO_Y, SAVANNAH_Y)
t2side3 = side_calc(SAVANNAH_X, ATLANTA_X, SAVANNAH_Y, ATLANTA_Y)

area2 = area_calc(t2side1, t2side2, t2side3)

area = area1 + area2

print(area)

# test case should be 117863
