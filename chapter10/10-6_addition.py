print("Enter two numbers to add them up.")
print("Enter 'q' to quit.")




while True:
    first_number = input("\nEnter first number: ")
    if first_number == 'q':
        break
    second_number = input("\nEnter second number: ")
    if second_number == 'q':
        break
    try:
        answer = int(first_number) + int(second_number)
    except ValueError:
        print("You must enter numberical values.")
    else:
        print(answer)
        



