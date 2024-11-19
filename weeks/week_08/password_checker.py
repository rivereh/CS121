"""
    CS121 W18
    PASSWORD CHECKER
    3/6/18
    PYTHON 3.6.4
"""

# asks user for their password
password = input("Please enter a password: ")


# function for checking if password is valid
def is_valid(string):
    # checks if password is longer than 8 characters
    if len(string) <= 7:
        return False
    # checks if there are any special characters
    for char in string:
        if not char.isalnum():
            return False
    digits = 0
    # checks if there is more than two numbers
    for char in string:
        if char.isdigit():
            digits += 1
    if not digits >= 2:
        return False
    return True


# verifies that password is valid
if is_valid(password):
    print("Password is valid")
else:
    print("Password is invalid")
