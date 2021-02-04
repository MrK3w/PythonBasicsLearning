class Account:

    def __init__(self,owner,balance) -> None:
        self.owner = owner
        self.balance = balance
    
    def withdraw(self,amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"Owner {self.owner} withdrawed {self.balance}$.")
        else:
            print(f"Sorry owner {self.owner} cannot withdraw {amount}$ because he is missing {amount-self.balance}$.")

    def deposit(self,amount):
        self.balance += amount
        print(f"Owner {self.owner} deposited {amount}$.")

    def __str__(self) -> str:
        return f"Account owner:\t{self.owner}\nAccount balance: {self.balance}"

john = Account('John',300)
print(john)
john.deposit(100)
print(john)
john.withdraw(300)
print(john)
john.withdraw(200)
print(john)

