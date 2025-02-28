# Magic methods are some dunder methods, are automatically called by python built in operations. Allows developers to define or customize the behavior of the objects
# eg -__init__, __main__, __str__


class Book:
    def __init__(self, title, author, num_page):
        self.title = title
        self.author = author
        self.num_page = num_page

    def __str__(self):
        return f"{self.title} by {self.author}"

    def __eq__(self, other):
        return self.title == other.title and self.author == other.author and self.num_page == other.num_page

    def __gt__(self, other):
        return self.num_page > other.num_page

    def __contains__(self, item):
        return item in self.title



book1 = Book("Oxford", "Britain", 2000)
book2 = Book("Harry Potter", "JK Rowling", 1010)

book3 = Book("Harry Potter", "JK Rowling", 2000)
book4 = Book("Harry Potter", "JK Rowling", 2000)

print(book3 == book4)
print(book3 > book1)
print("Potter" in book1)
