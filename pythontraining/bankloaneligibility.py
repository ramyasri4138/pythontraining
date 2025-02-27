def loan(salary,age,creditscore):
    if (age>18) and (salary>=50000) and creditscore>5:
        return 'approved'
    else:
        if age<=18:
            print("less than 18")
        if salary<50000:
            print("not meeting the requirement of salary")
        if creditscore<=5:
            print("credit score should be greater than 5")
        return 'rejected'
salary=int(input("enter the salary: "))
age=int(input("Enter the age: "))
creditscore=int(input("enter the credit score: "))
result=loan(salary,age,creditscore)
print(f"The loan status is {result}")