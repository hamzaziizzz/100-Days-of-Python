print("Welcome to the tip calculator!")

total_bill = float(input("What was the total bill? $"))
tip = float(input("How much tip would you like to give? 10, 12, or 15? "))
no_of_splits = float(input("How many peolpleto split the bill? "))

tip_ratio = 1 + (tip / 100)
payable_bill = (total_bill * tip_ratio) / no_of_splits

print(f"Each person should pay: ${payable_bill:.2f}")