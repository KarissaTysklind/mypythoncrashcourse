responses = {}
prompt = "\nIf you could visit anywhere in the world, where would you go?"

polling_active = True

while polling_active:
    name = input("\nWhat is your name?\n")
    response = input(prompt)

    responses[name] = response

    repeat = input("\nWould you like to let another person respond? (yes/no)")
    if repeat == "no":
        polling_active = False

print("\n ----Poll Results----")
for name, response in responses.items():
    print(f"\n{name.title()} would like to visit {response.title()}.")