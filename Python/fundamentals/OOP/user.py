class User:
    def __init__(self, name, email_address):
        self.name = name
        self.email_address = email_address
        self.account_balance = 0
    
    def make_deposit(self, amount):
        self.account_balance += amount
    
    def make_withdrawal(self, amount):
        self.account_balance -= amount

    def display_user_balance(self):
        print(f"{self.name}, Balance: {self.account_balance}")
    
    def transfer_money(self, other_user, amount):
        self.account_balance -= amount
        other_user.make_deposit(amount)

user1 = User("Hayden", "hayden@hayden.com")
user2 = User("Mom", "mom@mom.com")
user3 = User("Dad", "dad@dad.com")

user1.make_deposit(100)
user1.make_deposit(100)
user1.make_deposit(100)
user1.make_withdrawal(200)
user1.display_user_balance()

user2.make_deposit(100)
user2.make_deposit(50)
user2.make_withdrawal(50)
user2.make_withdrawal(10)
user2.display_user_balance()

user3.make_deposit(500)
user3.make_withdrawal(25)
user3.make_withdrawal(25)
user3.make_withdrawal(25)
user3.display_user_balance()

user1.transfer_money(user3, 50)
user1.display_user_balance()
user3.display_user_balance()