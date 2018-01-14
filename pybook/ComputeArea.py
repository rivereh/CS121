"""
    CS121 W18
    Compute Area
    River Hill
    Asks user for radius of circle and returns the area
    1/11/18
    Python 3.6.4
"""

# Import math library
import math

# Ask the user and assign a radius
radius = int(input("Enter the radius of the circle: "))

# Compute area
area = math.pow(radius, 2) * math.pi

# Display results
print("The area for the circle of radius", radius, "is", area)

# Test case input of 3 should equal 28.27~
