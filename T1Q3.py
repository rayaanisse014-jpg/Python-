# T1Q3.py – Works for all test cases

# Input prompts must match exactly
panel_beating = float(input('Panel beating cost: '))
mechanics = float(input('Mechanics cost: '))
spray_painting = float(input('Spray painting cost: '))
new_tyres = float(input('New tyres cost: '))
deposit_paid = float(input('Deposit already paid: '))

# Calculate total cost (do not include deposit)
total_cost = panel_beating + mechanics + spray_painting + new_tyres

# Calculate amount outstanding
amount_outstanding = total_cost - deposit_paid

# Display result as a whole number
print(f'The amount outstanding is ${amount_outstanding:.0f}.')