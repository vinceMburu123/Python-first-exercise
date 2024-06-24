class BankAccount:
    def __init__(self, account_number, balance, date_of_opening, customer_name):
        self.account_number = account_number
        self.balance = balance
        self.date_of_opening = date_of_opening
        self.customer_name = customer_name
    
    def deposit(self, amount):
        self.balance += amount
        return f"${amount} deposited. New balance is ${self.balance}."
    
    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient balance."
        else:
            self.balance -= amount
            return f"${amount} has been withdrawn. New balance is ${self.balance}."
    
    def check_balance(self):
        return f"Current balance is ${self.balance}."
    
    def customer_details(self):
        details = (f"Customer Name: {self.customer_name}\n"
                   f"Account Number: {self.account_number}\n"
                   f"Date of Account Opening: {self.date_of_opening}\n"
                   f"Balance: ${self.balance}")
        return details

bank_account1=BankAccount(account_number="1908900",balance=1000,date_of_opening="2024-1-2023",customer_name="Karen Fora")
print(bank_account1.deposit(400))  
print(bank_account1.withdraw(300))  
print(bank_account1.check_balance())  
print(bank_account1.customer_details()) 
