import math

radius = eval(input("Enter the length from the center of a pentagon to a vertex: "))

side = (2 * radius) * math.sin(math.pi / 5)
area = ((3 * math.sqrt(3)) / 2) * math.pow(side, 2)

print(area)
