def arraycreation(n):
    a=[]
    for i in range(n):
        b=input("enter the value: ")
        a.append(b)
    return a
def main():
    n=int(input("enter the number of elements required: "))
    result=arraycreation(n)
    print(" ".join(map(str, result)))
main()