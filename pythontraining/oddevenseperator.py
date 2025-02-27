def oddevenseperators(nums):
    odd=[]
    even=[]
    for num in nums:
        if num%2 == 0:
            even.append(num)
        else:
            odd.append(num)
    return odd,even
def main():
    user_input=input("enter the list of numbers")
    nums=list(map(int,user_input.split()))
    oddnumbers,evennumbers= oddevenseperators(nums)
    print("Odd numbers are ",oddnumbers)
    print("Even numbers are ",evennumbers)
main()