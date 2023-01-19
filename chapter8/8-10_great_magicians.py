magicians = ["harry potter", "albus dumbledore", "minerva mcgonagal", "hermione ganger", "ron weasley"]

def make_great(magicians):
    for index in range(0, len(magicians)):
        magicians[index] = f"{magicians[index].title()} the Great"
    return magicians

def show_magicians(magicians):
    for magician in magicians:
        print(magician.title())

make_great(magicians)
show_magicians(magicians)

