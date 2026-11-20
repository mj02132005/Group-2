age = int(input("Age: "))
member = input("Member? (yes/no): ").lower()
if age >= 18:
    if member == "yes":
        print("Adult member discount")
    else:
        print("Regular adult rate")
else:
    if member == "yes":
        print("Youth member discount")
    else:
        print("Regular youth rate")
