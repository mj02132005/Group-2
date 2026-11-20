characters = 0
words = 0
lines = 0
with open("large.txt", "r") as file:
    for line in file:
        lines += 1
        characters += len(line)
        words += len(line.split())
print("Lines:", lines)
print("Words:", words)
print("Characters:", characters)
