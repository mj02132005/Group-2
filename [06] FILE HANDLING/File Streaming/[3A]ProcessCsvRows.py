with open("large.txt", "r") as file:
    for line in file:
        if line.strip():
            print(line.strip())
