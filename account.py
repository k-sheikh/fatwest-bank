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


class CurrentAccount(Account):
    """
    Represents a Current Account with an overdraft facility.

    Inherits from Account and allows for an overdraft up to a specified limit.
    """
    def __init__(self, account_number, account_type, balance=0):
        super().__init__(account_number, account_type, balance)
        self.account_type = 'Current Account'
        self.overdraft_limit = -1000  # Overdraft facility

        def withdraw(self, amount):
            if self.balance - amount < self.overdraft_limit:
                print("Withdrawal denied. Exceeds overdraft limit.")
            else:
                super().withdraw(amount)
                print(f"Withdrawn £{amount}.")
                print(f"Current balance is £{self.balance}.")


class SavingsAccount(Account):
    """
    Represents a Savings Account that earns interest on deposits.

    Inherits from Account and adds interest to deposits.
    """
    def __init__(self, account_number, account_type, balance=0):
        super().__init__(account_number, account_type, balance)
        self.account_type = 'Savings Account'

        def deposit(self, amount):
            interest = amount * 0.05
            super().deposit(amount + interest)
            print(f"Deposited £{amount} with interest £{interest}.")
            print(f"Current balance is £{self.balance}.")