from user import User
from account import Account
from utilities import generate_user_id, generate_account_number
import sqlite3
from database import create_connection

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