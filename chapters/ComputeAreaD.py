"""
    CS121 W18
    Compute Area With Diameter
    River Hill
    Asks user for diameter of circle and returns the area
    1/11/18
    Python 3.6.4
"""

# Import math library
import math

# Ask the user and assign a radius
diameter = (int(input("Enter the radius of the circle: ")) / 2)

# Compute area
area = math.pow(diameter, 2) * math.pi

# Display results
print("The area for the circle of radius", diameter, "is", area)

# Test case input of 6 should equal 28.27~
