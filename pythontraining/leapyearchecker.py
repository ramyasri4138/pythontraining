def leapyearcheck(year):
    if ((year%4==0) and (year%100!=0)) or year%400==0:
        return True
    else:
        return False
    
def main():
    while(True):
        year=int(input("enter the year to be checked or exit: "))
        if year=='exit':
            print("exiting out of the loop")
            break
        if leapyearcheck(year):
            print(f"{year} is a leap year")
        else:
            print(f"{year} is not a leap year")
main()
        