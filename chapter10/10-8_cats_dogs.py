cats_filename = 'chapter10/cats.txt'
dogs_filename = 'chapter10/dogs.txt'

def read_file(filename):
    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
            print(contents)
    except FileNotFoundError:
        print(f"The file {filename} does not exist.")

filenames = [cats_filename, dogs_filename]

for filename in filenames:
    read_file(filename)
