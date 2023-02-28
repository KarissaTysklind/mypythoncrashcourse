import json

filename = "chapter10/my_fav_num.json"

with open(filename) as f:
    fav_num = json.load(f)
    print(fav_num)