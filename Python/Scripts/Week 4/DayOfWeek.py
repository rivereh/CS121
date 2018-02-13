"""
    CS121 W18
    DAY OF WEEK
    RIVER HILL
    ASKS USER FOR TODAY'S DATE AND FUTURE DATE
    AS NUMBER AND RETURNS DAY NAME
    2/1/18
    PYTHON 3.6.4
"""

# Gathering input from user
dayOfWeek = eval(input("Enter today's week day as a number: "))
daysFromNow = eval(input("Enter days from today: "))

# Calculation for finding day of week
calc = (dayOfWeek + daysFromNow) % 7


# Function to find day of week
def find_day(x):
    if x == 0:
        return "Sunday"
    elif x == 1:
        return "Monday"
    elif x == 2:
        return "Tuesday"
    elif x == 3:
        return "Wednesday"
    elif x == 4:
        return "Thursday"
    elif x == 5:
        return "Friday"
    elif x == 6:
        return "Saturday"
    else:
        return "ERROR"


# Print today's day and the future day
print("Today is", find_day(dayOfWeek), "and the future day is", find_day(calc))

# Test case for input of 4 and 3 should be Thursday and Sunday
