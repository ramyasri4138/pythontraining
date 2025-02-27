def secondlargest(nums):
    first=second=float('-inf')
    for num in nums:
        if num>first:
            second=first
            first=num
        elif first>num>second:
            second=num
    return second
def main():
    user_input=input("enter the numbers: ")
    nums=list(map(int,user_input.split()))
    seclargest=secondlargest(nums)
    print(f"the second largest: {seclargest}")
main()  