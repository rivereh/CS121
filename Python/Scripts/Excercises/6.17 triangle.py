import math


def find_distance(x1, y1, x2, y2):
    return math.hypot(x2 - x1, y2 - y1)


def is_valid(side1, side2, side3):
    if side1 + side2 > side3:
        return True
    elif side1 + side3 > side2:
        return True
    elif side2 + side3 > side1:
        return True
    else:
        return False


def area(side1, side2, side3):
    s = (side1 + side2 + side3) / 2
    return (s * (s - side1) * (s - side2) * (s - side3)) * 0.5


inputX1, inputY1, inputX2, inputY2, inputX3, inputY3 = eval(input("Enter three points for a triangle: "))

inputSide1 = find_distance(inputX1, inputY1, inputX2, inputY2)
inputSide2 = find_distance(inputX2, inputY2, inputX3, inputY3)
inputSide3 = find_distance(inputX3, inputY3, inputX1, inputY1)

if is_valid(inputSide1, inputSide2, inputSide3):
    print(area(inputSide1, inputSide2, inputSide3))
