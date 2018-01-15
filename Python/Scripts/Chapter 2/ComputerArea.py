"""
    CS121 W18
    ASKS USER FOR A RADIUS THEN
    COMPUTES THE AREA OF THE CIRCLE
    RIVER HILL
    1/14/18
    PYTHON 3.6.4
"""

PI = 3.14159

radius = eval(input("Enter the radius: "))
area = (radius ** 2) * PI
print("The area of a circle with a radius of", radius, "is", area)
