class BankAccount:
    def __init__(self, full_name, account_number, balance):
        self.name = full_name
        self.account = account_number
        self.balance = balance

# Instantiate the class outside of the class definition
customer = BankAccount("Acs 1111", 12345, 50)

# print(customer.balance)

def deposit(amount):
    deposited = float(input("Amount Deposit: $ "))
    balance = amount
    new_balance = deposited + balance
    print(f"Amount Deposited: ${deposited} New Balance: ${new_balance}")

deposit(0)