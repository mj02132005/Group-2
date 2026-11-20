balance = float(input("Balance: "))
withdrawal = float(input("Withdrawal: "))
if withdrawal > 0:
    if withdrawal <= balance:
        print("Remaining:", balance - withdrawal)
    else:
        print("Insufficient funds")
else:
    print("Invalid amount")
