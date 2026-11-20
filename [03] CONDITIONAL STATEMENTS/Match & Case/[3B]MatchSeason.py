operator = input("Operator (+, -, *): ")
a = 8
b = 4
match operator:
    case "+": print(a + b)
    case "-": print(a - b)
    case "*": print(a * b)
    case _: print("Unsupported operator")
