class Account:
    def __init__(self, balance, account_no):
        self.balance = balance
        self.account_no = account_no

    def display_account_info(self):
        print(f"Account Number: {self.account_no}, Balance: {self.balance}")
    def Debit(self,amount):
        self.balance -= amount
        print(f"Debited {amount}. New Balance: {self.balance}")
         
    def Credit(self,amount):
            self.balance += amount
            print(f"Credited {amount}. New Balance: {self.balance}")
             
    def get_balance(self):
        return self.balance
    
Account1 = Account(1000, "123456789")
Account1.Debit(1000)
Account1.Credit(500)
Account1.display_account_info()