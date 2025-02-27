def findsum():
    list1=[ ]
    n=int(input("enter the length of the list : "))
    totalsum=0
    while(n):
        a=int(input("enter the value: "))
        list1.append(a)
        n-=1
        totalsum+=a
    print("the list is",list1)
    print("the sum is: ",totalsum)
    return 0

def main():
    findsum()
main()


