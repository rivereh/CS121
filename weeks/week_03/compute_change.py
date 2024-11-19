"""
    CS121 W18
    CALCULATES THE NUMBER 
    OF DOLLARS AND CENTS
    2/13/18
    PYTHON 3.6.4
"""

# receive the amount
amount = eval(input("Enter an amount in double, e.g., 11.56: "))

# convert the amount to cents
remaining_amount = int(amount * 100)

# find the number of dollars
number_of_ones = int(remaining_amount / 100)
remaining_amount = int(remaining_amount % 100)

# find the number of cents
number_of_cents = remaining_amount

# display results
print("Your amount", amount, "consists of\n",
      "\t", number_of_ones, "dollars\n",
      "\t", number_of_cents, "cents")
