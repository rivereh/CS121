"""
    CS121 W18
    ASKS USER FOR 5 NUMBERS THEN
    COMPUTES THE AVERAGE
    2/1/18
    PYTHON 3.6.4
"""

NUMBER_OF_ELEMENTS = 5
numbers = []
sum = 0

for i in range(NUMBER_OF_ELEMENTS):
    value = eval(input("Enter a number: "))
    sum += value

average = sum / NUMBER_OF_ELEMENTS

count = 0
for i in range(NUMBER_OF_ELEMENTS):
    if numbers[i] > average:
        count += 1

print("Average is", average)
print("Amount of numbers above the average is", count)
