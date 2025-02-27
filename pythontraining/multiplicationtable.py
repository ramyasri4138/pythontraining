def multiplytable(number,end):
    start=1
    for i in range(start,end+1):
        print(f"{number}X{i}={number*i}")

end=int(input("enter the range: "))
number=int(input("enter a number of which multiplication table is req: "))
multiplytable(number,end)
