with open("large.txt", "r") as source, open("filtered.txt", "w") as target:
    for line in source:
        if "Python" in line:
            target.write(line)
