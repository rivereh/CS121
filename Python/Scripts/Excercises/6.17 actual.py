"""
    CS121 W18
    ASKS THE USER FOR THREE SIDES OF
    A TRIANGLE AND RETURNS AREA
    RIVER HILL
    2/19/18
    PYTHON 3.6.4
"""


# function for checking if inputs are valid
def is_valid(side1, side2, side3):
    if side1 + side2 > side3:
        return True
    elif side1 + side3 > side2:
        return True
    elif side2 + side3 > side1:
        return True
    else:
        return False


# function for finding the area of a triangle
# given user inputs
def area(side1, side2, side3):
    s = (side1 + side2 + side3) / 2
    num = ((s * (s - side1) * (s - side2) * (s - side3)) ** 0.5)
    if isinstance(num, complex):
        return "Input is invalid"
    else:
        return num


# asking user for inputs
input1, input2, input3 = eval(input("Enter three sides for a triangle: "))

# checking if valid and returning area if so
if is_valid(input1, input2, input3):
    print(area(input1, input2, input3))
else:
    print("Input is invalid")

# test case for "1, 1, 1" should return "0.4330127018922193"
