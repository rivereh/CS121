"""
    CS121 W18
    ASKS USER FOR A X, Y LOCATION AND
    CHECKS IF IT IS WITHIN A CIRCLE WITH
    A RADIUS OF 10
    2/1/18
    PYTHON 3.6.4
"""

# ask user for X and Y and determines distance from circle
x, y = eval(input("Enter an X and Y separated by commas: "))
d = (pow(x, 2) + pow(y, 2)) ** 0.5


# function for determining if the distance is within the circle or not
def determine_point(point):
    if point <= 10:
        return "is in"
    else:
        return "is not"


# print the point along with whether it is in the circle or not
print("The point (" + str(x) + "," + str(y) + ") is", determine_point(d))
