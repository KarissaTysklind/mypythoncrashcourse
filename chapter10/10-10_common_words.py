def word_count(filename, word):
    file_title_list = filename.split("/")
    file_title = file_title_list[-1]

    with open(filename, encoding='utf-8') as f:
        file_text = f.read()
        word_count = file_text.lower().count(word)
    
    if word_count == 0:
        print(f"The word '{word}' does not appear in the file {file_title}.")
    else:    
        print(f"The word '{word}' appears {int(word_count)} times in the file {file_title}.")


filenames = ['chapter10/Practice/alice.txt', 'chapter10/Practice/moby_dick.txt', 'chapter10/Practice/little_women.txt']

for filename in filenames:
    word_count(filename, " oz ")