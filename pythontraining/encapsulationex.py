class Employee:
    # Constructor method
    def __init__(self, name, salary):
        self.__name = name  # Private attribute
        self.__salary = salary  # Private attribute

    # Setter method for salary
    def set_salary(self, salary):
        self.__salary = salary

    # Getter method for salary
    def get_salary(self):
        return self.__salary


# Create an Employee object
emp = Employee("Alice", 50000)

# Print salary before update
print("Salary before update:", emp.get_salary())

# Update the salary
emp.set_salary(60000)

# Print salary after update 
print("Salary after update:", emp.get_salary()) 