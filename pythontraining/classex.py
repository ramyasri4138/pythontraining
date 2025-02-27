class car:
    def _init_(self,brand,model):
        self.brand=brand
        self.model=model
    def display_info(self):
        print(f"This car is a {self.brand}{self.model}")
car1=car("Toyota","Corolla")
car2=car("Honda","Civic")
car1.display_info()
car2.display_info()