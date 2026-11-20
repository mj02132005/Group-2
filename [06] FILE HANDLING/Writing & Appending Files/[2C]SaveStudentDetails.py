items = ["Apple", "Banana", "Orange"]
with open("fruits.txt", "w") as file:
    for item in items:
        file.write(item + "\n")
