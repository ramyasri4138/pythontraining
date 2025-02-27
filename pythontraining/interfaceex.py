from abc import ABC ,abstractmethod

class Father(ABC):
    @abstractmethod
    def disp(self):     #the abstract method should be implemented in every class else:error
        pass
#my=Father() #not possible to create an object for an abstract class

class Child(Father):
    def disp(self):
        print("child class")
        print("Defining abstract method")
class Relative(Father):
    def disp(self):
        print("Relative class")
r=Relative()     
c=Child()
c.disp()
r.disp()
