class User:
    def __init__(self, forename, surname, user_id, password):
        self.forename = forename
        self.surname = surname
        self.user_id = user_id
        self.password = password
        self.accounts = {}

    def add_account(self, account):
        # Add an account to the user
        self.accounts[account.account_number] = account

    def get_account(self, account_number):
        # Retrieve a specific account
        return self.accounts.get(account_number)