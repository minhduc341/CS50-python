# Password Manager App
## Video Demo: 
[Demo Video Link](<https://youtu.be/oqBr-IfdeNA>)

## Description:
This is a Python password management application that allows users to manage their passwords for different accounts. Users can add, view, delete and update passwords for different accounts. This application also provides the option to create highly secure passwords for users.

In "Add password" function, users can choose between automatically generating a password or entering a password from the keyboard.

Optionally, users can also customize the password generating function with options for the number of characters in the password, whether the password includes capital letters, or special characters.

## Files in the Project:

### `project.py`

The main script of this application. It includes functions for main menu, adding, viewing, updating, and deleting passwords, as well as setting password generation.

### `test_project.py`

A set of pytest test cases to ensure the correctness and robustness of some functions such as: add_password, update_password, delete_password.

### `passwords.json`

A JSON file used to store passwords. The file structure includes account types, usernames and passwords.

### `requirement.txt`

A list of every `pip`-installable library required by the project

## Design Choices:

- **Basic functions:** Users can add, view, delete and update passwords for different accounts.

- **Setting Password Generation:** Users can configure password generator function, including length, uppercase letters, numbers, and symbols.

- **Sorted Account Types:** Account types are stored in a sorted order for easier navigation and management.

- **Error Handling:** The application includes error handling for cases where the user does not enter what is required.

## How to Use:

1. Run `python project.py` to start the Password Manager.

2. Choose from the menu options to add, view, update, or delete passwords, setting password generation, or exit the application.

3. Follow the prompts and input requirements.