name = input("Name: ")
with open("names.txt", "a") as file:
    file.write(name + "\n")
