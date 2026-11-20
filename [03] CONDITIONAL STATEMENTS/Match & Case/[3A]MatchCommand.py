grade = input("Grade letter: ").upper()
match grade:
    case "A": print("Excellent")
    case "B": print("Very good")
    case "C": print("Satisfactory")
    case "D": print("Needs improvement")
    case "F": print("Failed")
    case _: print("Invalid grade")
