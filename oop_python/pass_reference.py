class Cat:
    def __init__(self, color, action):
        self.color = color
        self.action = action
        
    def view(self):
        print(f'The cat is {self.color} and {self.action}')
        
    def compare(self, other):
        if self.color == other.color and self.action == other.action:
            return True
        else:
            return False
        
cat1 = Cat('black', 'jumping')
cat2 = Cat('black', 'sleeping')

if cat1.compare(cat2): #Pass by reference
    print('The cats are the same')
else:
    print('The cats are different')
    
cat1.view()
cat2.view()


"""
What is Pass by Reference?

Pass by reference is a programming language feature that allows a function to modify the value of a variable outside of its scope. In other words, when you pass a variable to a function, you are passing a reference to the variable, not the actual value. This means that any changes made to the variable inside the function will be reflected in the original variable. In Python, all objects are passed by reference, which means that any changes made to an object inside a function will be reflected in the original object. This is in contrast to pass by value, where a copy of the variable is passed to the function, and any changes made to the variable inside the function do not affect the original variable."""
