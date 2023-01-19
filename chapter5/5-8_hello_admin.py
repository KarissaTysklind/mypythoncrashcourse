usernames = ["admin", "karissa", "cynthia", "ammar", "shan", "umme"]

for username in usernames:
    if username == "admin":
        print("\nHello admin, would you like to see a status report?")
    else:
        print("Hello {} thank you for logging in again.".format(username.title()))
   