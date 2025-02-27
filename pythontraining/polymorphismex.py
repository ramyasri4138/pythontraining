class Cat:
    def sound(self):
        print("Meow")
class Dog:
    def sound(self):
        print("Bark")

for animal in[Cat(),Dog()]:
    animal.sound()
    
    
#this is overriding , the method overloading is not supported by python
# This creates a list of instances: one Cat object and one Dog object.
# The for loop iterates over the list of these objects.
# During each iteration, it calls the sound method on the current object (animal).

# What the Program Does:
# First Iteration:
# The animal is an instance of Cat.
# It calls Cat's sound method, which prints "Meow".

# Second Iteration:
# The animal is an instance of Dog.
# It calls Dog's sound method, which prints "Bark".