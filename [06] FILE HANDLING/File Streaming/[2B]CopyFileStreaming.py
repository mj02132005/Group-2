search_term = input("Search for: ")
with open("large.txt", "r") as source, open("search_results.txt", "w") as target:
    for line_number, line in enumerate(source, start=1):
        if search_term.lower() in line.lower():
            target.write(f"{line_number}: {line}")
