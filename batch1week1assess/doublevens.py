numbers=list(map(int, input().split()))
def even(numbers):
    even_numbers = sorted([nums * 2 for nums in numbers if nums % 2 == 0])
    print(even_numbers)
even(numbers)   
        
list_num = list(map(int, input().split()))
numbers1 = sorted(map(lambda x:x*2,filter(lambda x:x %2 == 0 , list_num)))
print(numbers1)