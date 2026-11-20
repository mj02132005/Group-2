temperature = float(input("Temperature: "))
raining = input("Raining? (yes/no): ").lower()
if temperature > 25:
    if raining == "yes":
        print("Bring an umbrella")
    else:
        print("Wear light clothes")
else:
    if raining == "yes":
        print("Bring a jacket and umbrella")
    else:
        print("Bring a jacket")
