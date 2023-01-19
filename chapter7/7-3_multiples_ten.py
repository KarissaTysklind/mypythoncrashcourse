prompt = "Type a number:"
number = int(input(prompt))
if (number % 10) == 0:
    print(f"{number} is multiple of 10.")
else:
    print(f"{number} is not multiple of 10.")

