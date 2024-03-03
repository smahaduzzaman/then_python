import  book

class ImportedClass:
    def __init__(self):
        self.book = book.Book() # This is the line that causes the error
        
    def get_book(self):
        return self.book.get_price()