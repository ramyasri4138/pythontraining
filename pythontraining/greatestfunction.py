def get_input():
    a=input("enter num1: ")
    b=input("enter num2: ")
    c=input("enter num3: ")
    return a,b,c
def greatest(a,b,c):
    if (a>b) and (a>c):
        print("a")
        return a
    elif (b>a) and (b>c):
        print("b")
        return b#print(b)
    else:
        print("The greatest variable is c")
        return c
def display(data):
    print(f"greatest number is {data}")

def main():
    num1,num2,num3=get_input()
    great=greatest(num1,num2,num3)
    display(great)
    #print(greatest(a,b,c))
    #print(great)
main()

#it helps to disassemble the code
'''
def get_input( ):
    a=int(input("enter num1"))
    b=int(input("enter num2"))
    c=int(input("enter num3"))
    great=a
    if great<b:
        great=b
    if great<c:
        great=c
    return great
def display(data):
    print(data)
def main():
    great=get_input( )
    display(great)
main()
'''
