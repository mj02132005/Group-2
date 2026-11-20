size = input("Size (S/M/L): ").upper()
match size:
    case "S": price = 100
    case "M": price = 150
    case "L": price = 200
    case _: price = 0
if price:
    print("Price:", price)
else:
    print("Invalid size")
