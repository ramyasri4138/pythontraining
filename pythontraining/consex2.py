
class Example:
    def __init__(self,name):
        print(f"First constructor : hello{name}")
    def __init__(self,age):
        print(f"Second constructor : age is : {age}")
obj=Example(25)   #calls the second constructor

class Example:
    def __init__(self,*args):
        if len(args)==1:
            print(f"Hello: {args[0]}")
        elif len(args)==2:
            print(f"Hello: {args[0]}, you are {args[1]} years old")
obj1=Example("Alice")
obj2=Example("Bob",30)


class Example:
    def __init__(self,student_name=None,**kwargs):    #None i added
        self.student_name=student_name
        if "name" in kwargs and "age" in kwargs:
            print("Hello {kwargs['name']}, you are {kwargs['age']} years old")
        elif "name" in kwargs:
            print(f"hello {kwargs['name']}")
        self.xfield=kwargs['name']
obj1=Example(name="alice")
obj2=Example(name="bob",age=30)
print(obj1.student_name)
print(obj2.xfield)
        
        
       
class DestructorExample:
    def __init__(self,name):
        self.name=name               #I added
        print(f"Object {self.name} is created")
    def __del__(self):
        print(f"Object {self.name} is destroyed.")
        
#create and delete an object
obj=DestructorExample("Sample")
del obj
  
  
