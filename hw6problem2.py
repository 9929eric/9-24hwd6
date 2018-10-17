class BankAccount:

    def __init__(self, balance):
        self.balance = balance

    def deposit(self, deposit):
      if deposit > 0:
        self.balance += deposit
      else:
        print("False")

    def withdrawal(self, withdrawal):
      if withdrawal > 0:
        self.balance -= withdrawal
      else:
        print("False")

    def accumulate_interest(self, accumulate_interest):
         self.balance *= accumulate_interest



basic_account = BankAccount(0)
basic_account.deposit(600)

print("Basic account has ${}".format(basic_account.balance))


basic_account.withdrawal(17)

print("Basic account has ${}".format(basic_account.balance))

basic_account.accumulate_interest(1.02)

print("Basic account has ${}".format(basic_account.balance))
print(" ")

class ChildrensAccount:

    def __init__(self, balance):
        self.balance = balance

    def deposit(self, deposit):
        self.balance += deposit

    def withdrawal(self, withdrawal):
        self.balance -= withdrawal

    def accumulate_interest(self, accumulate_interest):
         self.balance += accumulate_interest

childs_account = ChildrensAccount(0)
childs_account.deposit(34)

print("Child's account has ${}".format(childs_account.balance))

childs_account.withdrawal(17)

print("Child's account has ${}".format(childs_account.balance))

childs_account.accumulate_interest(10)

print("Child's account has ${}".format(childs_account.balance))

print(" ")

class OverdraftAccount(BankAccount):

    def __init__(self, balance):
        self.balance = balance


    def withdrawal(self, withdrawal):
      if withdrawal > self.balance:
        self.balance -= 40
      elif withdrawal > 0:
        self.balance-=withdrawal
      else:
        print("False")

    def accumulate_interest(self, accumulate_interest):
      if self.balance > 0:
         self.balance *= accumulate_interest
      else:
         self.balance = self.balance



overdraft_account = OverdraftAccount(0)
overdraft_account.deposit(12)

print("Overdraft account has ${}".format(overdraft_account.balance))

overdraft_account.withdrawal(17)

print("Overdraft account has ${}".format(overdraft_account.balance))

overdraft_account.accumulate_interest(1.02)

print("Overdraft account has ${}".format(overdraft_account.balance))
