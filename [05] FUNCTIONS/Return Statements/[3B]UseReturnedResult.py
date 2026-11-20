def calculate_discount(price, rate):
    return price * (rate / 100)

price = float(input("Price: "))
rate = float(input("Discount percent: "))
print("Discount:", calculate_discount(price, rate))
