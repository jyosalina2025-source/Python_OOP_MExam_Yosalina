class BankAccount: 
    def __init__(self, account, initial_balance=100):
        self.account = account
        self.balance = initial_balance

    def get_balance(self):
        return self.balance
    
    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be greater than 0.")
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be greater than 0.")
        if amount > self.balance:
            raise ValueError("Insufficient balance.")
        self.balance -= amount
        return self.balance

account = BankAccount(100)
account.deposit(50)
account.withdraw(20)

print(account.get_balance())