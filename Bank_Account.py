# class Bank:
#     def __init__(self,Name,Account_Number):
#         self.Name=Name
#         self.Account_Number=Account_Number
#         self.Balance=1000
#     def create(self):
#         print("Account Holder Name :",self.Name)
#         print("Account Number :",self.Account_Number)
#         print("Account Balance :",self.Balance)
#         print("Account Created Scessfully :!")
#     def Deposit(self):
#         if self.Account_Number==int(input("enter the Account Number  :")):
#             new_Amount=int(input("Enter the Deposit Ammount :"))
#             self.Balance+=new_Amount
#             print("Account Balance : ",self.Balance)
#         else:
#             print("enter the Valid Account Number")
#     def Withdraw(self):
#         if self.Account_Number==int(input("enter the Account Number :")):
#             new_amount=int(input("Enter the Amount to withdraw : "))
#             if self.Balance>=new_amount:
#                 self.Balance-=new_amount
#                 print("Account Balance :",self.Balance)
#             else:
#                 print("Insufficent Balance")
#                 print("Valid ammount ")
#         else:
#             print("enter the Valid Account Number")
#     def display(self):
#         if self.Account_Number==int(input("enter the Account Number :")):
#             print("Balance Amount : ",self.Balance)
#         else:
#             print("enter the Valid Account Number")
# b1=Bank("sravan",101)
# print("1: To Create the Account ")
# print("2: Deposit the Money")
# print("3: Withdraw Money")
# print("4: Balance Amount")
# print("5: Exit")
# mark=0
# while mark==0:
#     choice=int(input("Enter the choice of 1 ,2 ,3, 4, 5 : " ))
#     if choice==1:
#         b1.create()
#     elif choice==2:
#         b1.Deposit()
#     elif choice==3:
#         b1.Withdraw()
#     elif choice==4:
#         b1.display()
#     elif choice==5:
#         mark=1
#         print("Thank you for Entering Bank !")
#     else:
#         print("enter the  valid input")




class Bank:
    new_account_num=1001
    def __init__(self,Name):
        self.Name=Name
        self.Account_Number=Bank.new_account_num
        self.Balance=1000
        Bank.new_account_num+=1
    def create(self):
        print("Account Holder Name :",self.Name)
        print("Account Number :",self.Account_Number)
        print("Account Balance :",self.Balance)
        print("Account Created Scessfully :!")
    def Deposit(self):
    
        new_Amount=int(input("Enter the Deposit Ammount :"))
        self.Balance+=new_Amount
        print("Account Balance : ",self.Balance)
        
    def Withdraw(self):
        new_amount=int(input("Enter the Amount to withdraw : "))
        if self.Balance>=new_amount:
            self.Balance-=new_amount
            print("Account Balance :",self.Balance)
        else:
            print("Insufficent Balance")
            print("Valid ammount ")
        
    def display(self):
        print("Account Holder Name : ",self.Name)
        print("Account Number : ",self.Account_Number)
        print("Balance Amount : ",self.Balance)
account={}

print("1: To Create the Account ")
print("2: Deposit the Money")
print("3: Withdraw Money")
print("4: Balance Amount")
print("5: Exit")
mark=0
while mark==0:
    choice=int(input("Enter the choice of 1 ,2 ,3, 4, 5 : " ))
    if choice==1:
        name=input("Enter the customer Name : ")
        b1=Bank(name)
        account[b1.Account_Number]=b1
        b1.create()
    elif choice==2:
        acc=int(input("Enter the Account Number :"))
        if acc in account:
            account[acc].Deposit()
        else:
            print("enter the Valid Account Number")
    elif choice==3:
        acc=int(input("Enter the Account Number :"))
        if acc in account:
            account[acc].Withdraw()
        else:
            print("enter the Valid Account Number")
    elif choice==4:
        acc=int(input("Enter the Account Number :"))
        if acc in account:
            account[acc].display()
        else:
            print("enter the Valid Account Number")
    elif choice==5:
        mark=1
        print("Thank you for Entering Bank !")
    else:
        print("enter the  valid input")
