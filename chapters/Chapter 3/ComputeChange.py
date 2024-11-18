# Receive the amount 
amount = eval(input("Enter an amount in double, e.g., 11.56: "))

# Convert the amount to cents
remainingAmount = int(amount * 100)

# Find the number of one dollars
numberOfOneDollars = int(remainingAmount / 100)
remainingAmount = int(remainingAmount % 100)


numberOfCents = remainingAmount

# Display results
print("Your amount", amount, "consists of\n", 
        "\t", numberOfOneDollars, "dollars\n",
        "\t", numberOfCents, "cents")


