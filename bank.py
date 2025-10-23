Name=input("enter the Name of the customer:")
Account_Number=int(input("enter the account Number:"))
Balance=1000
new_ammount=0
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
        if Account_Number==int(input("enter the Account Number")):
            new_ammount=int(input("Enter the Amount to Deposit :"))
            Balance+=new_ammount
            print("Amount creadited Sucessfully :!")
            print("The Account Balance :",Balance)
    elif choice==3:
        if Account_Number==int(input("enter the Account Number")):
            new_ammount=int(input("Enter the Amount to Withdraw  :"))
            Balance-=new_ammount
            print("Amount withdraw Sucessfully !")
            print("The Account Balance :",Balance)
    elif choice==4:
        if Account_Number==int(input("enter the Account Number")):
            print("Account Balance :",Balance)
    else:
        mark=1
