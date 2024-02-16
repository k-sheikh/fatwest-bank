import sqlite3


def create_connection():
    """
    Create a database connection to a SQLite database.

    This function establishes a connection to a SQLite database named 'banking.db'. 
    If the connection is successful, it returns the connection object; otherwise, it prints an error message.

    Returns:
        sqlite3.Connection: A connection object to the SQLite database, or None if the connection fails.
    """
    conn = None
    try:
        conn = sqlite3.connect('banking.db')
    except Exception as e:
        print(e)
    return conn


def initialise_database():
    """
    Initializes the database by creating necessary tables.

    This function creates a 'users' table in the SQLite database if it does not already exist. 
    The table includes columns for user ID, forename, surname, and password.

    No parameters or returns. Any exceptions during the table creation are caught and printed.
    """
    sql_create_users_table = """CREATE TABLE IF NOT EXISTS users (
                                    user_id TEXT PRIMARY KEY,
                                    forename TEXT NOT NULL,
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


# Verify login password
def get_password_by_user_id(conn, user_id):
    """
    Retrieves the password for a given user ID from the database.

    This function queries the 'users' table in the database to find the password associated with the specified user ID. It returns the password if found, or None if the user ID does not exist or an error occurs.

    Parameters:
        conn (sqlite3.Connection): The database connection object.
        user_id (str): The user ID for which to retrieve the password.

    Returns:
        str or None: The password associated with the user ID if found, otherwise None.

    Raises:
        Exception: If any database operation error occurs, it is caught and printed, and None is returned.
    """
    try:
        c = conn.cursor()
        c.execute("SELECT password FROM users WHERE user_id = ?", (user_id,))
        result = c.fetchone()
        return result[0] if result else None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None


# Verify login password
def get_forename_by_user_id(conn, user_id):
    """
    Retrieves the forename for a given user ID from the database.

    This function queries the 'users' table in the database to find the forename associated with the specified user ID. It returns the forename if found, or None if the user ID does not exist or an error occurs.

    Parameters:
        user_id (str): The user ID for which to retrieve the password.

    Returns:
        str or None: The password associated with the user ID if found, otherwise None.

    Raises:
        Exception: If any database operation error occurs, it is caught and printed, and None is returned.
    """
    try:
        c = conn.cursor()
        c.execute("SELECT forename FROM users WHERE user_id = ?", (user_id,))
        result = c.fetchone()
        return result[0]
    except Exception as e:
        print(f"An error occurred: {e}")
        return None
    

# Initialize the database by creating necessary tables when this script is run directly.
if __name__ == "__main__":
    initialise_database()