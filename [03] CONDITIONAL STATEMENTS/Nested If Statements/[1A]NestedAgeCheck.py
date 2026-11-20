score = float(input("Score: "))
if 0 <= score <= 100:
    if score >= 75:
        print("Passed")
    else:
        print("Failed")
else:
    print("Invalid score")
