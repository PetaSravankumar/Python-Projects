mark=0
result=0
while mark<1:
    num1=int(input("enter the number1:"))
    num2=int(input("enter the number2:"))
    symbol=input("enter the sumbol:")
    if symbol=="+":
        result=num1+num2
        print("result",result)
    elif symbol=="-":
        result=num1-num2
        print("result",result)
    elif symbol=="*":
        result=num1*num2
        print("result",result)
    elif symbol=="/":
        if num2 != 0:
            result = num1 / num2
        else:
            print("Error: Cannot divide by zero!")
            continue
    elif symbol=="%":
        result=num1%num2
        print("result",result)
    else:
        print("invalid symbol")
    cont=int(input("enter the 1:Yes to continue :,2:No to quite :"))
    if cont!=1:
        mark=1