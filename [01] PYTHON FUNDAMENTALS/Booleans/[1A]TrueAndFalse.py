age = int(input("Age: "))
registered = input("Registered? (yes/no): ").lower() == "yes"
qualified = age >= 18 and registered
print("Qualified:", qualified)
