class BankAccount:
    def __init__(self, account_number, account_holder, balance=0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount}. Current balance: ${self.balance}")
        else:
            print("Invalid deposit amount. Please enter a positive value.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount}. Current balance: ${self.balance}")
        else:
            print("Insufficient funds or invalid withdrawal amount.")

    def get_balance(self):
        return self.balance


def create_account(accounts, account_number, account_holder):
    if account_number not in accounts:
        new_account = BankAccount(account_number, account_holder)
        accounts[account_number] = new_account
        print("Account created successfully.")
    else:
        print("Account number already exists. Please try again.")


def main():
    accounts = {}

    while True:
        print("\nBanking Management System")
        print("1. Create Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Check Balance")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            account_number = input("Enter the account number: ")
            account_holder = input("Enter the account holder's name: ")
            create_account(accounts, account_number, account_holder)

        elif choice == "2":
            account_number = input("Enter the account number: ")
            amount = float(input("Enter the deposit amount: "))
            if account_number in accounts:
                accounts[account_number].deposit(amount)
            else:
                print("Account not found. Please check the account number.")

        elif choice == "3":
            account_number = input("Enter the account number: ")
            amount = float(input("Enter the withdrawal amount: "))
            if account_number in accounts:
                accounts[account_number].withdraw(amount)
            else:
                print("Account not found. Please check the account number.")

        elif choice == "4":
            account_number = input("Enter the account number: ")
            if account_number in accounts:
                balance = accounts[account_number].get_balance()
                print(f"Account balance: ${balance}")
            else:
                print("Account not found. Please check the account number.")

        elif choice == "5":
            print("Exiting the system.")
            break

        else:
            print("Invalid choice. Please select a valid option.")


if __name__ == "__main__":
    main()
