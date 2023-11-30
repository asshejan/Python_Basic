class Bank:
    def __init__(self, balance):
        self.balance = balance
        self.minimum = 100
        self.maximum = 100000
    
    def get_balance(self):
        return self.balance
    
    def deposit(self, amount):
        if(amount> 0):
            self.balance += amount

    def withdraw(self, amount):
        if(amount > self.maximum):
            return f'Not allowed'
        elif(amount < self.minimum):
            return f'insufficient withdraw'
        else:
            self.balance -= amount
            return f'current balance {self.balance}'
        

brac = Bank(1500)
brac.withdraw(100)
print(brac.withdraw(20))
