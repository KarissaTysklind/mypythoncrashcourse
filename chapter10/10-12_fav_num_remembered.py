import json

filename = "chapter10/my_fav_num.json"

try:
    with open(filename) as f:
        fav_num = json.load(f)
        print (f"I remember your favourite number, it's {fav_num}!")
except FileNotFoundError:
    print(f"Sorry, I don't know your favourite number.")
    with open(filename, 'w') as f:
        fav_num = input("What is your favourite number? ")
        json.dump(fav_num, f)

