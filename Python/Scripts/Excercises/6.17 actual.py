

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
    num = ((s * (s - side1) * (s - side2) * (s - side3)) ** 0.5)
    if isinstance(num, complex):
        return "Input is invalid"
    else:
        return num


input1, input2, input3 = eval(input("Enter three sides for a triangle: "))

if is_valid(input1, input2, input3):
    print(area(input1, input2, input3))
else:
    print("Input is invalid")
