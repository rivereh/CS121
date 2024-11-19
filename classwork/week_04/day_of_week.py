"""
    CS121 W18
    ASKS USER FOR TODAY'S DATE AND FUTURE DATE
    AS NUMBER AND RETURNS DAY NAME
    2/1/18
    PYTHON 3.6.4
"""

# gathering input from user
day_of_week = eval(input("Enter today's week day as a number: "))
days_from_now = eval(input("Enter days from today: "))

# calculation for finding day of week
calc = (day_of_week + days_from_now) % 7


# function to find day of week
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


# print today's day and the future day
print("Today is", find_day(day_of_week),
      "and the future day is", find_day(calc))

# test case for input of 4 and 3 should be Thursday and Sunday
