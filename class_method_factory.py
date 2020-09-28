class Book:
    TYPES = ("hardcover", "paperback")

    def __init__(self, name, book_type, weight):
        self.name = name
        self.book_type = book_type
        self.weight = weight

    def __repr__(self):
        return f"<Book {self.name}, {self.book_type}, weighing {self.weight} gm.>"

    @classmethod
    def hardcover(cls, name, weight):
        return Book(name, Book.TYPES[0], weight + 100)

    @classmethod
    def paperback(cls, name, weight):
        return Book(name, Book.TYPES[1], weight)


book3 = Book.hardcover("Harry Potter", 1500)
print(book3)

book4 = Book.paperback("2001", 800)
print(book4)



# print(Book.TYPES)
# print(Book)
#
# book1 = Book('The Shining', "hardcover", 1500)
# print(f"{book1.name} is a {book1.type} and weighs: {book1.weight} grams")
# # with the REPR method present we can:
# print(book1)
#
