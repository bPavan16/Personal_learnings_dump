class Library:
    def __init__(self):
        self.noBooks = 0
        self.books = []
    
    def addBooks(self,book):
        self.books.append(book)
        self.noBooks = len(self.books)

    def showinfo(self):
        print(f"The number of Books in The Library is {self.noBooks}")

l1 = Library()
l1.addBooks("Harry Potter")
l1.addBooks("Harry Potter 2")
l1.addBooks("Harry Potter 3")
l1.addBooks("Harry Potter 4")
l1.showinfo()
    
