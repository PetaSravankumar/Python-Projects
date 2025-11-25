import random
n=random.randint(1,3)
def fun():
    if n==1:
        print("computer choose :" ,"Rock")
        return "Rock"
    elif n==2:
        print("computer choose :" ,"Scissor")
        return "Scissor"
    else:
        print("computer choose :" ,"Paper")
        return "Paper"
num=int(input("Enter the number to Choose the 1: Rock , 2: Scissor ,3 : Paper"))
choice=""
if num==1:
    choice="Rock"
if "Rock"==fun():
    print("It is draw ")
elif "Scissor"==fun():
    print("")