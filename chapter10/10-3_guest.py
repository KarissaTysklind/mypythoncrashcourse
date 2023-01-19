filename = 'chapter10/guest.txt'
username = input("Hello, what is your name?: ")

with open(filename, 'w') as file:
    file.write(f"{username.title()}")

