"""
    CS121 W18
    ASKS THE USER FOR THREE SIDES OF
    A TRIANGLE AND RETURNS AREA
    RIVER HILL, JIN
    2/19/18
    PYTHON 3.6.4
"""


def main():
    # asking user for inputs
    input1, input2, input3 = eval(input("Enter three sides for a triangle: "))

    # checking if valid and returning area if so
    if is_valid(input1, input2, input3):
        print(bool(is_valid(input1, input2, input3)))
        print("The area is", area(input1, input2, input3))
    else:
        print(bool(is_valid(input1, input2, input3)))
        print("Input is invalid")


# function for checking if inputs are valid
def is_valid(side1, side2, side3):
    return (side1 + side2 > side3) and (side1 + side3 > side2) and (side2 + side3 > side1)


# function for finding the area of a triangle
# given user inputs
def area(side1, side2, side3):
    s = (side1 + side2 + side3) / 2
    return (s * (s - side1) * (s - side2) * (s - side3)) ** 0.5


main()
# test case for "1, 1, 1" should return "0.4330127018922193"
