current_users = ["admin", "KaRissa", "cynthia", "aMmar", "shan", "umme"]
new_users = ["andre", "CynThia", "david", "leylah", "AMMAR"]
current_users_lower = []

for user in current_users:
    current_users_lower.append(user.lower())

for user in new_users:
    if user.lower() in current_users_lower:
        print("The username {} is already being used. Please, enter a new one.".format(user))
    else:
        print("The username {} is available.".format(user))



