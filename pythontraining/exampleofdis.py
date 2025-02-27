import dis

def display(data):
    print(f"The product of two numbers {data}")
    
def input_values():
    a=input("enter the value a: ")
    b=input("enter the value b: ")
    return(a,b)
    
def multiply(a,b):
    c=int(a)*int(b)
    return c
def main():
    (a,b)=input_values()
    data=multiply(a,b)
    display(data)
    dis.dis(multiply)
main()