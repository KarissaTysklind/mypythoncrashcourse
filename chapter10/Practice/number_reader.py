import json

filename = 'chapter10/Practice/numbers.json'

with open(filename) as f:
    numbers = json.load(f)

print(numbers)
