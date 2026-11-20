def calculate_total(price, quantity=1, discount=0):
    total = price * quantity
    return total - total * discount

print(calculate_total(100))
print(calculate_total(100, 3, 0.1))
