class Bank:
    def __init__(self,Name,Account_Number):
        self.Name=Name
        self.Account_Number=Account_Number
    def create(self):
        print("Account Holder Name :",self.Name)
        print("Account Number :",self.Account_number)
        self.Balance=1000
        print("Account Balance :",self.Balance)
        print("Account Created Scessfully :!")
    def Deposit(self):
        if self.Account_Number==int(input("enter the Account Number")):
            new_Amount=int(input("Enter the Deposit Ammount :"))
            self.Balance+=new_Amount
            print("Account Balance : ",self.Balance)
        else:
            print("enter the Valid Account Number")
    def Withdraw(self):
        if self.Account_Number==int(input("enter the Account Number")):
            new_amount=int(input("Enter the Amount to withdraw : "))
            if self.Balance>=new_amount:
                self.Balance-=new_amount
                print("Account Balance :",self.Balance)
            else:
                print("Insufficent Balance")
                print("Valid ammount ")
        else:
            print("enter the Valid Account Number")
    def display(self):
        if self.Account_Number==int(input("enter the Account Number")):
            print("Balance Amount : ",self.Balance)
        else:
            print("enter the Valid Account Number")
b1=Bank("sravan",101)
print("1: To Create the Account ")
print("2: Deposit the Money")
print("3: Withdraw Money")
print("4: Balance Amount")
print("5: Exit")
mark=0
while mark==0:
    choice=int(input("Enter the choice of 1 ,2 ,3, 4, 5 : " ))
    if choice==1:
        b1.create()
    elif choice==2:
        b1.Deposit()
    elif choice==3:
        b1.Withdraw()
    elif choice==4:
        b1.display()
    elif choice==5:
        mark=1
    else:
        print("enter the  valid input")