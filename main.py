# BANKING ENVIRONMENT

# -----LIBRARIES-----

from bank import Bank
from sys import exit
import re
import stdiomask
from database import initialise_database
from database import get_forename_by_user_id


# -----FUNCTIONS-----

def welcome():
    """
    Display a welcome message to the user.
    """
    print("\nWelcome to FatWest Bank")


def get_validated_input(prompt, valid_options):
    """
    Get input from the user and validate it against a set of valid options.

    Args:
    prompt (str): The prompt to display to the user.
    valid_options (list): A list of valid input operations.

    Returns:
    str: The validated user input.
    """
    user_input = input(prompt)
    while user_input not in valid_options:
        print("\nInvalid input. Please try again.")
        user_input = input(prompt)
    return user_input


def main_menu(bank):
    """
    Display the main menu options and handle user selection.

    Args:
    bank (Bank): The Bank object to perform operations.
    """
    user_input = get_validated_input("""\nPlease select from one of the following options:
1 - Login
2 - Register
3 - Exit
: """, ['1', '2', '3'])
    
    if user_input == '1':
        login(bank)
    elif user_input == '2':
        register_new_user(bank)
    elif user_input == '3':
        print("\nThankyou for banking with FatWest. Goodbye!")
        exit()


def register_new_user(bank):
    """
    Handle the registration of a new user.

    Args:
    bank (Bank): The Bank object to perform operations.
    """
    try:
        forename, surname = get_user_name()
        password = get_user_password()

        new_user = bank.register_user(forename, surname, password)
        user_id = new_user.user_id

        print(f"""\nCongratulations {forename}, your account has been created successfully.
Your user id is {user_id}. Please keep this information safe.
You can now login with your credentials to open an account.""")
    except Exception as e:
        print(f"An error occurred during registration: {e}")


def get_user_name():
    """
    Get the user's forename and surname with validation.

    Returns:
    tuple: A tuple containing the forename and surname.
    """
    while True:
        forename = input("\nPlease enter your forename: ")
        surname = input("Please enter your surname: ")
        name_validation = input(
            f"Your name is {forename} {surname}, is this correct? Yes/No: ")
        if name_validation.lower() == 'yes':
            return forename, surname


def get_user_password():
    """
    Get and validate the user's password.

    Return:
    str: The validated password.
    """
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
    """
    Validate a password based on given criteria.

    Args:
    password (str): The password to validate.

    Returns:
    bool: True if the password is valid, otherwise False.
    """
    return (len(password) >= 8 and
            re.search("[a-z]", password) and
            re.search("[A-Z]", password) and
            re.search("[0-9]", password))


def login(bank):
    """
    Handle the user login process.

    Args:
    bank (Bank): The Bank object to perform operations.

    Returns:
    bool: True if login is successful, otherwise False.
    """
    user_id = input("\nPlease enter your user ID: ")

    if bank.user_exists(user_id):
        password = stdiomask.getpass("Please enter your password: ", mask="*")
        if bank.login_user(user_id, password):
            # Add login operations here
            user_forename = get_forename_by_user_id(bank.conn, user_id)
            if user_forename:
                user_menu(user_forename, user_id)
            else:
                print("User forename could not be retrieved.")
            return True
        else:
            return False
    else:
        print("\nInvalid input. User ID does not exist.")
        return False


def user_menu(user_forename, user_id):
    print(f"\nWelcome back {user_forename}!")
    while True:  # Keep showing the user menu until the user decides to log out
        choice = get_validated_input(f"""\nPlease select from one of the following options
1 - Check active accounts
2 - Open a new account
3 - Log out
: """, ['1', '2', '3'])
    
        if choice == '1':
            # Add functionality to check active accounts
            pass
        elif choice == '2':
            # Add functionality to open a new account
            open_new_account(user_forename, user_id)
            pass
        elif choice == '3':
            print(f"\nYou have been logged out successfully. Goodbye {user_forename}!")
            return  # Exit the loop and return to the main menu


def open_new_account(user_forename, user_id):
    choice = get_validated_input(f"""\nWhat type of account would you like to open?                                   
1 - Current Account
2 - Savings Account
3 - Go back
: """, ['1', '2', '3'])
        
    if choice == '1':
        # Add functionality to open a current account
        pass
    elif choice == '2':
        # Add functionality to open a savings account
        pass
    elif choice == '3':
        # This will take the user back to the user menu
        return True


# -----MAIN PROGRAM-----

if __name__ == "__main__":
    # Initialise the database required for the banking application.
    initialise_database()

    # Create an instance of the Bank class to manage banking operations.
    fatWestBank = Bank()

    # Enter the main loop of the program: display welcome message and show the main menu.
    while True:
        welcome()
        main_menu(fatWestBank)