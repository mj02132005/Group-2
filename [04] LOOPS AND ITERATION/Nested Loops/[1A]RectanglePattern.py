students = int(input("Number of students: "))
subjects = int(input("Subjects per student: "))
for student in range(1, students + 1):
    total = 0
    for subject in range(1, subjects + 1):
        grade = float(input(f"Student {student}, subject {subject}: "))
        total += grade
    print(f"Student {student} average: {total / subjects:.2f}")
