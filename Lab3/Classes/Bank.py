class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
    
    def __str__(self):
        return f"Owner: {self.owner}\nbalance: {self.balance}"
    
    def deposit(self, amount):
        self.balance += amount
        return "deposit"
    
    def withdraw(self, amount):
        if (amount <= self.balance):
            self.balance -= amount
            return "withdraw"
        else:
            return "denied"
        
    
acc1 = Account("Aibek", 100)

print(acc1)

print(acc1.deposit(50))
print(acc1.withdraw(20))
print(acc1.balance)
print(acc1.withdraw(150))
