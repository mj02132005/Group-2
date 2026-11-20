name = input("Customer name: ")
subtotal = float(input("Subtotal: "))
discount = subtotal * 0.10
total = subtotal - discount
print(f"Customer: {name}\nSubtotal: ₱{subtotal:,.2f}\nDiscount: ₱{discount:,.2f}\nTotal: ₱{total:,.2f}")
