size = int(input("Diamond half-size: "))
for row in range(1, size + 1):
    print(" " * (size - row) + "*" * (2 * row - 1))
for row in range(size - 1, 0, -1):
    print(" " * (size - row) + "*" * (2 * row - 1))
