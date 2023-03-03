class BankAccount:
    def __init__(self,name,balance):
        self.name = name
        self.balance = balance

    def deposit(self,amount):
        if amount > 0:
            self.balance += amount
            print(f"${amount} is deposited in {self.name}'s bank account")
        else:
            print("Insufficient Balance")
        self.show_balance()

    def withdraw(self,amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f"${amount} is withdrawn from {self.name}'s bank account")

        else:
            print ("Insufficient Balance")
        self.show_balance()

    def show_balance(self):
        print (f"Balance is ${self.balance}")

new_bank_account = BankAccount(name="Ankush",balance=0)
new_bank_account.deposit(100000)
new_bank_account.withdraw(20000)

