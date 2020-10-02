class TooManyPagesReadError(ValueError):
    pass


class Book:
    def __init__(self, name: str, page_count: int):
        self.name = name
        self.page_count = page_count
        self.pages_read = 0

    def __repr__(self):
        return(
            (f"<Book: {self.name}, # pages read: {self.pages_read} out of {self.page_count} pages>")
        )

    def read(self, pages: int):
        if self.pages_read + pages > self.page_count:
            raise TooManyPagesReadError(
                f"You tried to read {self.pages_read + pages} pages but that's more than { self.page_count} pages "
                f"- try again, you have {self.page_count - self.pages_read} pages left top read"
            )
        else:
            self.pages_read += pages
            print(f"You have read {self.pages_read} pages out of {self.page_count}. You have "
                  f"{self.page_count - self.pages_read} pages left to read")


python101 = Book('python101', 500)
print(python101)
try:
    python101.read(100)
    python101.read(200)
    python101.read(300)
    python101.read(150)
except TooManyPagesReadError as e:
    print(e)



