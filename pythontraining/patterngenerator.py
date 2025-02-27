n=int(input("enter n: "))
option=input("want in reverse pattern? yes or no: ")
for i in range (1,n+1):
    if option=='no':
        print("*"*i)
    else:
        print("*"* (n-i+1))