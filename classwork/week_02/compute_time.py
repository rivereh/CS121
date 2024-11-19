"""
    CS121 W18
    ASKS USER FOR AN AMOUNT OF TIME IN MINUTES
    THE COMPUTES THE AMOUNT OF HOURS AND MINUTES
    1/14/18
    PYTHON 3.6.4
"""

# ask user for an amount of time in minutes
minutes = eval(input("Enter integer for minutes: "))

# compute the amount of hours and minutes
hours = minutes // 60
remaining_minutes = minutes % 60

# print the amount of hours and minutes
print(minutes, "minutes is", hours, "hours and", remaining_minutes, "minutes")
