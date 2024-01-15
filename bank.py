from user import User
from account import Account
from utilities import generate_user_id, generate_account_number
import sqlite3
from database import create_connection
from database import get_password_by_user_id
import bcrypt

class Bank:
    def __init__(self):
        self.conn = create_connection()

    def register_user(self, forename, surname, password):
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
         stored_password = get_password_by_user_id(self.conn, user_id)
         return stored_password is not None