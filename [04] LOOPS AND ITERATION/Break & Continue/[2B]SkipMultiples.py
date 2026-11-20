for row in range(1, 6):
    for column in range(1, 6):
        if row == 3 and column == 3:
            break
        print(f"({row},{column})", end=" ")
    print()
