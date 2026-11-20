for number in range(2, 50):
    if number > 2 and any(number % divisor == 0 for divisor in range(2, number)):
        continue
    print(number)
