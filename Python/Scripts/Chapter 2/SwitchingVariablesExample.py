"""
    CS121 W18
    ASKS THE USER FOR TWO NAMES THEN SWITCHES THEM
    RIVER HILL
    1/9/18
    PYTHON 3.6.4
"""

firstName = input("Enter a name: ")
secondName = input("Enter a second name: ")

print(firstName, secondName)
# Switch the variables
firstName, secondName = secondName, firstName
print(firstName, secondName)
