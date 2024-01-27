from user import User
from account import Account
from utilities import generate_user_id, generate_account_number
import sqlite3
from database import create_connection
from database import get_password_by_user_id
import bcrypt

class Bank:
    """
    Represents a banking system, handling operations related to user registration, 
    account management, and interactions with the database.
    """

    def __init__(self):
        """
        Initializes the Bank instance, setting up a connection to the database.
        """
        self.conn = create_connection()

    def register_user(self, forename, surname, password):
        """
        Registers a new user in the system with provided personal details.

        Parameters:
            forename (str): The user's first name.
            surname (str): The user's last name.
            password (str): The user's password, which will be hashed for security.

        Returns:
            str: The unique user ID generated for the new user.
        """
        user_id = generate_user_id(forename, surname)
        hashed_password = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())
        try:
            with self.conn:
                c = self.conn.cursor()
                c.execute("INSERT INTO users (user_id, forename, surname, password) VALUES (?, ?, ?, ?)",
                          (user_id, forename, surname, hashed_password))
        except sqlite3.IntegrityError:
            raise ValueError("User ID already exists")
        except Exception as e:
            raise e
        return User(forename, surname, user_id, hashed_password)
    
    def create_account(self, user_id, account_type):
            """
            Creates a new account for the user with the specified account type.

            Parameters:
                user_id (str): The user ID of the account holder.
                account_type (str): The type of the new account (e.g., 'savings', 'checking').

            Returns:
                Account: The newly created Account object if successful, else None.
            """
            account_number = generate_account_number()
            try:
                c = self.conn.cursor()
                c.execute("INSERT INTO accounts (account_number, user_id, account_type, balance) VALUES (?, ?, ?, ?)",
                        (account_number, user_id,account_type, 0))
                self.conn.commit()
            except sqlite3.IntegrityError:
                 raise ValueError("Account number already exists")
            except Exception as e:
                 raise e
            return Account(account_number, account_type)
    
    def login_user(self, user_id, password):
        """
        Logs in a user with the given username and password.

        Parameters:
            username (str): The username of the user.
            password (str): The password of the user.

        Returns:
            User: The logged-in User object if credentials are valid, else None.
        """
        stored_password = get_password_by_user_id(self.conn, user_id)
        if stored_password:
            if bcrypt.checkpw(password.encode("utf-8"), stored_password):
                print("\nLogin successful.")
                return True
            else:
                print("\nIncorrect password. Please try again.")
                return False
        else:
            print("User not found. Please register.")
            return False
            

    def user_exists(self, user_id):
         """
        Checks if a user with the given user id already exists in the database.

        Parameters:
            user_id (str): The user id to check for existence.

        Returns:
            bool: True if the user id exists, False otherwise.
        """
         stored_password = get_password_by_user_id(self.conn, user_id)
         return stored_password is not None