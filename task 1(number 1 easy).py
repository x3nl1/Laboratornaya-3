class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
    
    def __str__(self):
        return f"'{self.title}' - {self.author}"

if __name__ == "__main__":
    book = Book("1984", "Джордж Оруэлл")
    print(book)
