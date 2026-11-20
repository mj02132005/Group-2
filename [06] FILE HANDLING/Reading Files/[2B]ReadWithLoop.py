with open("sample.txt", "r") as file:
    content = file.read().lower()
print("Python occurrences:", content.count("python"))
