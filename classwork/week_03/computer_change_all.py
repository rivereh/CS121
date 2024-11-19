"""
    CS121 W18
    COMPUTES THE AMOUNT OF DOLLARS, 
    QUARTERS, DIMES, NICKELS, AND CENTS
    2/13/18
    PYTHON 3.6.4
"""

import math

# receive the amount
amount = eval(input("Enter amount: "))

# convert the amount to cents
remaining_amount = int(amount * 100)

# find the number of dollars
number_of_dollars = remaining_amount // 100
remaining_amount = remaining_amount % 100

# find the number of quarters
number_of_quarters = remaining_amount // 25
remaining_amount = remaining_amount % 25

# find the number of dimes
number_of_dimes = remaining_amount // 10
remaining_amount = remaining_amount % 10

# find the number of nickels
number_of_nickels = remaining_amount // 5
remaining_amount = remaining_amount % 5

# find the number of cents
number_of_cents = remaining_amount

print(amount, "consists of \n",
      "\t", number_of_dollars, "dollars\n"
      "\t", number_of_quarters, "quarters\n",
      "\t", number_of_dimes, "dimes\n",
      "\t", number_of_nickels, "nickels\n"
      "\t", number_of_cents, "cents")
