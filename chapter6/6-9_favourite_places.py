favourite_places = {
        "karissa":["madrid", "london", "stokholm"],
        "cynthia": ["nairobi", "cape town", "seul"], 
        "shan":["bangladesh", "mecca", "zanzibar"],
        "ammar": ["mashad", "kashmir","tokio"]
        }

for person, places in favourite_places.items():
    print(f"\n{person.title()}'s favourite places are:")
    for place in places:
        print(f"\t{place.title()}")




