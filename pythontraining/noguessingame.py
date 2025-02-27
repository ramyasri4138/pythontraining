import random
num=random.randint(1,101)
numguess = None
while numguess!=num:
    numguess=int(input("enter the number you are guessing: "))
    if numguess>num:
        print("too high")
    elif numguess<num:
        print("too low")
    elif numguess==num:
        print("correct guess")
        
