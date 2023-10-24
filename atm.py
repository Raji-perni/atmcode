class Account:
    def __init__(self, user_id, pin, balance=0):
        self.user_id = user_id
        self.pin = pin
        self.balance = balance
        self.transactions = []

    def deposit(self, amount):
        self.balance += amount
        self.transactions.append(f"Deposited: {amount}")
        return f"Deposited: {amount}"

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            self.transactions.append(f"Withdrew: {amount}")
            return f"Withdrew: {amount}"
        else:
            return "Insufficient balance"

    def transfer(self, amount, recipient):
        if amount <= self.balance:
            self.balance -= amount
            recipient.balance += amount
            self.transactions.append(f"Transferred: {amount} to {recipient.user_id}")
            return f"Transferred: {amount} to {recipient.user_id}"
        else:
            return "Insufficient balance"

    def get_transaction_history(self):
        return self.transactions


class ATM:
    def __init__(self):
        self.accounts = {}

    def create_account(self, user_id, pin):
        if user_id not in self.accounts:
            account = Account(user_id, pin)
            self.accounts[user_id] = account
            return account
        else:
            return "User already exists. Please choose a different user ID."

    def authenticate_user(self, user_id, pin):
        if user_id in self.accounts and self.accounts[user_id].pin == pin:
            return self.accounts[user_id]
        else:
            return None


# Example usage
atm = ATM()

# Creating an account
user_id = input("Enter your user ID: ")
pin = input("Enter your PIN: ")
account = atm.create_account(user_id, pin)
if isinstance(account, Account):
    print("Account created successfully.")
else:
    print(account)

# Authenticating the user
user_id = input("Enter your user ID: ")
pin = input("Enter your PIN: ")
authenticated_user = atm.authenticate_user(user_id, pin)

if authenticated_user:
    print("Authentication successful. Welcome to the ATM system!")
    while True:
        print("Operations:")
        print("1. Transactions History")
        print("2. Withdraw")
        print("3. Deposit")
        print("4. Transfer")
        print("5. Quit")
        choice = input("Enter your choice: ")

        if choice == "1":
            print(authenticated_user.get_transaction_history())
        elif choice == "2":
            amount = float(input("Enter withdrawal amount: "))
            print(authenticated_user.withdraw(amount))
        elif choice == "3":
            amount = float(input("Enter deposit amount: "))
            print(authenticated_user.deposit(amount))
        elif choice == "4":
            recipient_id = input("Enter recipient's user ID: ")
            recipient = atm.accounts.get(recipient_id)
            if recipient:
                amount = float(input("Enter transfer amount: "))
                print(authenticated_user.transfer(amount, recipient))
            else:
                print("Recipient not found.")
        elif choice == "5":
            print("Thank you for using the ATM system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
else:
    print("Authentication failed. Invalid user ID or PIN.")
