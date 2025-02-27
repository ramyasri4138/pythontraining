class Parent:
    def __init__(self):
        self.bigNose = "7CM"  # Member variable
    def display_parent(self):  # Member function  #self is used to store the variables #member function 
        print("This is Parent Class")

class Child(Parent):
    def __init__(self):
        super().__init__()
    def display_child(self):  # Member function #self is the intermediate between caller and class, self is mandatory for fxn
        print("This is the child class")


# class Woman(Parent):
#     def display(self):
#         return super().display()

# Create an instance of Child
child = Child()
child.display_parent()
child.display_child()
print(child.bigNose)

p=Parent()
ch=Child()
p=ch
