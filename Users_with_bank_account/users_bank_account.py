class BankAccount:
    accounts = []

    def __init__(self, balance = 0, int_rate = .01):
        self.balance = balance
        self.int_rate = int_rate
        BankAccount.accounts.append(self)

    def deposit(self, amount):
        self.balance += amount
        return self 

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


user_a = User("Patrick", "papurington@gmail.com")
user_a.account.deposit(500)
print(user_a.account.balance)
