class Book:
    def __init__ (self, name:str, title:str, price:float):
        self.name=name
        self.title=title
        self.price=price
    @property
    def name(self):
        return self.__name


    @name.setter
    def name(self, value):
        if (any(char.isdigit() for char in value)) :
            print("Author not valid!")
            exit(0)
        else:
            self.__name=value
      
    @property        
    def title(self):
        return self.__title


    @title.setter
    def title(self, value):
        if len(value)<3:
            print("Title not valid!")
        else:
            self.__title=value
            
    @property  
    def price(self):
        return self.__price


    @price.setter
    def price(self, value):
        if value<0:
            print("Price not valid!")
        else:
            self.__price=value
    def __str__(self):
        return f"Type: Book \nTitle: {self.title} \nAuthor: {self.name} \nPrice: {self.price:.2f}"

        
class Golden(Book):
    def __init__(self, name, title, price):
        Book.__init__(self, name,title, price)

    @property
    def name(self):
        return self.__name


    @name.setter
    def name(self, value):
        if (any(char.isdigit() for char in value)) :
            print("Author not valid!")
            exit(0)
        else:
            self.__name=value
            
    @property        
    def title(self):
        return self.__title


    @title.setter
    def title(self, value):
        if len(value)<3:
            print("Title not valid!")
        else:
            self.__title=value
            
    @property  
    def price(self):
        return self.__price


    @price.setter
    def price(self, value):
        if value<0:
            print("Price not valid!")
        else:
            self.__price=value
    def __str__(self):
        return f"Type: GoldenEditionBook  \nTitle: {self.title} \nAuthor: {self.name} \nPrice: {self.price:.2f}"



name=input()
title=input()
price=float(input())
book=Book(name, title, price)
golden=Golden(name,title,price*30/100+price)
if not((any(char.isdigit() for char in name)) and len(title)<3 and price<0):
    print(book)
    print()
    print(golden)
