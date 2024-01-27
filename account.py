class Account:
    """
    Represents a bank account, allowing for basic transactions such as deposits and withdrawals.

    Attributes:
        account_number (str): The account number as a unique identifier.
        account_type (str): The type of account (e.g., savings, checking).
        balance (float): The current balance of the account.
    """
    def __init__(self, account_number, account_type, balance = 0):
        """
        Initializes a new Account instance.

        Parameters:
            account_number (str): The account number as a unique identifier.
            account_type (str): The type of account (e.g., savings, checking).
            balance (float, optional): The starting balance of the account. Default is 0.
        """
        self.account_number = account_number
        self.account_type = account_type
        self.balance = balance

    def deposit(self, amount):
        """
        Deposits a specified amount into the account.

        Parameters:
            amount (float): The amount to deposit.

        Returns:
            float: The updated account balance after the deposit.
        """
        self.balance += amount
        return self.balance
    
    def withdraw(self, amount):
        """
        Withdraws a specified amount from the account. Raises an error if insufficient funds.

        Parameters:
            amount (float): The amount to withdraw.

        Returns:
            float: The updated account balance after the withdrawal.

        Raises:
            ValueError: If the withdrawal amount exceeds the current balance.
        """
        if amount <= self.balance:
            self.balance -= amount
            return self.balance
        else:
            raise ValueError("Insufficient funds")