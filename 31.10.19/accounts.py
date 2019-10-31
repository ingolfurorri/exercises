class Account:
    def __init__(self, balance):
        self.balance = float(balance)

    def __str__(self):
        return "Balance: {:.2f}".format(self.balance)

class SavingsAccount(Account):
    def __init__(self, balance):
        Account.__init__(self, balance)

    def update_balance(self):
        self.balance = self.balance*1.05 + self.balance*0.10

class DebitAccount(Account):
    def __init__(self, balance):
        Account.__init__(self, balance)

    def update_balance(self):
        self.balance = self.balance*1.02

s1 = SavingsAccount(1000)
d1 = DebitAccount(1000)
s2 = SavingsAccount(2000)
d2 = DebitAccount(4000)