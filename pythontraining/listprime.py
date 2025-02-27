def input_numbers():
    a=int(input("enter lower range "))
    b=int(input("enter upper range "))
    return a,b

def is_prime(n):
    if n<=1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True

def print_primes(a,b):
    primenums=[]
    for i in range(a,b+1):
        if is_prime(i):
            #print(i,end=' ')
            primenums.append(i)
    #primenums=[i for i in range(a,b+1) if is_prime(i)]
    return primenums

def minmaxofprime(primenumbers):
    minimum=primenumbers[0]
    maximum=primenumbers[-1]
    return maximum,minimum

def main():
    a,b=input_numbers()
    primenumbers=print_primes(a,b)
    print("prime numbers are: ",primenumbers)
    a,b=minmaxofprime(primenumbers)
    print("max:",a,"min: ",b)
main()