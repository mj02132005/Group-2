def student_record(name, course="BSIT", year=1, section="A"):
    return f"{name} | {course} | Year {year} | Section {section}"

print(student_record("Alex", year=2, section="B"))
