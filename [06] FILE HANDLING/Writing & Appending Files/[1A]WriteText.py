product = input("Product: ")
price = float(input("Price: "))
quantity = int(input("Quantity: "))
with open("sales.txt", "a") as file:
    file.write(f"{product},{price:.2f},{quantity},{price * quantity:.2f}\n")
