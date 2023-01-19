glossary = {
        "variable": "a variable is a reusable value that can change", 
        "constant": "a constant is a reusable value that cannot change",
        "list": "a list is a data type that stores multiple values, is ordered and is mutable",
        "integer": "an integer is a data type that stores whole numbers",
        "float": "a float is a data type that stores decimal numbers"
        }

for word, definition in glossary.items():
    print("\n" + word.title() + ":\n" + definition)
