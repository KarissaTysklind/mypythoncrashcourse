import json

filename = "chapter10/my_fav_num.json"

with open(filename, 'w') as f:
    fav_num = input("What is your favourite number? ")
    json.dump(fav_num, f)