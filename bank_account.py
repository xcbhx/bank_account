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
        print(f'Amount Deposited: ${amount} New Balance: ${self.balance}')

    def withdraw(self, amount):
        """Withdraw a specified amount from the balance,w ith overdraft fees."""
        if amount > self.balance:
            # Apply the overdraft fee
            self.balance -= (amount + 10)
            print(f'Insufficient funds. You were charged an overdrafted fee of $10.\n Amount Withdrawn: ${amount} New Balance: ${self.balance}')
        else: 
            # Subtract the amount from the balance if sufficient funds
            self.balance -= amount
            print(f'Amount Withdrawn: ${amount} New Balance: ${self.balance}')
    
    def get_balance(self):
        """Print user-friendly message with the account balance and then return the current balance"""
        print(f'Here is your account information. Account Balance:${self.balance}')
        return self.balance
    
    def add_interest(self):
        """Add annual interest to users balance."""
        interest = self.balance *  0.00083
        self.balance += interest
        print(f'New balance with interest: ${self.balance}')

    def print_statement(self):
        """Display message with the account name, account number, and balance"""
        print(f'{self.name}\nAccount No.:{self.account}\nBalance: ${self.balance}')



# Instantiate the class outside of the class definition
customer = BankAccount('Acs 1111', 20)

print(f'Initial Balance: ${customer.balance}')

# Call the deposit method 
customer.deposit(50) 
customer.withdraw(10)
customer.add_interest()
customer.print_statement()



balance = customer.get_balance()
print(f'The current balance is: ${balance}')
