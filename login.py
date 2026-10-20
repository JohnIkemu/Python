# ----- Setup -----
correct_username = "admin"      # the username we're checking against
correct_password = "1234"       # the password we're checking against
count = 0                       # tracks how many attempts have been used (max 4)
username_correct = False        # flag: becomes True once the username is verified

# ----- Username verification loop -----
# Runs as long as we still have attempts left (count < 4)
while count < 4:
    username = input("Enter username: ")   # ask the user to type a username
    count += 1                             # this attempt counts against the max of 4

    if username == correct_username:
        # Correct username entered
        username_correct = True   # mark username as verified
        count = 0                 # reset attempts so the password loop gets its own fresh 4 tries
        break                     # exit the username loop immediately

    else:
        # Wrong username entered
        if count < 4:
            # Attempts remain, let them try again
            print("Incorrect username. Try again.")
            continue              # go back to the top of the while loop
        else:
            # No attempts left
            print("Account locked.")
            break                 # exit the loop (locked out)

# ----- Password verification loop -----
# Only runs if the username was successfully verified above (username_correct == True)
# and there are still attempts left (count < 4, freshly reset to 0 on success)
while count < 4 and username_correct == True:
    password = input("Enter password: ")   # ask the user to type a password
    count += 1                             # this attempt counts against the max of 4

    if password == correct_password:
        # Correct password entered
        print("Login successful.")
        break                     # exit the loop, login complete

    else:
        # Wrong password entered
        if count < 4:
            # Attempts remain, let them try again
            print("Incorrect password. Try again.")
            continue              # go back to the top of the while loop
        else:
            # No attempts left
            print("Account locked.")
            break                 # exit the loop (locked out)