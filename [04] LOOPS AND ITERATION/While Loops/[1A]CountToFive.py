total = 0
count = 0
while True:
    value = input("Enter a number or q to quit: ")
    if value.lower() == "q":
        break
    total += float(value)
    count += 1
print("Total:", total)
print("Entries:", count)
