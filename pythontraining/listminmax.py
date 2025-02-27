def get_input():
    a=list(map(int,input("enter the elements: ").split()))
    return a
def findminmax(a):
    #numbers=[int(input(f"enter numbers {i+1}: "))for i in range(3)]
    minimum=a[0]
    maximum=a[0]
    for num in a:    #for i in range(3)
        if num<=minimum:
            minimum=num
        if num>=maximum:
            maximum=num
    return minimum,maximum   

def main():
    a=get_input()
    c,d=findminmax(a)
    print("max:",c,"min: ",d)
main()