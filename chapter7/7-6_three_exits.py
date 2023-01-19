prompt = "\nWhat is your age?\n"
active = True
while active:
    age = input(prompt)
    if age == "quit":
        break
    elif int(age) < 3:
        print("\nThe ticket is free.")
    elif int(age) < 12:
        print("\nThe ticket is $10.")
    else:
        print("\nThe ticket is $15.")
