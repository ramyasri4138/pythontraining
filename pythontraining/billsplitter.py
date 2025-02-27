def billsplitter(totalbill,noofpeople,tippercent):
    tip=(tippercent/100)*totalbill
    amount=totalbill+tip
    share=amount/noofpeople
    return share
    
totalbill=float(input("enter the total bill amount: "))
noofpeople=int(input("enter the number of people: "))
tippercent=float(input("enter the tip percentage "))
result=billsplitter(totalbill,noofpeople,tippercent)
print(f"Amount each person should pay is {result}")