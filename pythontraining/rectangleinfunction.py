def greet():
    print("Helllo")
greet()
    
def display(data):
    print(f"The area is {data}")
def get_input():
    recieved_length=input("Length: ")
    recieved_width=input("width: ")
    return(recieved_length,recieved_width)
def compute_area(length,width):
    area=int(length)*int(width)
    return area
def main():
    (length,width)=get_input()
    area=compute_area(length,width)
    display(area)

main()



