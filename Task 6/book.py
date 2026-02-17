class Book:
    def __init__(self, title, price):
        self.title = title
        self.__price = price
    def update_price(self, new_price):
        if new_price > 0:
            self.__price = new_price
            print("Price updated successfully")
        else:
            print("Invalid price")

    def get_price(self):
        return self.__price


book = Book("Python Basics", 500)
print("Current Price:", book.get_price())
book.update_price(600)
print("Updated Price:", book.get_price())
