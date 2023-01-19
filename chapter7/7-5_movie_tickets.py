prompt = "\nWhat is your age?\n"


while True:
    age = int(input(prompt))
    if age < 3:
        print("\nThe ticket is free.")
    elif age < 12:
        print("\nThe ticket is $10.")
    else:
        print("\nThe ticket is $15.")
