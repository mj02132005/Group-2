amount = float(input("Purchase amount: "))
if amount >= 5000:
    discount = 0.15
elif amount >= 2500:
    discount = 0.10
elif amount >= 1000:
    discount = 0.05
else:
    discount = 0
print("Discount:", amount * discount)
print("Total:", amount * (1 - discount))
