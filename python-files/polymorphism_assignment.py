
class Transaction:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def display_balance(self):
        print(f"Account Number: {self.account_number}, Balance: UGX {self.balance:.2f}")

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited: UGX {amount:.2f}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawn: UGX {amount:.2f}")
        else:
            print("Invalid withdrawal amount.")

    def transfer(self, target_account, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            target_account.balance += amount
            print(f"Transferred: UGX {amount:.2f} to Account {target_account.account_number}")
        else:
            print("Invalid transfer amount.")
class Deposit(Transaction):
    def deposit(self, amount):
        super().deposit(amount)

class Withdraw(Transaction):
    def withdraw(self, amount):
        super().withdraw(amount)

class Transfer(Transaction):
    def transfer(self, target_account, amount):
        super().transfer(target_account, amount)

account1 = Transaction("123456", 1000.0)
account2 = Transaction("654321", 500.0)

def main():
    print("choose an option")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Transfer")
    option = int(input("Enter your choice: "))

    if option == 1:
        amount = float(input("Enter the amount to deposit: "))
        account1.deposit(amount)
    elif option == 2:
        amount = float(input("Enter the amount to withdraw: "))
        account1.withdraw(amount)
    elif option == 3:
        amount = float(input("Enter the amount to transfer: "))
        account1.transfer(account2, amount)
    else:
        print("Invalid option selected.")
    account1.display_balance()
main()