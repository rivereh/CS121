"""
    CS121 W18
    ASKS USER FOR THREE NUMBERS THEN
    COMPUTES THE AVERAGE
    1/18/18
    PYTHON 3.6.4
"""

# ask user for three numbers
number_1, number_2, number_3 = eval(
    input("Enter three numbers separated by commas: "))

# compute the average
average = (number_1 + number_2 + number_3) / 3

# print the average
print("The average of,", number_1, number_2, number_3, "is", average)

# test case for 1, 2, 3 should output 2.0
