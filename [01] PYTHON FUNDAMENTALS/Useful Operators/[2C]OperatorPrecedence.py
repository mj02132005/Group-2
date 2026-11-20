score = int(input("Score: "))
attendance = int(input("Attendance percentage: "))
qualified = score >= 75 and attendance >= 80
print("Eligible:", qualified)
