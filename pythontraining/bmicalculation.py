def calculatebmi(weight,height):
    bmi=weight/(height**2)
    return bmi
def knowcategory(bmi):
    if bmi<18:
        return "Underweight"
    elif 18<=bmi<25:
        return "normal"
    elif 25<= bmi <30:
        return "Overweight"
    else:
        return "Obese"
def main():
    weight=float(input("enter weight in kg "))
    height=float(input("enter height in metres "))
    bmivalue=calculatebmi(weight,height)
    print(bmivalue)
    category=knowcategory(bmivalue)
    print(category)
main()
    