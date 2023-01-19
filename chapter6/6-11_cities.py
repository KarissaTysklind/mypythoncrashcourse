cities = {
        "madrid": {
            "country": "spain",
            "population": "3m",
            "language": "spanish"
            },
        "london": {
            "country": "united kingdom",
            "population": "8m",
            "language": "english"
            },
        "geneva": {
            "country": "switzerland",
            "population": "200k",
            "language": "french"
            }
        }

for city, details in cities.items():
    print(f"\n{city.title()}:")
    for key, value in details.items():
        print(f"\t{key.title()}: {value.title()}")



