class conex:
    # Combined constructor
    def __init__(self, message="Hello guys!!", sender=None):
        self.message = message
        self.sender = sender

    def display(self):
        if self.sender:
            print(f"Message: {self.message} - From: {self.sender}")
        else:
            print(self.message)

# Create instances of the class using default and parameterized constructors
default_obj = conex()
param_obj = conex("Welcome to the class!")

# Call the display method
default_obj.display()  
param_obj.display()    
