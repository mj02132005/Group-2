username = input("Username: ")
if username == "admin":
    password = input("Password: ")
    if password == "letmein":
        print("Access granted")
    else:
        print("Incorrect password")
else:
    print("Unknown user")
