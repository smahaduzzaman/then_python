class Book:
    def __init__(self, name, author):
        self.name = name
        self.author = author
        self.price = 0
        
    def set_price(self, price):
        self.price = price
        
    def get_price(self):
        return (self.name, "is written by", self.author, "and it's price is", self.price)
    
book1 = Book("Firye Aye", "S M Ahaduzzaman")
print(book1.__dict__)
book1.set_price(500)
# print(book1.__dict__)
bk = book1.get_price()
print(bk)