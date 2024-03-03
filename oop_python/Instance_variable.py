class Car:
    
    def __init__(self, name, model):
        self.name = name
        self.model = model
        self.wheel = 4
        
    def view(self):
        print(self.name, "is built in", self.model, "and", "this is a", self.wheel, "wheel car")
    
    
car1 = Car("BMW", 1990)
car1.view()
car2 = Car("Tesla", 2002)
car2.wheel = 6
car2.view()