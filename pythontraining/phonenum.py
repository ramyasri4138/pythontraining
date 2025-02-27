def get_input():
    phonenum=input("Enter the phonenumber ")
    return phonenum
def logic(phonenumber):
    phonenums={'0':'zero','1':'one','2':'Two','3':'three','4':'four','5':'five','6':'six','7':'seven','8':'eight','9':'nine'}
    output=[]
    for i in phonenumber:
        if i in phonenums:
            output.append(phonenums[i])
    return output
def main():
    phonenumber=get_input()
    result=logic(phonenumber)
    print(" ".join(result))
main()