student = input("Student name: ")
score = input("Score: ")
with open("grades.txt", "a") as file:
    file.write(f"{student},{score}\n")
