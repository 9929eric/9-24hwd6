class BankAccount:

    def __init__(self, balance):
        self.balance = balance

    def deposit(self, deposit):
        self.balance += deposit

    def withdrawal(self, withdrawal):
        self.balance -= withdrawal

    def accumulate_interest(self, accumulate_interest):
         self.balance *= accumulate_interest



basic_account = BankAccount(0)
basic_account.deposit(600)

print("Basic account has ${}".format(basic_account.balance))

basic_account.withdrawal(17)

print("Basic account has ${}".format(basic_account.balance))

basic_account.accumulate_interest(1.02)

print("Basic account has ${}".format(basic_account.balance))
