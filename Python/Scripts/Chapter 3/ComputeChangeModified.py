# Receive the amount 
amount = eval(input("Enter an amount, e.g., 11.56: "))

# Convert the amount to cents
remainingAmount = int(amount * 100)

# Find the number of halves
numberOfHalves = int(remainingAmount / 50)
remainingAmount = int(remainingAmount % 50)

# Find the number of thirds
numberOfThirds = int(remainingAmount / 33)
remainingAmount = int(remainingAmount % 33)

# Assign remaining amount to cents
numberOfCentis = remainingAmount

# Display results
print("Your amount", amount, "consists of\n", 
    "\t", numberOfHalves, "halves\n",
    "\t", numberOfThirds, "thirds\n",
    "\t", numberOfCentis,  "cents")


