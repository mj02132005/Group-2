rows = int(input("Rows: "))
for row in range(1, rows + 1):
    print(" " * (rows - row) + "*" * (2 * row - 1))
