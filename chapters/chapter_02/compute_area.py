"""
    CS121 W18
    ASKS USER FOR A RADIUS THEN
    COMPUTES THE AREA OF THE CIRCLE
    RIVER
    1/14/18
    PYTHON 3.6.4
"""

PI = 3.14159

# ask user for the radius
radius = eval(input("Enter the radius: "))

# compute the area of the circle
area = (radius ** 2) * PI

# print the area of the circle
print("The area of a circle with a radius of", radius, "is", area)
