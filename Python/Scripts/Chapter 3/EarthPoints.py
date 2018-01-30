
import math

x1, x2, y1, y2 = eval(math.radians(input("Enter two sets of latitude and longitude separated by commas\n"
                       "e.g. x1, x2, y1, y2: ")))


RADIUS = 6371.01

d = RADIUS * math.acos(math.sin(x1) * math.sin(x2) + math.cos(x1) * math.cos(y1 - y2))

print(d)