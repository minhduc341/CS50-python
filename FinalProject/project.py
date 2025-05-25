import json
import random
import string
from pyfiglet import Figlet

# Password features
password_length = 12
password_uppercase = True
password_lowercase = True # This will always be True
password_numbers = True
password_symbols = True

def main():
    passwords_file = load_passwords()

    # Greeting 
    figlet = Figlet()
    figlet.width = 120
    figlet.setFont(font = 'slant')
    print(figlet.renderText("Wellcome to"))
    print(figlet.renderText("Password Manager"))

    while True:
        print("\n######################")
        print("Password Manager Menu:")
        print("1. Add Password")
        print("2. View Passwords")
        print("3. Update Password")
        print("4. Delete Password")
        print("5. Setting Password Generation")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            add_password(passwords_file)
        elif choice == '2':
            view_passwords(passwords_file)
        elif choice == '3':
            update_password(passwords_file)
        elif choice == '4':
            delete_password(passwords_file)
        elif choice == '5':
            generate_password_setting()
        elif choice == '6':
            print("\nGoodbye!!!")
            save_passwords(passwords_file)
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

def load_passwords():
    try:
        with open('passwords.json', 'r') as file:
            passwords_file = json.load(file)
    except FileNotFoundError:
        passwords_file = {"accounts": {}}
        save_passwords(passwords_file)  # Create file passwords.json if it doesn't exist
    return passwords_file

def save_passwords(passwords_file):
    # Soft account type 
    passwords_file["accounts"] = dict(sorted(passwords_file["accounts"].items()))

    with open('passwords.json', 'w') as file:
        json.dump(passwords_file, file, indent=2)

# Generate password
def generate_password():
    characters = ""

    if password_uppercase:
        characters += string.ascii_uppercase
    if password_lowercase:
        characters += string.ascii_lowercase
    if password_numbers:
        characters += string.digits
    if password_symbols:
        characters += string.punctuation

    if password_length < 1:
        raise ValueError("Password length must be at least 1.")

    password = ''.join(random.choice(characters) for _ in range(password_length))
    return password

def generate_password_setting():
    global password_length, password_uppercase, password_numbers, password_symbols

    print("\nSetting Password Generation:")
    while True:
        try:
            password_length = int(input("Enter the password length: "))
            if password_length < 1:
                raise ValueError("Password length must be at least 1.")
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    while True:
        uppercase_choice = input("Include Uppercase? (y/n): ").lower()
        if uppercase_choice in ['y', 'n']:
            password_uppercase = uppercase_choice == 'y'
            break
        else:
            print("Invalid choice. Please enter 'y' for YES or 'n' for NO.")

    while True:
        numbers_choice = input("Include Numbers? (y/n): ").lower()
        if numbers_choice in ['y', 'n']:
            password_numbers = numbers_choice == 'y'
            break
        else:
            print("Invalid choice. Please enter 'y' for YES or 'n' for NO.")

    while True:
        symbols_choice = input("Include Symbols? (y/n): ").lower()
        if symbols_choice in ['y', 'n']:
            password_symbols = symbols_choice == 'y'
            break
        else:
            print("Invalid choice. Please enter 'y' for YES or 'n' for NO.")

    try:
        password = generate_password()
        print(f"\nGenerate An Example Password: {password}")
    except ValueError as e:
        print(f"Error: {e}")

# Add password
def add_password(passwords_file):
    print("\n######################")
    print("Add password:")
    account_type = input("Enter the account type: ")
    username = input("Enter the username: ")

    # Check if the account type exists in the passwords dictionary
    if account_type not in passwords_file["accounts"]:
        passwords_file["accounts"][account_type] = {}

    # Ask if user want to generate a password
    while True:
        generate_password_choice = input("Do you want to generate a password? (y/n): ").lower()

        if generate_password_choice == "y":
            password = generate_password()
            passwords_file["accounts"][account_type][username] = {"password": password}
            print(f"Generated Password for {account_type}:")
            print(f"    Username: {username}")
            print(f"    Password: {password}")
            return
        elif generate_password_choice == "n":
            # Let the user set their own password
            password = input("Enter the password: ")
            passwords_file["accounts"][account_type][username] = {"password": password}
            print(f"Password for {account_type}:")
            print(f"    Username: {username}")
            print(f"    Password: {password}")
            print("added successfully.")
            return
        else:
            print("Invalid choice. Please enter 'y' for YES or 'n' for NO.")

# View all passwords
def view_passwords(passwords_file):
    
    print("\nStored Passwords:")
    for account_type, accounts in passwords_file["accounts"].items():
        print(f"\n{account_type} Accounts:")
        for username, details in accounts.items():
            print(f"Username: {username} - Password: {details['password']}")

# Update password
def update_password(passwords_file):
    print("\n######################")
    print("Update password:")
    account_type = input("Enter the account type to update: ")
    username = input("Enter the username to update: ")
    
    # Check if the account type and name exist
    if account_type in passwords_file["accounts"] and username in passwords_file["accounts"][account_type]:
        new_password = input("Enter the new password: ")
        passwords_file["accounts"][account_type][username]["password"] = new_password
        print(f"Password for {account_type} - {username} updated successfully.")
    else:
        print(f"Username {username} in account type {account_type} not found.")

# Delete password
def delete_password(passwords_file):
    print("\n######################")
    print("Delete password:")
    account_type = input("Enter the account type to delete: ")
    username = input("Enter the username to delete: ")
    
    # Check if the account type and name exist
    if account_type in passwords_file["accounts"] and username in passwords_file["accounts"][account_type]:
        del passwords_file["accounts"][account_type][username]
        print(f"Password for {account_type} - {username} deleted successfully.")
    else:
        print(f"Username {username} in account type {account_type} not found.")

if __name__ == "__main__":
    main()
