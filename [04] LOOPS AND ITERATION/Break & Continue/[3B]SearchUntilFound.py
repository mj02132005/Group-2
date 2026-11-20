attempts = 0
while attempts < 3:
    pin = input("PIN: ")
    if pin == "1357":
        print("Unlocked")
        break
    attempts += 1
else:
    print("Too many attempts")
