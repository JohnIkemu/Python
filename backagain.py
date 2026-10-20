username_correct = False

for attempt in range(4):
    username = input("Enter username: ")
    if username == "admin":
        print("correct username")
        username_correct = True

