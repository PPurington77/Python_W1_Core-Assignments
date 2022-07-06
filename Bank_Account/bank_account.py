class BankAccount:

    def __init__(self, balance = 0, int_rate = .01):
        self.balance = balance
        self.int_rate = int_rate

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

user_a = BankAccount(1000, .1)
user_b = BankAccount(2000)

user_a.deposit(100).deposit(200).deposit(300).withdraw(28).yield_interest().account_info()
user_b.deposit(8350).deposit(10239).withdraw(201).withdraw(234).withdraw(2434).withdraw(124).yield_interest().account_info()
