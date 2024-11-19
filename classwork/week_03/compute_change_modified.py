# Receive the amount
amount = eval(input("Enter an amount, e.g., 11.56: "))

# Convert the amount to cents
remaining_amount = int(amount * 100)

# Find the number of halves
number_of_halves = int(remaining_amount / 50)
remaining_amount = int(remaining_amount % 50)

# Find the number of thirds
number_of_thirds = int(remaining_amount / 33)
remaining_amount = int(remaining_amount % 33)

# Assign remaining amount to cents
number_of_cents = remaining_amount

# Display results
print("Your amount", amount, "consists of\n",
      "\t", number_of_halves, "halves\n",
      "\t", number_of_thirds, "thirds\n",
      "\t", number_of_cents,  "cents")
