expenses = [10, 12,4.5,7,19]
total = 0

# option 1
for expense in expenses:
    total += expense
print("You spent $", total, sep = '')

# option 2
total = sum(expenses)
print("You spent $", total, sep = '')