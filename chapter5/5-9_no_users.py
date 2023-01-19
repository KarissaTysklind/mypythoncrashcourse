usernames = []

for username in usernames:
    if username != "admin":
        print("Hello {} thank you for logging in again.".format(username.title()))
    elif username == "admin":
        print("\nHello admin, would you like to see a status report?")
if usernames == []:
    print("We need to find some users!")
    