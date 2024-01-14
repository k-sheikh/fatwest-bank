from user import User
from account import Account
from utilities import generate_user_id, generate_account_number
import sqlite3
from database import create_connection
from database import get_password_by_user_id

class Bank:
    def __init__(self):
        self.conn = create_connection()

    def register_user(self, forename, surname, password):
        user_id = generate_user_id(forename, surname)
        try:
            c = self.conn.cursor()
            c.execute("INSERT INTO users (user_id, forename, surname, password) VALUES (?, ?, ?, ?)",
                      (user_id, forename, surname, password))
            self.conn.commit()
        except sqlite3.IntegrityError:
            raise ValueError("User ID already exists")
        except Exception as e:
            raise e
        return User(forename, surname, user_id, password)
    
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
         if stored_password is None:
              print("User ID does not exist.")
              return False
         elif stored_password == password:
              print("Login successful.")
              return True
         else:
              print("Incorrect password.")
              return False