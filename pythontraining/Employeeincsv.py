import csv
import os

class Employee:
    def __init__(self, name, emp_id):
        self.name = name
        self.id = emp_id

    def display(self):
        print("The details are here!!")
        print("Name is : ", self.name)
        print("ID is : ", self.id)

    def save_to_csv(self, filename='employees.csv'):
        try:
            with open(filename, mode='a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow([self.name, self.id])
        except IOError:
            print("An error occurred while opening the file.")

def get_employee_input():
    name = input("Enter employee name: ")
    emp_id = input("Enter employee ID: ")
    return Employee(name, emp_id)

if __name__ == "__main__":
    while True:
        user_input = input("Do you want to add an employee? Type 'yes' to continue or 'exit' to stop: ")
        if user_input.lower() == 'exit':
            break
        # Create an instance of Employee with user input
        employee = get_employee_input()
        employee.display()
        # Save the instance details to a CSV file
        employee.save_to_csv()

    # To see where the file is saved
    print("Current Working Directory:", os.getcwd())




# import csv
# class Employee:
#     def __init__(self,name,id):
#         self.name=name
#         self.id=id
#     def display(self):
#         print("The details are here!!")
#         print("Name is : ",self.name)
#         print("ID is : ",self.id)
        
#     def save_to_csv(self, filename='employees.csv'):
#         with open(filename, mode='a', newline='') as file:
#             #this line creates a CSV writer object using the csv.writer function
#             writer = csv.writer(file)
#             writer.writerow([self.name, self.id])
        
# e=Employee("Ram",10)
# e.display()
# e.save_to_csv() # Save the instance details to a CSV file

# import os
# #to see where it is there
# print("Current Working Directory:", os.getcwd())

