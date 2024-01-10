# -----LIBRARIES-----

import random


# -----UTILITY FUNCTIONS-----

def generate_user_id(forename, surname):
    return f"{forename[0].lower()}{surname[:5].lower()}{random.randint(1000, 9999)}"


def generate_account_number():
    return random.randint(10000000, 99999999)