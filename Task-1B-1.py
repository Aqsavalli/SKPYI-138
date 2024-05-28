class Book:
    def __init__(self, title, author, publisher, price):
        self._title = title
        self._author = author
        self._publisher = publisher
        self._price = price
        self._author_royalty = 0

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, value):
        self._author = value

    @property
    def publisher(self):
        return self._publisher

    @publisher.setter
    def publisher(self, value):
        self._publisher = value

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        self._price = value

    @property
    def author_royalty(self):
        return self._author_royalty

    @author_royalty.setter
    def author_royalty(self, value):
        self._author_royalty = value

    def royalty(self, copies_sold):
        royalty = 0
        if copies_sold <= 500:
            royalty = 0.1 * self._price * copies_sold
        elif copies_sold <= 1500:
            royalty = (0.1 * 500 * self._price) + (0.125 * self._price * (copies_sold - 500))
        else:
            royalty = (0.1 * 500 * self._price) + (0.125 * 1000 * self._price) + (0.15 * self._price * (copies_sold - 1500))
        self._author_royalty = royalty
        return royalty


book1 = Book("Python Programming", "GUIDO VAN ROSSUM", "Publisher Aqsa", 25)
print("The name of the Book is",book1.title)
print("The AUTHOR of the book is",book1.author)
print("The PUBLISHER of the book is",book1.publisher)
print("The PRICE of the book is",book1.price)
print("10% of the retail price on the first 500 copies is",book1.royalty(700))  
print("12.5% for the next 1,000 copies sold is",book1.author_royalty)  
class Ebook(Book):
    def __init__(self, title, author, publisher, price, ebook_format):
        super().__init__(title, author, publisher, price)
        self._ebook_format = ebook_format

    @property
    def ebook_format(self):
        return self._ebook_format

    @ebook_format.setter
    def ebook_format(self, value):
        self._ebook_format = value

    def royalty(self, copies_sold):
        royalty = super().royalty(copies_sold)
        if self._ebook_format:  
            royalty -= 0.12 * royalty
        return royalty


ebook1 = Ebook("Python Programming (ebook)", "GUIDO VAN ROSSUM", "Publisher Aqsa", 20, "PDF")
print("The TITLE of the ebooks is",ebook1.title)
print("The AUTHOR of the ebooks is",ebook1.author)
print("The PUBLISHER of the ebooks is",ebook1.publisher)
print("The PRICE of the ebooks is",ebook1.price)
print("The FORMAT of ebooks is",ebook1.ebook_format)
print("12% of GST on ebooks is",ebook1.royalty(700))  
