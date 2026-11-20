def order_summary(item, price, quantity, customer):
    total = price * quantity
    print(f"Customer: {customer}\nItem: {item}\nQuantity: {quantity}\nTotal: ₱{total:.2f}")

order_summary("Notebook", 45, 3, "Alex")
