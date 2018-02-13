"""
    CS121 W18
    NUMBER SORTER
    RIVER HILL
    ASKS USER FOR THREE NUMBERS
    AND RETURNS A SORTED ARRAY
    2/13/18
    PYTHON 3.6.4
"""

# gather three numbers from user
input1, input2, input3 = eval(input("Enter three numbers: "))


# function to sort the numbers into an array
def display_sorted_numbers(num1, num2, num3):
    array = [num1, num2, num3]
    return sorted(array)


# printing the results
sortedNumbers = display_sorted_numbers(input1, input2, input3)
print("The sorted numbers are:", end=" ")

for i in range(3):
    print(sortedNumbers[i], end=" ")


# test case for inputs "10, 5, 3" should output "3, 5, 10"
