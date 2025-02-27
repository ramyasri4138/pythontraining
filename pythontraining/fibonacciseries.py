def fibonacci(n):
    a=0
    b=1
    print(a,b,end=" ")
    for i in range(n-2):
        a,b = b,a+b
        print(b,end=" ")
    return 0
    
def main():
    n=int(input("how many numbers are required: "))
    fibonacci(n)
main()



def fibonacci(n: int) -> list:
    """
    Compute Fibonacci sequence up to n terms.
    
    Args:
    n (int): The number of terms in the Fibonacci sequence.
    
    Returns:
    list: A list containing the Fibonacci sequence up to n terms.
    """
    a, b = 0, 1
    sequence = [a, b]  # Initialize the sequence list

    for _ in range(n-2):
        a, b = b, a + b
        sequence.append(b)

    return sequence

def main() -> None:
    n = int(input("How many numbers are required: "))
    sequence = fibonacci(n)
    print(" ".join(map(str, sequence)))

main()
