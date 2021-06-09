import bank_account

class User:
    def __init__(self, username, email_address):
        self.username = username
        self.email_address = email_address
        self.accounts = [] # Create empty list of accounts
        # self.account_balance = 0
    
    def make_deposit(self, name, amount):
        # Look through list of user's accounts
        # Find account with same name as account_name
        # Deposit amount to that account
        # If account isn't found, print an error

        has_account = False # Check for nonexistent account
        for account in self.accounts:
            if account.account_name == name:
                has_account = True
                account.deposit(amount)
                print(f"Deposit of ${amount} to {name} complete")

        if has_account == False:
                print(f"Account name '{name}' not found")
    
        return self
    
    def make_withdrawal(self, name, amount):
        # Look through list of user's accounts
        # Find account with same name as account_name
        # Withdraw amount from that account
        # If account isn't found, print an error

        has_account = False # Check for nonexistent account
        for account in self.accounts:
            if account.account_name == name:
                has_account = True
                account.withdraw(amount)
                print(f"Withdrawal of ${amount} from {name} complete")

        if has_account == False:
                print(f"Account name '{name}' not found")
    
        return self

    def display_user_balance(self, name):
        # Look through list of user's accounts
        # Find account with same name as account_name
        # Get account balance
        # If account isn't found, print an error

        has_account = False # Check for nonexistent account
        for account in self.accounts:
            if account.account_name == name:
                account.display_account_info(name)
                has_account = True

        if has_account == False:
                print(f"Account name '{name}' not found")
    
        return self
    
    def transfer_money(self, transfer_from, other_user, transfer_to, amount):
        self.make_withdrawal(transfer_from, amount)
        other_user.make_deposit(transfer_to, amount)
        return self
    
    def make_account(self, int_rate=0.02, init_deposit=0, account_name="New Account"):
        # Make a new bank account with a name, interest rate, and initial deposit
        # Add account to user's accounts dictionary

        # Check to see if user has multiple accounts and create a default name if 
        if len(self.accounts) != 0:
            account_name = "New Account " + str(len(self.accounts)+1)
        self.accounts.append(bank_account.BankAccount(int_rate, init_deposit, account_name))
        return self
    

# ========== TESTS =======================================================

# Create multiple users
user1 = User("Hayden", "hayden@hayden.com")
user2 = User("Mom", "mom@mom.com")
user3 = User("Dad", "dad@dad.com")

# Create multiple accounts for a single user
user1.make_account(0.01, 1000, "Checking 2")
user1.make_account(0.01, 1000)
user1.make_account(0.01, 1000)
user2.make_account(0.05, 600, "Fun Munny")

# Deposit to specific account
user1.make_withdrawal("New Account 2", 100)
user1.display_user_balance("New Account 2")
user2.make_deposit("Fun Munny", 2000)
user2.display_user_balance("Fun Munny")

# Transfer
user1.display_user_balance("Checking 2")
user2.transfer_money("Fun Munny", user1, "Checking 2", 500)
user1.display_user_balance("Checking 2")

# user1.make_deposit(100).make_deposit(100).make_deposit(100).make_withdrawal(200).transfer_money(user3, 50).display_user_balance()
# # user1.make_deposit(100)
# # user1.make_deposit(100)
# # user1.make_withdrawal(200)
# # user1.display_user_balance()

# user2.make_deposit(100).make_deposit(50).make_withdrawal(50).make_withdrawal(10).display_user_balance()
# # user2.make_deposit(50)
# # user2.make_withdrawal(50)
# # user2.make_withdrawal(10)
# # user2.display_user_balance()

# user3.make_deposit(500).make_withdrawal(25).make_withdrawal(25).make_withdrawal(25).display_user_balance()
# user3.make_withdrawal(25)
# user3.make_withdrawal(25)
# user3.make_withdrawal(25)
# user3.display_user_balance()

# user1.transfer_money(user3, 50)
# user1.display_user_balance()
# user3.display_user_balance()