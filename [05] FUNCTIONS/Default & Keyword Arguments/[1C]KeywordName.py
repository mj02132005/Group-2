def create_username(first_name, last_name, separator="_"):
    return first_name.lower() + separator + last_name.lower()

print(create_username("Alex", "Reyes"))
print(create_username("Alex", "Reyes", "."))
