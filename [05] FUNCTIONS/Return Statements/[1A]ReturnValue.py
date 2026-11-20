def calculator(a, operator, b):
    if operator == "+": return a + b
    if operator == "-": return a - b
    if operator == "*": return a * b
    if operator == "/" and b != 0: return a / b
    return None

print(calculator(12, "*", 4))
