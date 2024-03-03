#Instance Variable | Instance Method

class House:
    def __init__(self):
        self.window = 4     #instance variable
        # self.window = ""     #instance variable
        self.door = 2       #instance variable
        
    def view(self):
        print("Windows:", self.window, "Door:", self.door)
        
#******************************

house1 = House()
house1.window = 6
house1.view()
house2 = House()
house2.door = 3
house2.view()