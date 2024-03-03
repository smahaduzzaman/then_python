class Dog:
    def __init__(self, name, color):
        self.name = name
        self.color = color
        
    def update_color(self, name, color):
        self.name = name
        self.color = color
        
    def barking(self, bark):
        self.bark = bark
        print(self.name, ",", self.color, "colored dog is barking", self.bark)
        
        
dog1 = Dog("Cooper", "Balck-White")
# print(dog1.name, dog1.color)
# dog1.update_color("Tommy", "red-white")
# dog1.barking("Ghew, Ghew")

print(dog1.__dict__)
print(dir(dog1)) 

"""
__dict__ Method Return All Attribute Values of a Class with a dictionary
dir() Method Returns Each and Everything of a Class
"""

dog2 = Dog("Buddy", "Yellow")
print(dog2.name)
    