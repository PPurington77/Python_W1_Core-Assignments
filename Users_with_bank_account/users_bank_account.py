class BankAccount:
    accounts = []

    def __init__(self, balance = 0, int_rate = .01):
        self.balance = balance
        self.int_rate = int_rate
        BankAccount.accounts.append(self)

    def deposit(self, amount):
        self.balance += amount
        return self 

    def see_balance(self):
        print(f"Your balance is {self.balance}")

    def withdraw(self, amount):
        if (self.balance - amount) < 0:
            print("Sorry you don't have the funds necessary to make this withdrawel")
            return False
        else:
            self.balance -= amount
            return self

    def account_info (self):
        print("*" * 80)
        print(f"Your account balance is {self.balance}")
        print(f"Your account interest rate is {self.int_rate}")
        return self

    def yield_interest(self):
        if self.balance > 0:
            self.balance = self.balance + (self.balance * self.int_rate)
            return self

    @classmethod
    def print_all_accounts(cls):
        for account in cls.accounts:
            account.account_info()

class User:

    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(balance = 0, int_rate = .02)

    def deposit_money(self, amount):
        self.account.deposit(amount)
        return self

    def withdraw_money(self, amount):
        self.account.withdraw(amount)
        return self 

    def display_user_balance(self):
        self.account.see_balance()

user_a = User("Patrick", "papurington@gmail.com")
user_a.deposit_money(1500).withdraw_money(500)
user_a.display_user_balance()
