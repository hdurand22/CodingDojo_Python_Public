class User:
    def __init__(self, name, email_address):
        self.name = name
        self.email_address = email_address
        self.account_balance = 0
    
    def make_deposit(self, amount):
        self.account_balance += amount
        return self
    
    def make_withdrawal(self, amount):
        self.account_balance -= amount
        return self

    def display_user_balance(self):
        print(f"{self.name}, Balance: {self.account_balance}")
        return self
    
    def transfer_money(self, other_user, amount):
        self.account_balance -= amount
        other_user.make_deposit(amount)
        return self

user1 = User("Hayden", "hayden@hayden.com")
user2 = User("Mom", "mom@mom.com")
user3 = User("Dad", "dad@dad.com")

user1.make_deposit(100).make_deposit(100).make_deposit(100).make_withdrawal(200).transfer_money(user3, 50).display_user_balance()
# user1.make_deposit(100)
# user1.make_deposit(100)
# user1.make_withdrawal(200)
# user1.display_user_balance()

user2.make_deposit(100).make_deposit(50).make_withdrawal(50).make_withdrawal(10).display_user_balance()
# user2.make_deposit(50)
# user2.make_withdrawal(50)
# user2.make_withdrawal(10)
# user2.display_user_balance()

user3.make_deposit(500).make_withdrawal(25).make_withdrawal(25).make_withdrawal(25).display_user_balance()
# user3.make_withdrawal(25)
# user3.make_withdrawal(25)
# user3.make_withdrawal(25)
# user3.display_user_balance()

# user1.transfer_money(user3, 50)
# user1.display_user_balance()
# user3.display_user_balance()