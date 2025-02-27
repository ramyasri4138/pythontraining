class DefaultConstructor:
    def __init__(self):
        self.message="Default constructor example"
    def display(self):
        print(self.message)
#create an object
obj=DefaultConstructor()
obj.display()