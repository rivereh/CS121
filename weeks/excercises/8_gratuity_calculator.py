"""
    CS121 W18
    ASKS THE USER FOR TOTAL AND GRATUITY RATE AND
    RETURNS TOTAL AMOUNT DUE
    2/13/18
    PYTHON 3.6.4
"""

# capture input
total, gratuity = eval(input("Enter the subtotal and a gratuity rate: "))

# find total due
gratuity = total * (gratuity / 100)
total = total + gratuity

# print results
print("The gratuity is", round(gratuity, 2),
      "and the total is", round(total, 2))
