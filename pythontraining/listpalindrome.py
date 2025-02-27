def ispalindrome(value):
    value=str(value).replace(" ","").lower()
    valuelist=list(value)
    revlist=valuelist[::-1]
    return valuelist==revlist
def main():
    while True:
        value=input("enter a number or string or exit: ")
        if value == 'exit':
            print("exiting out of the loop")
            break
        elif ispalindrome(value):
            print(f"{value} is palindrome")
        else:
            print(f"{value} is not a palindrome")
main()