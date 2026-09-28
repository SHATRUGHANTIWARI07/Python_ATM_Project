class ATM:

    def __init__(self, name, pin, balance):
        self.name = name
        self.pin = pin
        self.balance = balance

    def check_balance(self):
        print("Current Balance:", self.balance)

    def deposit(self):
        amount = float(input("Enter deposit amount: "))

        if amount > 0:
            self.balance += amount
            print("Amount deposited successfully.")
        else:
            print("Invalid amount.")

    def withdraw(self):
        amount = float(input("Enter withdrawal amount: "))

        if amount <= 0:
            print("Invalid amount.")

        elif amount > self.balance:
            print("Insufficient balance.")

        else:
            self.balance -= amount
            print("Please collect your cash.")

    def menu(self):

        while True:

            print("\n===== ATM MENU =====")
            print("1. Check Balance")
            print("2. Deposit")
            print("3. Withdraw")
            print("4. Exit")

            choice = input("Enter choice: ")

            if choice == "1":
                self.check_balance()

            elif choice == "2":
                self.deposit()

            elif choice == "3":
                self.withdraw()

            elif choice == "4":
                print("Thank you for using ATM.")
                break

            else:
                print("Invalid choice.")


# User details
name = input("Enter your name: ")
pin = input("Set your PIN: ")
balance = float(input("Enter opening balance: "))

# Object creation
user = ATM(name, pin, balance)

# PIN verification
entered_pin = input("Enter your PIN: ")

if entered_pin == user.pin:
    print(f"\nWelcome, {user.name}!")
    user.menu()
else:
    print("Incorrect PIN.")