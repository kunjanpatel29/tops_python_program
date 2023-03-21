"""
Creating Banking Application :
- In This Application I Perform OpenAccount, Deposit and Withdraw Amount
  and Check Balance Functionality.
"""

# Created Class
class BankApp:

    # Function for Open Bank Account
    def openAccount(self,acno,cname,balance):
        self.acno = acno
        self.cname = cname
        self.balance = balance
        print("Hello ",self.cname," , Your Account Number ",self.acno," Is Opened With ",self.balance," Rs.")

    # Function for Deposit Money into Account
    def deposit(self,amount):
        self.balance = self.balance + amount

    # Function for Withdraw Money from Account
    def withdraw(self,amount):
        if amount <= self.balance:
            self.balance = self.balance - amount
        else:
            self.needs = amount - self.balance
            print("Sorry, You Need Another ",self.needs," RS. To Withdraw")
            
    # Function for Check Balance in Account
    def checkBalance(self):
        print("Current Balance : ",self.balance) 


b1 = BankApp() # Object is Created
# Taken Input from the user
acno = int(input("Enter a Account Number: "))
cname = input("Enter Customer Name: ")
balance = int(input("Enter a Initial Balance: "))

b1.openAccount(acno,cname,balance)  # Called Method
    
while True:

    print("*"*50)
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")
    print("*"*50)
    
    choice = int(input("Enter Your Choice: "))
    print("*"*50)

    if choice == 1:
        amount = int(input("Enter Deposit Amount: "))
        b1.deposit(amount)
        print("*"*50)
    elif choice == 2:
        amount = int(input("Enter a Withdrawal Amount: "))
        b1.withdraw(amount)
        print("*"*50)
    elif choice == 3:
        b1.checkBalance()
        print("*"*50)
    else:
        print("Good Bye, Thank you For Using Our Services.")
        break
