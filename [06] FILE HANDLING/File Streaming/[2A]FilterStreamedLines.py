with open("large.txt", "r") as source, open("uppercase.txt", "w") as target:
    for line in source:
        target.write(line.upper())
