for number in range(1, 6):
    with open("numbers.txt", "a") as file:
        file.write(f"{number}\n")
