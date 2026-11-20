word_count = 0
with open("large.txt", "r") as file:
    for line in file:
        word_count += len(line.split())
print("Words:", word_count)
