choice = input("1. Balance  2. Deposit  3. Exit: ")
match choice:
    case "1": print("Your balance is ₱5000")
    case "2":
        amount = float(input("Deposit amount: "))
        if amount > 0: print("New balance:", 5000 + amount)
        else: print("Invalid amount")
    case "3": print("Goodbye")
    case _: print("Invalid selection")
