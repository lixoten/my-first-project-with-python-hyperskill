# Stage 3/3
print("Earned amount:")
print("Bubblegum: $202")
print("Toffee: $118")
print("Ice cream: $2250")
print("Milk chocolate: $1680")
print("Doughnut: $1075")
print("Pancake: $80")
print()

total = 202 + 118 + 2250 + 1680 + 1075 + 80

print("Income: $", total, sep="")

staffExpenses = int(input("Staff expenses:\n"))
otherExpenses = int(input("Other expenses:\n"))

netIncome = total - staffExpenses - otherExpenses

print("Net Income: $", netIncome, sep="")

