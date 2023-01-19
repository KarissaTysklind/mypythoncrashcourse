favourite_numbers = {
        "karissa": [6, 22, 11],
        "cynthia": [26, 14, 3],
        "ammar":[8, 10, 27],
        "shan":[18, 40, 38],
        "andre":[1, 10, 100]}

for person, numbers in favourite_numbers.items():
    print(f"\n{person.title()}'s favourite numbers are:")
    for num in numbers:
        print(f"\t{str(num)}")
