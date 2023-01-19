filename = 'chapter10/poll_responses.txt'
promt = "Why do you like programming: "

active = True

while active:
    reason = input(promt)
    print("Enter 'q' to quit.")
    if reason == 'q':
        active = False
    else:
        with open(filename, 'a') as file:
            file.write(f"\n{reason}")
        

        
