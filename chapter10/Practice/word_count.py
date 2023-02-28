def count_words(filename):
    """Count the approximate number of words in a file."""
    title_list = filename.split("/")
    title = title_list[-1]
    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()      
    except FileNotFoundError:
        pass
    else:
        words = contents.split()
        num_words = len(words)
        print(f"The file {title} has about {num_words} words.")

filenames = ['chapter10/Practice/alice.txt', 'siddhartha.txt', 'chapter10/Practice/moby_dick.txt', 'chapter10/Practice/little_women.txt']
for filename in filenames:
    count_words(filename)