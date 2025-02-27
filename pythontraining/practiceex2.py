# user_input=input("enter the values")
# inputs=user_input.split()
# for value in inputs:
#     print(value,end=' ')
    
listex=[]
n=int(input( ))
i=0     #initialization is mandatory
for i in range(n):
    value=int(input(f"{i+1}"))
    listex.append(value)
print(listex)
print("The numbers you entered are:", ' '.join(map(str ,listex)))
#int(input())---it doesn't take spaces while giving input...it returns an error
