# BANKING ENVIRONMENT

# -----LIBRARIES-----

from bank import Bank
from sys import exit
import re
import stdiomask


# -----FUNCTIONS-----

# Welcome message
def welcome():
    print("\nWelcome to FatWest Bank")


# Input validator
def get_validated_input(prompt, valid_options):
    user_input = input(prompt)
    while user_input not in valid_options:
        print("\nInput is not valid.")
        user_input = input(prompt)
    return user_input


# Main menu
def main_menu(bank):
    user_input = get_validated_input("""Please select from one of the following options:
1 - Login
2 - Register
3 - Exit
: """, ['1', '2', '3'])
    
    if user_input == '1':
        pass  # Placeholder for future login functionality
    elif user_input == '2':
        register_new_user(bank)
    elif user_input == '3':
        print("\nThankyou for banking with FatWest. Goodbye!")
        exit()


# Register new user
def register_new_user(bank):
    try:
        forename, surname = get_user_name()
        password = get_user_password()

        new_user = bank.register_user(forename, surname, password)
        user_id = new_user.user_id

        print(f"""\nCongratulations {forename}, your account has been created successfully.
Your user id is {user_id}. Please keep this information safe.""")
    except Exception as e:
        print(f"An error occurred during registration: {e}")


def get_user_name():
    while True:
        forename = input("\nPlease enter your forename: ")
        surname = input("Please enter your surname: ")
        name_validation = input(
            f"Your name is {forename} {surname}, is this correct? Yes/No: ")
        if name_validation.lower() == 'yes':
            return forename, surname


def get_user_password():
    print("\nPlease create a password.")
    while True:
        password = stdiomask.getpass("""Passwords must be alphanumerical,
must contain at least one uppercase letter,
must contain at least one lowercase letter,
must contain at least 8 characters.
Create a password now:  """, mask="*")

        if validate_password(password):
            password2 = stdiomask.getpass("Please re-enter your password: ")
            if password == password2:
                return password
            else:
                print("\nPasswords do not match. Please start again.")
        else:
            print("\nInvalid password, please try again.")


def validate_password(password):
    return (len(password) >= 8 and
            re.search("[a-z]", password) and
            re.search("[A-Z]", password) and
            re.search("[0-9]", password))


# -----MAIN PROGRAM-----

if __name__ == "__main__":
    from database import initialise_database
    initialise_database()  # Initialise database on program start
    fatWestBank = Bank()
    while True:
        welcome()
        main_menu(fatWestBank)