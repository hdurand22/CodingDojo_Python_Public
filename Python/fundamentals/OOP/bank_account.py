class BankAccount:
    
    # bank_name = "First National Dojo"
    # all_accounts = []
    def __init__(self, int_rate, balance, account_name): 
        self.int_rate = int_rate
        self.balance = balance
        self.account_name = account_name
        # BankAccount.all_accounts.append(self)
    
    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if BankAccount.can_withdraw(self.balance, amount):
            self.balance -= amount
        else:
            print("Insufficient Funds")
        return self

    def display_account_info(self, name):
        print(f"{name}'s account balance: {self.balance}")
        return self

    def yield_interest(self):
        self.balance += (self.balance*self.int_rate)
        return self
    
    # @classmethod
    # def all_balances(cls):
    #     print(cls.all_accounts)

    @staticmethod
    def can_withdraw(balance, amount):
        if (balance - amount) < 0:
            return False
        else:
            return True

# account1 = BankAccount(0.02)
# account2 = BankAccount(0.03, 500)

# account1.deposit(200).deposit(200).deposit(50).withdraw(200).yield_interest().display_account_info()
# account2.deposit(200).deposit(200).withdraw(50).withdraw(200).withdraw(50).withdraw(10).yield_interest().display_account_info()

# BankAccount.all_balances()