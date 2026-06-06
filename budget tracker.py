# Budget Tracker

print("=== My Budget Tracker ===")

# Taking inputs
income = float(input("Enter your monthly income: "))

rent = float(input("Enter rent amount: "))
food = float(input("Enter food expenses: "))
transport = float(input("Enter transport expenses: "))
other = float(input("Enter other expenses: "))

# Calculations
total_expenses = rent + food + transport + other
balance = income - total_expenses
savings_percent = (balance / income) * 100

# Output
print("\n--- Your Monthly Summary ---")
print("Total Income:   ₹", income)
print("Total Expenses: ₹", total_expenses)
print("Balance Left:   ₹", balance)
print("Savings %:      ", savings_percent, "%")

if balance > 0:
    print("Great! You are saving money.")
elif balance == 0:
    print("Warning: You are breaking even.")
else:
    print("Alert! You are overspending!")


