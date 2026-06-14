class BankAccount:

    def __init__(self, ownerName, balance):
        self.ownerName = ownerName
        self.balance = balance
    
    def deposit(self, amount):
        print(f"Deposited: {amount}")
        self.balance += amount

    def withdraw(self, amount):
        print(f"Withdrwa: {amount}")
        self.balance -= amount
    
    def show_balance(self):
        print(f"Total Balance: {self.balance}")


acc = BankAccount("Zarak khan", 1000)
acc.deposit(522)
acc.withdraw(100)
acc.show_balance()