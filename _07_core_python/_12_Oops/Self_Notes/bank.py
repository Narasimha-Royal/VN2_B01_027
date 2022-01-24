class Bank:
    balance = 100000

    def __init__(self, amount):
        self.amount = amount

    def deposit(self):
        print("After Depositing Total Amount of Money in Account :-- ", Bank.balance + self.amount)

    def withdraw(self):
        if self.amount < Bank.balance:
            print("After Withdraw Total Amount of Money in Account :--", Bank.balance - self.amount)
        else:
            print("Insufficient Amount in Account \n Please Enter valid Amount")


bal = Bank(5000)
bal.deposit()
bal = Bank(2000)
bal.withdraw()
bal = Bank(150000)
bal.withdraw()
