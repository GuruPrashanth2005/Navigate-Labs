class Book:
    def __init__(self, title):
        self.title = title
        self.available = True

    def borrow(self):
        if self.available:
            self.available = False
            print("Borrowed")
        else:
            print("Not Available")

    def return_book(self):
        self.available = True
        print("Returned")

b = Book("Python")
b.borrow()
