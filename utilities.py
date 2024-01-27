# -----LIBRARIES-----

import random


# -----UTILITY FUNCTIONS-----

def generate_user_id(forename, surname):
    """
    Generates a unique user ID based on the user's name and a random number.

    The user ID is constructed by taking the first letter of the forename, 
    the first five letters of the surname (or the entire surname if it's shorter), 
    and a random four-digit number. This combination helps in creating a unique ID for each user.

    Parameters:
        forename (str): The forename of the user.
        surname (str): The surname of the user.

    Returns:
        str: A unique user ID.
    """
    return f"{forename[0].lower()}{surname[:5].lower()}{random.randint(1000, 9999)}"


def generate_account_number():
    """
    Generates a random, unique account number.

    This function creates an 8-digit random number that serves as an account number. 
    The randomness ensures that each account number is unique.

    Returns:
        int: An 8-digit random account number.
    """
    return random.randint(10000000, 99999999)