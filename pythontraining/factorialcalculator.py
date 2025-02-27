def factorialcalculator(number):
    if number<0:
        raise ValueError("factorial cannot be found for negative numbers")
    factorial=1
    for i in range(1,number+1):
        factorial*=i
    return factorial
def main():
    while(True):
        num=input("Enter a number or exit ")
        if num.lower()=='exit':
            print("exiting out of loop")
            break
        try:
            number=int(num)
            result=factorialcalculator(number)
            print(f"The factorial of {number}", result)
        except ValueError as ex:
            print(ex)
main()