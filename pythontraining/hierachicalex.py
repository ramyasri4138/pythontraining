#Parent Class
class Shape:
    def area(self):
        pass

#Child class 1
class Circle(Shape):
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        return 3.14*self.radius**2
    
#Child class 2
class Square(Shape):
    def __init__(self,side):
        self.side=side
    def area(self):
        return self.side**2

c=Circle(4)
s=Square(3)
print(c.area())
print(s.area())
