from abc import ABC, abstractmethod

class Item(ABC):
    @abstractmethod
    def __init__(self, id:str, op:str, price:float):
        self.id=id
        self.op=op
        self.price=price

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, value):
        if not value.isalpha() or len(value) < 8 :
            print("Invalid id!")
        else:
            self.__age = value

    @property
    def price(self):
        return self._price

    @price.setter
    def price (self,value):
        if value>0:
            self._price=value
        else:
            raise Exception("Invalid price")

    def __str__(self):
        return f"Item id: {self.id}\nOperating system: {self.op}\nPrice: {self.price}"

class Phone(Item):
    @abstractmethod
    def __init__(self,id:str,op:str,price:float):
        Item.__init__(self,id,op,price)

    def make_call(self):
        return "Making call..."

    def receive_call(self):
        return "Receiving a call!"

    def send_message(self):
        return "Sending message..."

    def receive_message(self):
        return "Receiving a message!"
class SmartPhone(Phone):
    def __init__(self,id:str,op:str,price:float,apps:[]):
        Phone.__init__(self,id,op,price)
        self.apps=apps

    @property
    def apps(self):
        return self.__apps

    @apps.setter
    def apps(self, value):
        if len(value)<5:
            print("Invalid number of applications!")
        else:
            self.__age = value

    def browse(self):
        return "Browsing..."

    def __str__(self):
        a= f"Item id: {self.id}\nOperating system: {self.op}\nPrice: {self.price}"
        b= f"Applications: {','.join(self.apps)}"
        return f"{a}\n{b}"

class CellPhone(Phone):
    def __init__(self, id: str, op: str, price: float):
        Phone.__init__(self, id, op, price)

class Tablet(Item):
    def __init__(self, id: str, op: str, price: float):
        Item.__init__(self, id, op, price)
    def Streem(self):
        return "Streaming movie..."

items={}
data=input()
while not data=="end":
    try:
        item=eval(data)
        id=data.split(", ")[0].split("(")[1].lstrip('"').rstrip('"')
        if not items.get(id):
            items[id]=item
    except Exception as ex:
        print(ex)

    data=input()
report=input().split()
while not report[0]=="end":
    if report[0] == "test":
        if report[1] in items.keys():
            my_item=items[report[1]]
            my_class=my_item.__class__.__name__
            if report[2] in dir(my_item):
                if my_class=="Tablet":
                    method=getattr(Tablet,data[2])
                    method(my_item)
                if my_class=="CellPhone":
                    method=getattr(CellPhone,data[2])
                    method(my_item)
                if my_class == "SmartPhone":
                    method = getattr(SmartPhone, data[2])
                    method(my_item)
            else:
                print("Invalid request has been made!")
        else:
            print("Invalid request has been made!")
    if report[0]=="report":
        if report[1]=="Tablet":
            for i in items.values():
                if isinstance(i,Tablet):
                    print(i)
        if report[1]=="CellPhone":
            for i in items.values():
                if isinstance(i,CellPhone):
                    print(i)
        if report[1]=="SmatPhone":
            for i in items.values():
                if isinstance(i,SmartPhone):
                    print(i)
        else:
            print("Invalid request has been made!")

    report = input().split()











