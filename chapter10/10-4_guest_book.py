filename = 'chapter10/guest_book.txt'
promt = "Enter your name:"

active = True

while active:
    name = input(promt)
    print("Enter 'q' to quit.")
    if name == 'q':
        active = False
    else:
        with open(filename, 'a') as file:
            file.write(f"\n{name}")
        

        
