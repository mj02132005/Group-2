line_count = 0
with open("large.txt", "r") as file:
    for line in file:
        line_count += 1
print("Lines:", line_count)
