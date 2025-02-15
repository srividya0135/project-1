import random

# generate a random username
def generate_username(adjectives, nouns):
    adjective = random.choice(adjectives)
    noun = random.choice(nouns)
    return f"{adjective}{noun}"

# Function to generate a custom username
def generate_custom_username(adjectives, nouns, include_number=True, include_special_char=False):
    adjective = random.choice(adjectives)
    noun = random.choice(nouns)
    username = f"{adjective}{noun}" #dynamic string formatting
    
    if include_number:
        username += str(random.randint(0, 999))
    if include_special_char:
        special_chars = ["!", "@", "#", "$", "%"]
        username += random.choice(special_chars)
    return username

# Function to save the username to a file
def save_username_to_file(username, filename="usernames.txt"):
    with open(filename, "a") as file:
        file.write(username + "\n")
    print(f"Username '{username}' saved to {filename}")

# Function to get valid user input (yes/no)
def get_valid_input(prompt):
    while True:
        user_input = input(prompt).strip().lower()
        if user_input in ["yes", "no"]:
            return user_input
        else:
            print("Enter valid input (yes/no):")


adjectives = ["Cool", "Happy", "Mighty", "Silent", "Brave", "Joyful", "Ferocious","Elegant","Fierce","tech", "Gentle", "Clever", "Bold","warrior",]
nouns = ["Tiger", "Dragon", "Eagle", "Lion", "Wolf", "Panther", "Phoenix", "Hawk", "Shark", "Bear","King","Soul","Girl","Boy","queen","prince",]
include_number = get_valid_input("Include numbers in username? (yes/no): ") == "yes"
include_special_char = get_valid_input("Include special characters in username? (yes/no): ") == "yes"
    
while True:
    username = generate_custom_username(adjectives, nouns, include_number, include_special_char)
    print(f"Generated Username: {username}")
        
    like_username = get_valid_input("Do you like this username? (yes/no): ")
    if like_username == "yes":
        save_username_to_file(username)
        break


