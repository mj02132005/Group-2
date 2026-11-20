def analyze_number(number):
    return {"square": number ** 2, "cube": number ** 3, "even": number % 2 == 0}

result = analyze_number(6)
for key, value in result.items():
    print(key, value)
