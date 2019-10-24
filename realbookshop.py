class Book :
    def __init__(self, name: str, title: str, price: float) :
        self.name = name
        self.title = title
        self.price = price

    def isValidAuthor(self, author: str):
        for s in author.split():
            if not s.isalpha():
                return  False
        return True

    @property
    def name(self) :
        return self.__name

    @name.setter
    def name(self, value: str) :
        if not self.isValidAuthor(value):
            print("Author not valid!")
            exit()
        else :
            self.__name = value

    @property
    def title(self) :
        return self.__title

    @title.setter
    def title(self, value) :
        if len(value) < 3 :
            print("Title not valid!")
            exit()
        else :
            self.__title = value

    @property
    def price(self) :
        return self.__price

    @price.setter
    def price(self, value) :
        if value < 0 :
            print("Price not valid!")
            exit()
        else :
            self.__price = value

    def __str__(self) :
        return f"Type: Book \nTitle: {self.title} \nAuthor: {self.name} \nPrice: {self.price:.2f}"


class Golden(Book) :
    def __init__(self, regular_book: Book) :
        Book.__init__(self, regular_book.name, regular_book.title, regular_book.price)

    @property
    def name(self) :
        return self.__name

    @name.setter
    def name(self, value: str) :
        if not self.isValidAuthor(value) :
            print("Author not valid!")
            exit()
        else :
            self.__name = value

    @property
    def title(self) :
        return self.__title

    @title.setter
    def title(self, value) :
        if len(value) < 3 :
            print("Title not valid!")
            exit()
        else :
            self.__title = value

    @property
    def price(self) :
        return self.__price

    @price.setter
    def price(self, value) :
        if value < 0 :
            print("Price not valid!")
        else :
            self.__price = 1.3 * value

    def __str__(self) :
        return f"Type: GoldenEditionBook  \nTitle: {self.title} \nAuthor: {self.name} \nPrice: {self.price:.2f}"


name = input()
title = input()
price = float(input())
book = Book(name, title, price)

print(book)
print()
print(Golden(book))
