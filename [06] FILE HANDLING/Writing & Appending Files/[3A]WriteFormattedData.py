entries = []
for _ in range(3):
    entries.append(input("Enter note: "))
with open("journal.txt", "w") as file:
    file.write("\n".join(entries))
