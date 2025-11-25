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
elif num==2:
    choice="Scissor"
elif num==3:
    choice="Paper"
if choice=="Rock":
    if "Rock"==fun():
        print("You choose :Rock")
        print("It is draw ")
    elif "Scissor"==fun():
        print("You choose :Rock")
        print("You win")
    else:
        print("You choose :Rock")
        print("You loss")
elif choice=="Scissor":
    if "Rock"==fun():
        print("You choose :Scissor")
        print("It is Loss ")
    elif "Scissor"==fun():
        print("You choose : SCissor")
        print("You Draw")
    else:
        print("You choose : Scissor ")
        print("You Win")
else:
    if "Rock"==fun():
        print("You choose :Paper")
        print("It is Win")
    elif "Scissor"==fun():
        print("You choose :Paper")
        print("You loss")
    else:
        print("You choose :Paper")
        print("You Draw")
