favourite_languages = {
    "jen": "python",
    "sarah": "c",
    "edward": "ruby",
    "phil": "python",

}

#for name, language in favourite_languages.items():
    #print(name.title() + "'s favourite language is " + language.title())

poll = ["jen", "edward", "karissa", "cynthia"]

for person in poll:
    if person in favourite_languages.keys():
        print(f"Thank you, {person.title()}, for taking part in the poll.")
    else:
        print(f"{person.title()}, would you like to take part in the poll")
        