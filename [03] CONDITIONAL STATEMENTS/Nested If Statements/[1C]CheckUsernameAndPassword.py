pin = input("Enter PIN: ")
if pin == "2468":
    amount = float(input("Withdrawal amount: "))
    if amount > 0 and amount % 100 == 0:
        print("Please collect:", amount)
    else:
        print("Invalid withdrawal amount")
else:
    print("Incorrect PIN")
