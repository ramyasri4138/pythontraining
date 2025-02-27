def ispalindrome(value):
    value=str(value).replace(" ","").lower()
    return value==value[::-1]
def main():
    while True:
        value=input("enter a number or string or exit")
        if value == 'exit':
            print("exiting out of the loop")
            break
        if ispalindrome(value):
            print(f"{value} is palindrome")
        else:
            print(f"{value} is not a palindrome")
main()