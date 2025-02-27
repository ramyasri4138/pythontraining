class School:
    def __init__(self, name, location): #This is the constructor method for the School class. It initializes the name and location attributes.
        self.name = name
        self.location = location

    def school_data(self):
        print(f"School Name: {self.name}, Location: {self.location}")

class UnderG(School):
    def __init__(self, name, location, undergrad_program):
        super().__init__(name, location) #It calls the parent class's constructor using super().__init__(name, location) to initialize the name and location attributes, and then initializes the undergrad_program attribute.
        self.undergrad_program = undergrad_program

    def UnderG_data(self):
        print(f"Undergraduate Program: {self.undergrad_program}")

class PostG(School):
    def __init__(self, name, location, postgrad_program):
        super().__init__(name, location)
        self.postgrad_program = postgrad_program

    def PostG_data(self):
        print(f"Postgraduate Program: {self.postgrad_program}")

# Create instances
u = UnderG("ABC University", "City A", "Computer Science")
p = PostG("XYZ University", "City B", "Data Science")

# Access school data and specific program data
u.school_data()
u.UnderG_data()
p.school_data()
p.PostG_data()