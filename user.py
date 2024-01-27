class User:
    """
    Represents a user in the banking system.

    Attributes:
        forename (str): The forename of the user.
        surname (str): The surname of the user.
        user_id (str): The unique identifier for the user.
        password (str): The password for the user.
        accounts (dict): A dictionary of accounts associated with the user, 
                         where keys are account numbers and values are Account objects.
    """

    def __init__(self, forename, surname, user_id, password):
        """
        Initializes a new User instance with the given details.

        Parameters:
            forename (str): The forename of the user.
            surname (str): The surname of the user.
            user_id (str): The unique identifier for the user.
            password (str): The password for the user.
        """
        self.forename = forename
        self.surname = surname
        self.user_id = user_id
        self.password = password
        self.accounts = {}

    def add_account(self, account):
        """
        Adds an account to the user's list of accounts.

        Parameters:
            account (Account): The account object to be added to the user's accounts.
        """
        self.accounts[account.account_number] = account

    def get_account(self, account_number):
        """
        Retrieves a specific account associated with the user by account number.

        Parameters:
            account_number (str): The account number of the account to retrieve.

        Returns:
            Account: The account object associated with the given account number, if found; otherwise, None.
        """
        return self.accounts.get(account_number)