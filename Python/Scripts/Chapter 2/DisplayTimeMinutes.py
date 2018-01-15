"""
    CS121 W18
    ASKS USER FOR AN AMOUNT OF TIME IN MINUTES
    THE COMPUTES THE AMOUNT OF HOURS AND MINUTES
    RIVER HILL
    1/14/18
    PYTHON 3.6.4
"""

minutes = eval(input("Enter integer for minutes: "))
hours = minutes // 60
# Find remaining minutes by dividing the hours by 60 and storing the remainder
remainingMinutes = hours % 60
print(minutes, "minutes is", hours, "hours and", remainingMinutes, "minutes")
