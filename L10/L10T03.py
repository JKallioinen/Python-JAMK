class Account:
    def __init__(saldo):
        saldo.balance = 2000
        print("Bank account created.")
        print("Bank account balance: ", saldo.balance)
 
    def add(money):
        amount = int(input("How many euros will be added?: "))
        money.balance += amount
        print("Bank account balance:", money.balance,"€")
 
    def withdraw(money):
        amount = int(input("Enter amount to be Withdrawn: "))
        if money.balance>=amount:
            money.balance-=amount
            print("You Withdrew:", amount,"€")
            print("Bank account balance: ", money.balance,"€")
        else:
            print(f"Sorry, you have only {money.balance}€, the withdraw cannot be done.  ")

s = Account()
s.add()
s.withdraw()
s.withdraw()
