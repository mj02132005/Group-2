principal = float(input("Principal: "))
rate = float(input("Annual rate (%): "))
years = float(input("Years: "))
interest = principal * (rate / 100) * years
print("Simple interest:", round(interest, 2))
print("Total amount:", round(principal + interest, 2))
