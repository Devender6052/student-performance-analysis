class account:
    Balance = 10000
    Account_no= 1020234567
    def __init__(self):
        print("account created successfully")
        print("Your account no. is :", self.Account_no)
    def debit(self,Amount):
        self.Balance-=Amount
        print("Amount Debited succesfully. Your remaining balance is :",self.Balance)
    def credit(self,Amount):
        self.Balance+= Amount
        print("Amount Credited succesfully. Now your current balance is :",self.Balance)
    def show_Balance(self):
        print("Your balance is :",self.Balance)

account1=account()
account1.debit(5000)
account1.credit(342)
account1.show_Balance()
