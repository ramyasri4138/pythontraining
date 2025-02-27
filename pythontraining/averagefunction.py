def display(data):
    print(f"The average is {data}")
def get_input():
    n=input("enter the numbers req: ")
    recieved_num1=input("num1: ")
    recieved_num2=input("num2: ")
    recieved_num3=input("num3: ")
    recieved_num4=input("num4: ")
    return(n,recieved_num1,recieved_num2,recieved_num3,recieved_num4)
def compute_add(num1,num2,num3,num4):
    sum=(int(num1)+int(num2)+int(num3)+int(num4))
    return sum
def average(sum,n):
    average=int(sum)/int(n)
    return average
def main():
    (n,num1,num2,num3,num4)=get_input()
    sum=compute_add(num1,num2,num3,num4)
    avg=average(sum,n)
    display(avg)
    
main()