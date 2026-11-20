total = 0
for number in range(1, 101):
    if number % 7 == 0:
        continue
    total += number
print(total)
