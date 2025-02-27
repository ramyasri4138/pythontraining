from abc import ABC, abstractmethod

class Father(ABC):
    @abstractmethod
    def disp(self):
        pass
    def show(self):
        print("Concrete method")
        
class Son(Father):
    def disp(self):
        print("Son is implementing the abstract method")
class Daughter(Father):
    def disp(self):
        print("Daughter is implementing the abstract method")
        
#Creating objects 
s=Son()
s.disp()  #Output: Son is implementing the abstract method
s.show()  #output: Concrete method

d=Daughter()
d.disp() #output: Daughter is implementing the abstract method 
d.show() #output: Concrete method
