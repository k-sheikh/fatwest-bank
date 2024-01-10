import sqlite3

def create_connection():
    """Create a database connection to a SQLite database."""
    conn = None
    try:
        conn = sqlite3.connect('banking.db')
    except Exception as e:
        print(e)
    return conn

def initialise_database():
    sql_create_users_table = """CREATE TABLE IF NOT EXISTS users (
                                    user_id TEXT PRIMARY KET,
                                    forname TEXT NOT NULL,
                                    surname TEXT NOT NULL,
                                    password TEXT NOT NULL
                                    )"""
    
    sql_create_accounts_table = """CREATE TABLE IF NOT EXISTS accounts (
                                        account_number INTEGER PRIMARY KEY,
                                        user_id TEXT NOT NULL,
                                        account_type TEXT NOT NULL,
                                        balance REAL NOT NULL,
                                        FOREIGN KEY (user_id) REFERENCES users (user_id)
                                        )"""
    
    conn = create_connection()
    if conn is not None:
        try:
            c = conn.cursor()
            c.execute(sql_create_users_table)
            c.execute(sql_create_accounts_table)
        except Exception as e:
            print(e)
        finally:
            conn.close()

if __name__ == "__main__":
    initialise_database()