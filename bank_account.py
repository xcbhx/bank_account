# Import the random library
import random

class BankAccount:
    def __init__(self, full_name, account_number, balance=0):
        self.name = full_name
        self.account = random.randint(10000000, 99999999)
        self.balance = balance

    def deposit(self, amount):
        """Add a specified amount to the balance""" #Docstring
        # Update the balance by adding the amount
        self.balance += amount
        print(f"Amount Deposited: ${amount} New Balance: ${self.balance}")




# Instantiate the class outside of the class definition
customer = BankAccount('Acs 1111', 20)

print(f'Initial Balance: ${customer.balance}')

# Call the deposit method the instance
customer.deposit(50) 
    