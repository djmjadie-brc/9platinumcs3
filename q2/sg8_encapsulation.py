class BankAccount:  #below are the properties and methods of the class
    def __init__(self, account_number: int, balance: float):
        self.__account_number = account_number
        self.__balance = balance

    def set_account_number(self, account_number: int):
        self.__account_number = account_number

    def set_balance(self, update_balance: float):
        if update_balance < 0:
            print("The balance must not be a negative number")
            return
        
        self.__balance = update_balance

    def get_account_number(self):
        return self.__account_number

    def get_balance(self):
        return self.__balance
    
    
a1 = BankAccount(12345, 1000.00)  #object created for the class BankAccount

print("Account 1")
print("Account Number:", a1.get_account_number())
print("Balance:", f"{a1.get_balance():.2f}")
print(" ")

print("Update balance to -100.00")
result = a1.set_balance(-100.00)

print("Account Number:", a1.get_account_number())
print("Balance:", f"{a1.get_balance():.2f}")
