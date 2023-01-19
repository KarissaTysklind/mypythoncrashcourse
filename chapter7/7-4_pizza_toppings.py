prompt = "\nWhat toppings would you like?"
prompt += "\nEnter 'quit' when you are finished.\n"

topping = input(prompt)

while topping != "quit":
    print(f"\n{topping} has been added to your pizza.")
    prompt = "\nwould you like any more toppings?"
    topping = input(prompt)
    

