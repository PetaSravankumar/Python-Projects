import random
n=random.randint(0,100)
count=0
def no_of_chances():
    if count==0:
        print("you have 2 chances !")
    elif count==1:
        print("you have 1 chance !")
        for i in range(2,12):
            if n%i==0:
                
while count<=2:
    guss=int(input("guss the number :"))
    if guss==n:
        print("Conguralations")
        print("You have gussed it correct ",n)
    elif n>guss :
        print("The guess a number is greater ",guss)
        no_of_chances()
    elif n<guss:
        print("The guess a number is less than ",guss)
        no_of_chances()
    count+=1
if count==3 and guss!=n:
    print("you have Loss try again")
    print("Number is ",n)
