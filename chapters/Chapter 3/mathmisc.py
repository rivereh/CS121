

import math

amount = eval(input("Enter amount: "))

remainingAmount = int(amount * 100)

numberOfDollars = remainingAmount // 100
remainingAmount = remainingAmount % 100

numberOfQuarters = remainingAmount // 25
remainingAmount = remainingAmount % 25

numberOfDimes = remainingAmount // 10
remainingAmount = remainingAmount % 10

numberOfNickels = remainingAmount // 5
remainingAmount = remainingAmount % 5

numberOfCents = remainingAmount

print(amount, "consists of \n",
      "\t", numberOfDollars, "dollars\n"
      "\t", numberOfQuarters, "quarters\n",
      "\t", numberOfDimes, "dimes\n",
      "\t", numberOfNickels, "nickels\n"
      "\t", numberOfCents, "cents")
