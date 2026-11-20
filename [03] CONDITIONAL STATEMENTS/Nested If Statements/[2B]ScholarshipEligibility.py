attendance = float(input("Attendance percentage: "))
score = float(input("Final score: "))
if attendance >= 80:
    if score >= 75:
        print("Passed")
    else:
        print("Failed due to score")
else:
    print("Failed due to attendance")
