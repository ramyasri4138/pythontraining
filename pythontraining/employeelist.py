class employee:
    def __init__(self):
        self.message = "Just a Default constructor"
    
    def taking_input(self):
        self.name = input("Enter name: ")
        self.age = input("Enter age: ")

    def display(self):
        return [self.name, self.age]

# Create an instance of the class
emp = employee()

# Use method to take user input for name and age
emp.taking_input()

# Get and print the attributes as a list
print(emp.display())
emp.print_message()