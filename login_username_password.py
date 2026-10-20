username_correct = False

for attempt in range(4):
    user_name = input("Enter username: ")
    if user_name == "admin":
        print("correct username")
        username_correct = True
        break
    else:
        print("incorrect username")

if username_correct == True:
    for attempt in range(4):
       password_correct = False
       password = input("Enter password: ")
       if  password == "admin":
           print("login successful")
           password_correct = True
           break
       else:
        print("incorrect password")
    if  password_correct == False:
        print("access denied")
else:
     print("access denied")