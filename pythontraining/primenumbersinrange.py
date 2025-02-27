def input_numbers():
    a=int(input("enter lower range"))
    b=int(input("enter upper range"))
    return a,b
def is_prime(n):
    if n<=1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True
def print_primes(a,b):
    for i in range(a,b+1):
        if is_prime(i):
            print(i,end=' ')
a,b=input_numbers()
print_primes(a,b)
