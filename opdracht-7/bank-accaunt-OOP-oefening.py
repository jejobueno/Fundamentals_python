class BankAcount:
    
    balance = 0.0
    
    def __init__(self, owner):
        self.owner = owner
    
    def deposit(self, deposited_cash):
        self.balance += deposited_cash
        print(f'Your new balance is {self.balance}€')
        
    def withdraw(self, withdrawed_cash):
        self.balance -= withdrawed_cash
        print(f'Your new balance is {self.balance}€')
        
        
account = BankAcount("Alex")
print("The owner is: ",account.owner)
print(f'The actual balance is: {account.balance}€')
account.deposit(10)
account.withdraw(3)