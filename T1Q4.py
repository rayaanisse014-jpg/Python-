# Prices for the items
MILK_PRICE = 3.50
MARS_BAR_PRICE = 2.75
ANTACID_PRICE = 4.30

# Ask the user for their money and quantities
money = float(input("How much money do you have (10, 20, 50, 100)? "))
milk_qty = int(input("How many litres of milk? "))
mars_qty = int(input("How many Mars bars? "))
antacid_qty = int(input("How many packs of antacid tablets? "))

# Calculate total cost
total_cost = (
    MILK_PRICE * milk_qty +
    MARS_BAR_PRICE * mars_qty +
    ANTACID_PRICE * antacid_qty
)

# Calculate change
change = money - total_cost

# Display result
print(f"The change should be ${change:.2f}.")
