# Python 

class Library:
    def __init__(self):
        self.nobooks = 0
        self.books = []
    
    def addbook(self,book):
        self.books.append(book)
        self.nobooks = len(self.books)
    
    def showbooks(self):
        print(f"The library has {self.nobooks} books.")
        print("The books are:")
        for b in self.books:
            print(b)

l1 = Library()
l1.addbook("Harry Potter")
l1.addbook("Twilight")
l1.addbook("Marvel")
l1.addbook("Lord of the rings")

l1.showbooks()