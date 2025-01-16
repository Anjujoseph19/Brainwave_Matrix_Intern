#Task 1: Create a fully functional ATM interface using Python.

class ATM:
    def __init__(self, balance=0):
        self.balance = balance

    def check_balance(self):
        return f"Your current balance is: ${self.balance:.2f}"

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return f"${amount:.2f} deposited successfully. {self.check_balance()}"
        else:
            return "Deposit amount must be positive."

    def withdraw(self, amount):
        if amount <= 0:
            return "Withdrawal amount must be positive."
        elif amount > self.balance:
            return "Insufficient balance for this transaction."
        else:
            self.balance -= amount
            return f"${amount:.2f} withdrawn successfully. {self.check_balance()}"

    def exit(self):
        return "Thank you for using our ATM. Have a great day!"

def atm_interface():
    print("Welcome to the ATM Interface")
    user_atm = ATM(balance=1000)  # Default balance set to $1000

    while True:
        print("\nPlease choose an option:")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")

        try:
            choice = int(input("Enter your choice (1-4): "))
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 4.")
            continue

        if choice == 1:
            print(user_atm.check_balance())

        elif choice == 2:
            try:
                amount = float(input("Enter the amount to deposit: "))
                print(user_atm.deposit(amount))
            except ValueError:
                print("Invalid input. Please enter a valid amount.")

        elif choice == 3:
            try:
                amount = float(input("Enter the amount to withdraw: "))
                print(user_atm.withdraw(amount))
            except ValueError:
                print("Invalid input. Please enter a valid amount.")

        elif choice == 4:
            print(user_atm.exit())
            break

        else:
            print("Invalid choice. Please choose a number between 1 and 4.")

if __name__ == "__main__":
    atm_interface()
