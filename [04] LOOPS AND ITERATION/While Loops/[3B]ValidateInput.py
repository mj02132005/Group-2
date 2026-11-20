number = int(input("Enter an integer: "))
original = number
reverse = 0
while number > 0:
    digit = number % 10
    reverse = reverse * 10 + digit
    number //= 10
print("Original:", original)
print("Reversed:", reverse)
