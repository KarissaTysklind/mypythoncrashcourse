import json

filename = 'chapter10/Practice/username.json'

with open(filename) as f:
    username = json.load(f)
    print(f"Welcome back, {username}!")