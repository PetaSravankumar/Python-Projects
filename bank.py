Name=input("enter the Name of the customer:")
Account_Number=int(input("enter the account Number:"))
Balance=1000
print("Sucessfull created the New Account !")
mark=0
while mark==0:
    print("1: To See the Account Holder Details")
    print("2: To Deposit the MOney")
    print("3: To Withdraw the Money")
    print("4: To Check Balance Amont")
    print("5: TO Exit")
    choice=int(input("Enter the choice 1 ,2,3,4,5"))
    if choice==1:
        print("Customer Name :",Name)
        print("Account Number :",Account_Number)
        print("Balance Amount :",Balance)
    elif choice==2:
        if Account_Number==int(input("enter the Account NUmber")):
            print("working")
            break