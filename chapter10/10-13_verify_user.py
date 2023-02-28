import json

def get_stored_username():
    filename = "chapter10/username.json"
    try:
        with open(filename) as f:
            stored_username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return stored_username

def verify_username():
    stored_username = get_stored_username()
    username = input("Hello, what is your name? ")
    print("\nVerifying username...")
    if stored_username == None:
        get_new_username(username)
    elif username == stored_username:
        greet_user(username)
    else:
        get_new_username()
        
        
def get_new_username(username):
    """Prompt for a new username."""
    filename = 'chapter10/username.json'
    print(f"We'll remember you when you come back, {username}!")
    with open(filename, 'w') as f:
            json.dump(username, f)
            return username
    

def greet_user(username):
    """Greet user by name."""
    print(f"Welcome back, {username}!")
    

verify_username()