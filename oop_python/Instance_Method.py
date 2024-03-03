class Student:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address
        # print(self.name, self.age)
        
    def details(self):
        print("Name:", self.name, "Age:", self.age, self.address)

        
St1 = Student("Arisha", 13, "")
print(St1.name, St1.age)
St1.details()

St2 = Student("Munira", 29, "Khulna")
print(St2.name, St2.age)
St2.details()
St2.details()
St2.details()


# Method Cara Onno attribute osongkho bar call kora zete pare

    
        